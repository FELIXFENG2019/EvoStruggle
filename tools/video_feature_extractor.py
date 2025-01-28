import os
import sys
import tqdm
import json
import argparse
import numpy as np
import pandas as pd

import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision.io import read_video
import torchvision.transforms as T
from pytorchvideo.data import UniformClipSampler



def get_arguments():
    '''
    parse all the arguments from command line inteface
    return a list of parsed arguments
    '''

    parser = argparse.ArgumentParser(
        description='feature extraction')
    parser.add_argument(
        '--dataset_dir', type=str, default='/media/alexa/WORKSPACE/Shijia-stage-two/new_struggle_dataset/', help='path to dataset directory')
    parser.add_argument(
        '--save_dir', type=str, default='/media/alexa/WORKSPACE/Shijia-stage-two/new_struggle_dataset/extracted_features', 
        help='path to the directory you want to save video features')
    parser.add_argument(
        '--task', type=str, default='Origami', help='task name', choices=['Origami', 'Shuffle_Cards', 'Tangram', 'Tying_Knots'])
    parser.add_argument(
        '--arch', type=str, default='slowfast', help='model architecture. (slowfast)')
    parser.add_argument(
        '--size', type=int, default=256, help='input image size')
    parser.add_argument(
        '--window_size', type=int, default=32, help='sliding window size')
    parser.add_argument(
        '--stride', type=int, default=16, help='sliding window stride')
    parser.add_argument(
        '--num_workers', type=int, default=0, help='the number of workes for data loding')
    parser.add_argument(
        '--clip_batch_size', type=int, default=1, help='the number of clips of a video to be processed at once')

    return parser.parse_args()
    

def extract_features(model, loader, clip_batch_size, save_dir, window_size, image_size, device):
    '''
    extract features from video clips and save them to .npy files
    '''
    model.eval()

    for j, sample in enumerate(loader):
        # print the progress 
        print(f'Videos processed: {j+1}/{len(loader)}')
        with torch.no_grad():
            name = sample['name'][0]
            vid_path = sample['vid_path'][0]
            clip_offsets = sample['clip_offsets']
            num_clips = len(clip_offsets)
            annotations = sample['annotations']

            # if features already exist, the below process will be passes.
            if os.path.exists(os.path.join(save_dir, name + '.npy')):
                continue
            
            # calculate the number of iterations given the clip_batch_size
            num_batches = num_clips // clip_batch_size
            remainder = num_clips % clip_batch_size
            num_iter = num_batches if remainder == 0 else num_batches + 1

            feats = []
            with tqdm.tqdm(total=num_iter, desc=f'Extracting features from video {name}') as pbar:       
                for i in range(num_iter):
                    start = i * clip_batch_size
                    end = min((i + 1) * clip_batch_size, num_clips)
                    # print(start, end)
                    stack_frames = []
                    for j in range(start, end):
                        frames, _, _ = read_video(vid_path, start_pts=clip_offsets[j][0].item(), end_pts=clip_offsets[j][1].item(), pts_unit='sec') # output: (T=window_size, H, W, C)
                        frames = frames.permute(0, 3, 1, 2) # shape (T, C, H, W)
                        frames = frames[:window_size] # truncate the frames to the window size
                        # print(frames.shape)
                        # Resize to shorter side 256, then center crop to 256*256
                        frames = frames / 255.0
                        mean = frames.mean(dim=[0, 2, 3])
                        std = frames.std(dim=[0, 2, 3])
                        transforms = T.Compose([
                            T.Resize([image_size, ]),
                            T.CenterCrop(image_size),
                            T.Normalize(mean, std)
                        ])
                        frames = transforms(frames) 
                        stack_frames.append(frames)
                    clip = torch.stack(stack_frames, dim=0) # (N, T, C, H, W) N is the number of clips
                    # (N, T, C, H, W) -> (N, C, T, H, W)
                    clip = clip.permute(0, 2, 1, 3, 4).contiguous()
                    slow_input_clip = clip[:, :, ::8, :, :].to(device, dtype=torch.float32)
                    fast_input_clip = clip[:, :, ::2, :, :].to(device, dtype=torch.float32)
                    feat = model([slow_input_clip, fast_input_clip])
                    feats.append(feat.to('cpu')) # (N, 2304)
                    pbar.update(1)

            feats = torch.cat(feats, dim=0) # (N', 2304)
            np.save(os.path.join(save_dir, name + '.npy'), feats.numpy())
            # print(feats.shape)


