import os
import csv
import argparse


parser = argparse.ArgumentParser(description='Codes for moving the video file from backup directory to the workspace directory')
parser.add_argument('-source_path', '-source', type=str, default="/media/alexa/DATA")
parser.add_argument('-source_subfolder_name', '-sfname', type=str, default="Origami", choices=['Origami', 'Shuffle_Cards', 'Tangram', 'Tying_Knots'])
parser.add_argument('-target_path', '-target', type=str, default="/media/alexa/WORKSPACE/Shijia-stage-two/new_struggle_dataset/data/")
parser.add_argument('-resolution', '-res', type=str, default="360p", choices=['360p', '1080p'], help='select the resolution of the video to be moved')
parser.add_argument('-target_subfolder_name', '-tfname', type=str, default="Origami", choices=['Origami', 'Shuffle_Cards', 'Tangram', 'Tying_Knots'])
parser.add_argument('-annotation_path', '-ann', type=str, default="/media/alexa/WORKSPACE/Shijia-stage-two/new_struggle_dataset/annotations/")
parser.add_argument('-annotation_file', '-annfile', type=str, default="origami_tsa_full.csv", 
                    choices=['origami_tsa_full.csv', 'shufflecards_tsa_full.csv', 'tangram_tsa_full.csv', 'tyingknots_tsa_full.csv'])
args = parser.parse_args()


source_path = os.path.join(args.source_path, args.source_subfolder_name)
target_path = os.path.join(args.target_path, args.resolution, args.target_subfolder_name)
annotation_path = os.path.join(args.annotation_path, args.annotation_file)


# start from the annotation csv file, for each video name find the corresponding video file and move it to the target directory
with open(annotation_path, 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        video_name = row[0]
        # import pdb; pdb.set_trace()
        participant_id = str(int(video_name.split('_')[0])) # e.g. convert 01 to 1
        if args.resolution == '360p':
            source_video_name = video_name + '_360p.mp4'
            video_path = os.path.join(source_path, f'Participant{participant_id}', args.resolution.upper(), source_video_name)
        elif args.resolution == '1080p':
            source_video_name = video_name
            video_path = os.path.join(source_path, f'Participant{participant_id}', source_video_name)
        else:
            print('Invalid resolution!')
            break
        target_video_path = os.path.join(target_path, video_name+'.mp4')
        # copy the video file to the target directory
        os.system(f'cp {video_path} {target_video_path}')
        print(f'Video {video_name} is moved to {target_video_path}')

print('All videos are moved successfully!')

# Run this script with the following command:
# python video_mover.py -source /media/alexa/DATA -source_subfolder_name Origami -target /media/alexa/WORKSPACE/Shijia-stage-two/new_struggle_dataset/data/ -resolution 360p -target_subfolder_name Origami -annotation_path /media/alexa/WORKSPACE/Shijia-stage-two/new_struggle_dataset/annotations/ -annotation_file origami_tsa_full.csv
# python video_mover.py -source /media/alexa/DATA -source_subfolder_name Shuffle_Cards -target /media/alexa/WORKSPACE/Shijia-stage-two/new_struggle_dataset/data/ -resolution 360p -target_subfolder_name Shuffle_Cards -annotation_path /media/alexa/WORKSPACE/Shijia-stage-two/new_struggle_dataset/annotations/ -annotation_file shufflecards_tsa_full.csv
# python video_mover.py -source /media/alexa/DATA -source_subfolder_name Tangram -target /media/alexa/WORKSPACE/Shijia-stage-two/new_struggle_dataset/data/ -resolution 360p -target_subfolder_name Tangram -annotation_path /media/alexa/WORKSPACE/Shijia-stage-two/new_struggle_dataset/annotations/ -annotation_file tangram_tsa_full.csv
# python video_mover.py -source /media/alexa/DATA -source_subfolder_name Tying_Knots -target /media/alexa/WORKSPACE/Shijia-stage-two/new_struggle_dataset/data/ -resolution 360p -target_subfolder_name Tying_Knots -annotation_path /media/alexa/WORKSPACE/Shijia-stage-two/new_struggle_dataset/annotations/ -annotation_file tyingknots_tsa_full.csv

# The script will move the video files from the backup directory to the workspace directory based on the annotation csv file.

