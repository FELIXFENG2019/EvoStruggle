import os
import csv
import json
import argparse
import pandas as pd


parser = argparse.ArgumentParser(description='Codes for splitting the train/validation/test data for cross-domain generalization')
parser.add_argument('-domain_name', '-dname', type=str, default="Origami", choices=['Origami', 'Shuffle_Cards', 'Tangram', 'Tying_Knots'])
parser.add_argument('-split_path', '-spath', type=str, default="/media/alexa/WORKSPACE/Shijia-stage-two/new_struggle_dataset/splits/crossdomain_generalization")
parser.add_argument('-save_path', '-save', type=str, default="/media/alexa/WORKSPACE/Shijia-stage-two/new_struggle_dataset/splits/crossdomain_generalization/")
args = parser.parse_args()


def df_rows_to_dict(df, sebset, activity, json_data):
    for index, row in df.iterrows():
        # Extract values from the row
        # print(activity, row['video_name'])
        video_name = activity + '-' + row['video_name']
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
root_path = args.split_path
args.save_path = os.path.join(args.save_path, args.domain_name)
if not os.path.exists(args.save_path):
    os.makedirs(args.save_path)
domains_list = ['Origami', 'Shuffle_Cards', 'Tangram', 'Tying_Knots']
json_data = {
    "version": "crossdomain_generalization",
    "database": {}
}
for domain_name in domains_list:
    if domain_name == args.domain_name:
        # This domain as held-out test set
        files_ls = os.listdir(os.path.join(root_path, domain_name))
        csv_list = []
        for file in files_ls:
            if file.split('.')[1] == 'csv':
                csv_list.append(file)
        num_sub_activities = len(csv_list) - 2 # except for the train/val csv
        # In the held-out test domain, we only load the unseentest csv as the test set and store in json
        for i in range(num_sub_activities):
            csv_file_name = domain_name + '_' + "subactivity{:02d}".format(i+1) + '_' + 'unseentest.csv'
            df = pd.read_csv(os.path.join(root_path, domain_name, csv_file_name))
            json_data = df_rows_to_dict(df, 'test_subactivity{:02d}'.format(i+1), domain_name, json_data)
    else:
        # the other domains should be combined and used as trian/validation set
        csv_file_name = domain_name + '_' + 'train.csv'
        df = pd.read_csv(os.path.join(root_path, domain_name, csv_file_name))
        json_data = df_rows_to_dict(df, 'train', domain_name, json_data)

        csv_file_name = domain_name + '_' + 'val.csv'
        df = pd.read_csv(os.path.join(root_path, domain_name, csv_file_name))
        json_data = df_rows_to_dict(df, 'validation', domain_name, json_data)
    # import pdb;pdb.set_trace()

# Save the JSON data to a file
with open(os.path.join(args.save_path, f"{args.domain_name}_crossdomain.json"), 'w') as fp:
    json.dump(json_data, fp, indent=4)   

print("Done!")

# Run this script with the following command:
# python crossdomain_generalization_split_generator.py -domain_name Origami 
# python crossdomain_generalization_split_generator.py -domain_name Shuffle_Cards 
# python crossdomain_generalization_split_generator.py -domain_name Tangram 
# python crossdomain_generalization_split_generator.py -domain_name Tying_Knots 
    