class VideoDataset(torch.utils.data.Dataset):
    def __init__(self, root_dir, task_name, image_size=256, window_size=32, stride=16):
        
        self.root_dir = root_dir
        self.video_path = os.path.join(root_dir, 'data', '360p', task_name)
        self.video_list = os.listdir(self.video_path)
        self.image_size = image_size # centre crop image size to 256*256 for feature extraction
        self.window_size = window_size
        self.stride = stride

        if task_name == 'Origami':
            self.annotation_path = os.path.join(root_dir, 'annotations', 'origami_tsa_full.csv')
        elif task_name == 'Shuffle_Cards':
            self.annotation_path = os.path.join(root_dir, 'annotations', 'shufflecards_tsa_full.csv')
        elif task_name == 'Tangram':
            self.annotation_path = os.path.join(root_dir, 'annotations', 'tangram_tsa_full.csv')
        elif task_name == 'Tying_Knots':
            self.annotation_path = os.path.join(root_dir, 'annotations', 'tyingknots_tsa_full.csv')
        
        self.annotation = pd.read_csv(self.annotation_path)
        self.annotation['keyframes'] = self.annotation['keyframes'].apply(json.loads)
        self.annotation['keyframes(frames)'] = self.annotation['keyframes(frames)'].apply(json.loads)
        self.annotation['struggle'] = self.annotation['struggle'].apply(json.loads)
        self.annotation['struggle(frames)'] = self.annotation['struggle(frames)'].apply(json.loads)

        self.data = []
        # sort the video list by name
        self.video_list.sort()
        for vid in self.video_list:
            vid_name = vid.split('.')[0]
            vid_path = os.path.join(self.video_path, vid) # path to video file
            video_metadata = self.annotation[self.annotation['video_name'] == vid_name]
            duration = video_metadata['duration'].values[0]
            fps = video_metadata['fps'].values[0]
            # import pdb; pdb.set_trace()
            clipsampler = UniformClipSampler(clip_duration=self.window_size/fps, stride=self.stride/fps, backpad_last=True)
            clip_info = []
            last_clip_time = 0.0 # start from the beginning
            while True:
                clip_start_time, clip_end_time, clip_index, aug_index, is_last_clip = clipsampler(last_clip_time=last_clip_time, video_duration=duration, annotation=None)
                clip_info.append([float(clip_start_time), float(clip_end_time)])
                last_clip_time = clip_end_time
                if is_last_clip:
                    break
            self.data.append((vid_name, vid_path, clip_info, video_metadata.to_dict('records')[0]))
        print("Video Dataset Initialization Complete!")
        
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        name, path, clip_info, metadata = self.data[idx] # metadata is a dictionary containing the struggle annotations
        """
        stack_frames = []
        # print(f'loading clips from video: {name}...')
        with tqdm.tqdm(total=len(clip_info), desc=f'Loading clips from video {name}') as pbar:
            for clip in clip_info:
                frames, _, _ = read_video(path, start_pts=clip[0], end_pts=clip[1], pts_unit='sec') # output: (T, H, W, C)
                frames = frames.permute(0, 3, 1, 2) # shape (T, C, H, W)
                frames = frames[:self.window_size] # truncate the frames to the window size
                # print(frames.shape)
                # Resize to shorter side 256, then center crop to 256*256
                frames = frames / 255.0
                mean = frames.mean(dim=[0, 2, 3])
                std = frames.std(dim=[0, 2, 3])
                transforms = T.Compose([
                    T.Resize([self.image_size, ]),
                    T.CenterCrop(self.image_size),
                    T.Normalize(mean, std)
                ])
                frames = transforms(frames) 
                stack_frames.append(frames)
                pbar.update(1)
        stack_frames = torch.stack(stack_frames, dim=0) # (N, T, C, H, W) N is the number of clips
        """

        return {
            'name': name,
            'vid_path': path,
            'clip_offsets': clip_info,
            'annotations': metadata
        }
        


def main():
    args = get_arguments()

    # dataset, dataloader
    data = VideoDataset(
        args.dataset_dir,
        args.task,
        args.size,
        args.window_size,
        args.stride
    )

    loader = DataLoader(
        data,
        batch_size=1,
        shuffle=False,
        num_workers=args.num_workers,
        pin_memory=True
    )

    # load model
    print('\n------------------------Loading Model------------------------\n')

    if args.arch == 'slowfast':
        print('SlowFast-R50 will be used as a model.')
        model = torch.hub.load('facebookresearch/pytorchvideo', 'slowfast_r50', pretrained=True)
        model.blocks[6].proj = torch.nn.Identity() # remove the last layer of the model to extract features in 2304 dim
        model.blocks[5].pool[0] = torch.nn.AdaptiveAvgPool3d((1, 1, 1))
        model.blocks[5].pool[1] = torch.nn.AdaptiveAvgPool3d((1, 1, 1))
        # make save directory
        if not os.path.exists(os.path.join(args.save_dir, 'slowfast_features')):
            os.makedirs(os.path.join(args.save_dir, 'slowfast_features'))
        if not os.path.exists(os.path.join(args.save_dir, 'slowfast_features', args.task)):
            os.makedirs(os.path.join(args.save_dir, 'slowfast_features', args.task))
        save_dir = os.path.join(args.save_dir, 'slowfast_features', args.task)
    else:
        print('There is no model appropriate to your choice.')
        sys.exit(1)

    # send the model to cuda/cpu
    if torch.cuda.is_available():
        device = 'cuda'
        print(f'Using device {device}.')
        print(f'Number of GPUs: {torch.cuda.device_count()}')
        torch.backends.cudnn.benchmark = True
        model.to(device)
        # if torch.cuda.device_count() > 1:
            # model = nn.DataParallel(model)
    else:
        device = 'cpu'
        print(f'Using device {device}.')
        model.to(device)

    # extract and save features
    print('\n------------------------Start extracting features------------------------\n')
    extract_features(model, loader, args.clip_batch_size, save_dir, args.window_size, args.size, device)
    print("Done!")


if __name__ == '__main__':
    main()

