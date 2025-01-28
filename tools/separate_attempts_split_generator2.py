import os
import csv
import json
import argparse
import numpy as np
import pandas as pd


parser = argparse.ArgumentParser(description='Codes for splitting the train/validation/test data for training on separate attempts')
parser.add_argument('-domain_name', '-dname', type=str, default="Origami", choices=['Origami', 'Shuffle_Cards', 'Tangram', 'Tying_Knots'])
parser.add_argument('-split_path', '-spath', type=str, default="/media/alexa/WORKSPACE/Shijia-stage-two/new_struggle_dataset/splits/separate_attempts/")
parser.add_argument('-save_path', '-save', type=str, default="/media/alexa/WORKSPACE/Shijia-stage-two/new_struggle_dataset/splits/separate_attempts/")
parser.add_argument('--save_file_suffix', '-suffix', type=str, default="allattempts_sample01")
parser.add_argument('--random_seed', '-seed', type=int, default=42)
args = parser.parse_args()


def df_rows_to_dict(df, sebset, json_data):
    for index, row in df.iterrows():
        # Extract values from the row
        video_name = row['video_name']
        duration = row['duration']
        fps = row['fps']

        # Create a dictionary for the video entry
        video_dict = {
            "subset": sebset,  # Assuming all videos are in the Test subset
            "duration": duration,
            "fps": fps,
            "annotations": []
        }
        # import pdb; pdb.set_trace()
        # Create a dictionary for the struggle annotation (adjust if needed)
        row['struggle'] = json.loads(row['struggle'])
        row['struggle(frames)'] = json.loads(row['struggle(frames)'])
        if len(row['struggle']) > 0:
            for idx, segment_items in enumerate(row['struggle']):
                struggle_annotation = {
                    "label": "Struggle",  # Replace with your desired label
                    "segment": segment_items,  # Replace with actual struggle segment
                    "segment(frames)": row['struggle(frames)'][idx],  # Replace with actual struggle segment in frames
                    "label_id": 1  # Replace with your desired label ID
                }
                # Add the struggle annotation to the video's annotations list
                video_dict["annotations"].append(struggle_annotation)

        # Add the video entry to the database dictionary
        json_data["database"][video_name] = video_dict
    return json_data


print(f"Currently preparing activity name: {args.domain_name}")
args.split_path = os.path.join(args.split_path, args.domain_name)
args.save_path = os.path.join(args.save_path, args.domain_name)
seed = args.random_seed
if not os.path.exists(args.save_path):
    os.makedirs(args.save_path)

json_data = {
    "version": "separate_attempts",
    "database": {}
}
 
# the other domains should be combined and used as trian/validation set
csv_file_name = args.domain_name + '_' + 'train.csv'
df = pd.read_csv(os.path.join(args.split_path, csv_file_name))
# import pdb; pdb.set_trace()
# forming subsets for each of the df['attemptID'] ranging from 01 to 05 and then random select 20% to form the final training set
selected_df_ls = []
for i in range(1, 6):
    # import pdb; pdb.set_trace()
    sub_df = df.loc[df['attemptID'] == i]
    num_samples = round(len(sub_df)/5.)
    sub_df_indices = np.array(sub_df.index.tolist())
    np.random.seed(seed)
    sampled_indices = np.random.choice(sub_df_indices, num_samples, replace=False)
    sampled_indices_ls = sampled_indices.tolist()
    sampled_indices_ls.sort()
    # fetch the rows from the sub_df according to the row index
    mask = np.isin(sub_df.index, sampled_indices_ls)
    selected_df_ls.append(sub_df[mask])

sampled_train_df = pd.concat(selected_df_ls, ignore_index=True)
json_data = df_rows_to_dict(sampled_train_df, 'train', json_data)

csv_file_name = args.domain_name + '_' + 'val.csv'
df = pd.read_csv(os.path.join(args.split_path, csv_file_name))
json_data = df_rows_to_dict(df, 'validation', json_data)

# Save the JSON data to a file
with open(os.path.join(args.save_path, f"{args.domain_name}_{args.save_file_suffix}.json"), 'w') as fp:
    json.dump(json_data, fp, indent=4)   

print("Done!")

# Run this script with the following command:
# seed = [42, 123, 123456] for allattempts_sample01, allattempts_sample02, allattempts_sample03
# python separate_attempts_split_generator2.py -domain_name Origami -seed 42 -suffix allattempts_sample01
# python separate_attempts_split_generator2.py -domain_name Shuffle_Cards -seed 42 -suffix allattempts_sample01
# python separate_attempts_split_generator2.py -domain_name Tangram -seed 42 -suffix allattempts_sample01
# python separate_attempts_split_generator2.py -domain_name Tying_Knots -seed 42 -suffix allattempts_sample01
    

