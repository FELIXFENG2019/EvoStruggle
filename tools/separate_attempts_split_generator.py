import os
import csv
import json
import argparse
import pandas as pd


parser = argparse.ArgumentParser(description='Codes for splitting the train/validation/test data for training on separate attempts')
parser.add_argument('-domain_name', '-dname', type=str, default="Origami", choices=['Origami', 'Shuffle_Cards', 'Tangram', 'Tying_Knots'])
parser.add_argument('-split_path', '-spath', type=str, default="/media/alexa/WORKSPACE/Shijia-stage-two/new_struggle_dataset/splits/separate_attempts/")
parser.add_argument('-save_path', '-save', type=str, default="/media/alexa/WORKSPACE/Shijia-stage-two/new_struggle_dataset/splits/separate_attempts/")
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
if not os.path.exists(args.save_path):
    os.makedirs(args.save_path)

json_data = {
    "version": "separate_attempts",
    "database": {}
}
 
# the other domains should be combined and used as trian/validation set
csv_file_name = args.domain_name + '_' + 'train.csv'
df = pd.read_csv(os.path.join(args.split_path, csv_file_name))
# group according to df['attemptID'] from 01 to 05 and then split into train_attempt01 to train_attempt05
for i in range(1, 6):
    # import pdb; pdb.set_trace()
    json_data = df_rows_to_dict(df.loc[df['attemptID'] == i], f'train_attempt0{i}', json_data)
    # print the number of videos in each split
    print(f"Number of videos in train_attempt0{i}: {len(df.loc[df['attemptID'] == i])}")

csv_file_name = args.domain_name + '_' + 'val.csv'
df = pd.read_csv(os.path.join(args.split_path, csv_file_name))
json_data = df_rows_to_dict(df, 'validation', json_data)

# Save the JSON data to a file
with open(os.path.join(args.save_path, f"{args.domain_name}_sepattempt.json"), 'w') as fp:
    json.dump(json_data, fp, indent=4)   

print("Done!")

# Run this script with the following command:
# python separate_attempts_split_generator.py -domain_name Origami 
# python separate_attempts_split_generator.py -domain_name Shuffle_Cards 
# python separate_attempts_split_generator.py -domain_name Tangram 
# python separate_attempts_split_generator.py -domain_name Tying_Knots 
    

