import os
import csv
import json
import argparse
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


parser = argparse.ArgumentParser(description='Codes for splitting the train/test data for in-domain generalization')
parser.add_argument('-domain_name', '-dname', type=str, default="Origami", choices=['Origami', 'Shuffle_Cards', 'Tangram', 'Tying_Knots'])
parser.add_argument('-annotation_path', '-ann', type=str, default="/media/alexa/WORKSPACE/Shijia-stage-two/new_struggle_dataset/annotations/")
parser.add_argument('-annotation_file', '-annfile', type=str, default="origami_tsa_full.csv", 
                    choices=['origami_tsa_full.csv', 'shufflecards_tsa_full.csv', 'tangram_tsa_full.csv', 'tyingknots_tsa_full.csv'])
parser.add_argument('-save_path', '-save', type=str, default="/media/alexa/WORKSPACE/Shijia-stage-two/new_struggle_dataset/splits/indomain_generalization/")
parser.add_argument('-seed', type=int, default=42)
parser.add_argument('-trainval_split_ratio', '-splitrate', type=float, default=0.2)
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


df_original = pd.read_csv(os.path.join(args.annotation_path, args.annotation_file))
df = df_original.copy() # the df will be added with new columns
df['participantID'] = df['video_name'].apply(lambda x: x.split('_')[0])
df['subactivityID'] = df['video_name'].apply(lambda x: x.split('_')[1])
df['attemptID'] = df['video_name'].apply(lambda x: x.split('_')[2])

df['struggle'] = df['struggle'].apply(json.loads)
df['struggle_durations'] = df['struggle'].apply(lambda x: [item[1] - item[0] for item in x] if len(x) > 0 else [])
df['total_struggle_duration'] = df['struggle_durations'].apply(lambda x: sum(x))
df['struggle_proportions'] = df['total_struggle_duration'] / df['duration']
df['struggle_proportions'] = df['struggle_proportions'].apply(lambda x: round(x, 2))

# quantize the struggle proportions
# df['struggle_proportions'] = pd.qcut(df['struggle_proportions'], q=5, labels=False)

# import pdb; pdb.set_trace()
# df_participant = df.groupby('participantID', group_keys=True).mean()
# train_df, val_df = train_test_split(df_participant, test_size=0.2, random_state=42, stratify=pd.qcut(df_participant['struggle_proportions'], q=5, labels=False))

args.save_path = os.path.join(args.save_path, args.domain_name)
if not os.path.exists(args.save_path):
    os.makedirs(args.save_path)

# The rows containing the same subactivityID form a test set, while the rest form a train set
for subactivity in df['subactivityID'].unique():
    print(f"Subactivity: {subactivity}")
    subactivity_df = df[df['subactivityID'] == subactivity]
    test_idx = subactivity_df.index
    train_idx = df.index.difference(test_idx)
    # import pdb; pdb.set_trace()
    # form the new dataframes
    test_df = df.loc[test_idx] # this is the held-out test set for the unseen subactivity
    train_df = df.loc[train_idx]
    
    # further split the train set into train and validation sets
    df_participant = train_df.groupby('participantID', group_keys=True).mean()
    train_participant_df, val_participant_df = train_test_split(
        df_participant, 
        test_size=args.trainval_split_ratio, 
        random_state=args.seed, 
        stratify=pd.qcut(df_participant['struggle_proportions'], q=5, labels=False))

    train_participant_ids = train_participant_df.index
    val_participant_ids = val_participant_df.index

    new_train_df = train_df[train_df['participantID'].isin(train_participant_ids)]
    val_df = train_df[train_df['participantID'].isin(val_participant_ids)]
    # import pdb; pdb.set_trace()

    # plot the struggle proportions histogram
    sns.histplot(new_train_df['struggle_proportions'], stat='count', bins=20, kde=True)
    plt.savefig(os.path.join(args.save_path, f"{args.domain_name}_subactivity{subactivity}_train_struggle_proportions.png"))
    plt.close()
    sns.histplot(val_df['struggle_proportions'], stat='count', bins=20, kde=True)
    plt.savefig(os.path.join(args.save_path, f"{args.domain_name}_subactivity{subactivity}_val_struggle_proportions.png"))
    plt.close()
    sns.histplot(test_df['struggle_proportions'], stat='count', bins=20, kde=True)
    plt.savefig(os.path.join(args.save_path, f"{args.domain_name}_subactivity{subactivity}_test_struggle_proportions.png"))
    plt.close()

    # save the dataframes
    test_df.to_csv(os.path.join(args.save_path, f"{args.domain_name}_subactivity{subactivity}_unseentest.csv"), index=False)
    new_train_df.to_csv(os.path.join(args.save_path, f"{args.domain_name}_subactivity{subactivity}_train.csv"), index=False)
    val_df.to_csv(os.path.join(args.save_path, f"{args.domain_name}_subactivity{subactivity}_val.csv"), index=False)
    print(f"Test set: {len(test_df)} samples")
    print(f"Train set: {len(new_train_df)} samples")
    print(f"Validation set: {len(val_df)} samples")

    # convert train_df, val_df, and test_df to json format and save in one json file
    json_data = {
        "version": "generalization_test1",
        "database": {}
    }
    # Iterate through each row of the DataFrame
    json_data = df_rows_to_dict(new_train_df, 'Train', json_data)
    json_data = df_rows_to_dict(val_df, 'Validation', json_data)
    json_data = df_rows_to_dict(test_df, 'Test', json_data)
    
    # Save the JSON data to a file
    with open(os.path.join(args.save_path, f"{args.domain_name}_subactivity{subactivity}_data.json"), 'w') as fp:
        json.dump(json_data, fp, indent=4)
            

print("Done!")

# Run this script with the following command:
# python indomain_generalization_split_generator.py -domain_name Origami -annotation_path /media/alexa/WORKSPACE/Shijia-stage-two/new_struggle_dataset/annotations/ -annotation_file origami_tsa_full.csv -save_path /media/alexa/WORKSPACE/Shijia-stage-two/new_struggle_dataset/splits/indomain_generalization/
# python indomain_generalization_split_generator.py -domain_name Shuffle_Cards -annotation_path /media/alexa/WORKSPACE/Shijia-stage-two/new_struggle_dataset/annotations/ -annotation_file shufflecards_tsa_full.csv -save_path /media/alexa/WORKSPACE/Shijia-stage-two/new_struggle_dataset/splits/indomain_generalization/
# python indomain_generalization_split_generator.py -domain_name Tangram -annotation_path /media/alexa/WORKSPACE/Shijia-stage-two/new_struggle_dataset/annotations/ -annotation_file tangram_tsa_full.csv -save_path /media/alexa/WORKSPACE/Shijia-stage-two/new_struggle_dataset/splits/indomain_generalization/
# python indomain_generalization_split_generator.py -domain_name Tying_Knots -annotation_path /media/alexa/WORKSPACE/Shijia-stage-two/new_struggle_dataset/annotations/ -annotation_file tyingknots_tsa_full.csv -save_path /media/alexa/WORKSPACE/Shijia-stage-two/new_struggle_dataset/splits/indomain_generalization/

    
