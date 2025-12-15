# EvoStruggle Dataset

Data of video recordings of manual activities of various people performing manual tasks from a first-person perspective. Activities include origami, card shuffling, tangrams and knot tying.

Please see the paper ["EvoStruggle: A Dataset Capturing the Evolution of Struggle across Activities and Skill Levels"](https://arxiv.org/abs/2510.01362) for more details. The [EvoStruggle Dataset Promo Video](https://youtu.be/UmTwZx0y9ZE) is available on YouTube.

## Introduction of the Struggle Determination

https://github.com/user-attachments/assets/496fe073-8add-42cf-927a-d82a4ea2a522

### Our Definition of Struggle
> *“To struggle, as defined in the dictionary (verb), is to experience difficulty and make a great effort in order to do something.”*

In this work, **struggle** is defined as *observable difficulty* in completing a given activity. It may be characterized by one or more of the following indicators:

* Motor hesitation of the hands  
* Repeated attempts  
* Prolonged actions  
* Body-gesture signs of frustration (e.g., hand and/or head movements)  
* Disruptive errors and pauses  

Struggle examples in each of the activities:
| **1. Tying Knots** | **2. Origami** |
| :---: | :---: |
| <video src="https://github.com/user-attachments/assets/45ad35ae-1eaf-40b5-851d-b1a659e36e6f" controls="controls" width="100%"></video> | <video src="https://github.com/user-attachments/assets/ab9296ce-8c4b-4f58-b65e-076345f61356" controls="controls" width="100%"></video> |
| **3. Tangram** | **4. Shuffle Cards** |
| <video src="https://github.com/user-attachments/assets/d224f251-d2ad-4aa1-8b8f-65e785303c2f" controls="controls" width="100%"></video> | <video src="https://github.com/user-attachments/assets/a3e7c8dc-0b22-46b6-97ce-4a641c352f31" controls="controls" width="100%"></video> |

## What's new in this dataset?
* Over 60 hours video recordings, 2,793 videos, and 5,385 annotated temporal struggle segments from 76 participants.

* Evolution of Skill: Five Attempts/Repetitions Each Task. 

https://github.com/user-attachments/assets/ec7015c6-c63b-4e6a-bf4f-26f47e16a39d

* Diversity: 18 Tasks Grouped into Four activities--Tying Knots, Origami, Tangram Puzzles, and Shuffling Cards.

| **1. Tasks in Tying Knots** | **2. Tasks in Origami** |
| :---: | :---: |
| <video src="https://github.com/user-attachments/assets/a2300d5e-9d23-44a2-8fe7-9b82aedeaae2" controls="controls" width="100%"></video> | <video src="https://github.com/user-attachments/assets/af012349-3ad4-4890-a3ce-6e51ce2702bd" controls="controls" width="100%"></video> |
| **3. Tasks in Tangram** | **4. Tasks in Shuffle Cards** |
| <video src="https://github.com/user-attachments/assets/2b02566a-110a-4693-97c7-7620f4608285" controls="controls" width="100%"></video> | <video src="https://github.com/user-attachments/assets/69fb4fab-9ca1-4289-8093-93b485cf53ae" controls="controls" width="100%"></video> |

## Usage of the Data

In this section, we describe how our struggle determination dataset is organised and how the data is saved in each file. Here is an overview of the dataset structure:
```
.
└── Struggle-Dataset/
    ├── annotation/
    │   ├── pipe.csv
    │   ├── tent.csv
    │   ├── tent_subactions/
    │   │   ├── tent_0_ass_sup.csv
    │   │   ├── tent_1_ins_sta.csv
    │   │   ├── tent_2_ins_sup.csv
    │   │   ├── tent_3_ins_tab.csv
    │   │   └── tent_9_pla_guy.csv
    │   └── tower.csv
    ├── Pipes-Struggle/
    │   └── <Pipes_VideoIDs>.MP4 e.g. 01_00_0001.MP4
    ├── Tent-Struggle/
    │   └── <Tent_VideoIDs>.MP4 e.g. 08_02_00.MP4
    ├── Tower-Struggle/
    │   └── <Tower_VideoIDs>.MP4 e.g. 01_00_0000.MP4
    ├── extracted_frames/
    │   ├── Pipes-Struggle/
    │   │   └── <Pipes_VideoIDs>/
    │   │       ├── img_000.jpg
    │   │       ├── img_001.jpg
    │   │       └── ...
    │   ├── Tent-Struggle/
    │   │   └── <Tent_VideoIDs>/
    │   │       ├── img_000.jpg
    │   │       ├── img_001.jpg
    │   │       └── ...
    │   └── Tower-Struggle/
    │       └── <Tower_VideoIDs>/
    │           ├── img_000.jpg
    │           ├── img_001.jpg
    │           └── ...
    ├── splits/
    │   ├── Pipes-Struggle/
    │   │   ├── test_<num_splits>.txt
    │   │   └── train_<num_splits>.txt
    │   ├── Tent-Struggle/
    │   │   ├── test_<num_splits>.txt
    │   │   └── train_<num_splits>.txt
    │   └── Tower-Struggle/
    │       ├── test_<num_splits>.txt
    │       └── train_<num_splits>.txt
    ├── tools/
    │   ├── build_frames.py
    │   ├── stratifiedgroupkfold.py
    │   └── human_baseline_stats.py
    └── README.md
```

### Folder Structure
- Annotation:
  This folder contains annotations of the struggle determination dataset. There are three annotation files that correspond to the tasks plumbing pipes, pitching tent, and tower of Hanoi game by the names of pipes.csv, tent.csv, and tower.csv respectively. There is a folder called 'tent_subactions' which contains the annotations files by sub-actions of pitching tent task named as following:
  - tent_0_ass_sup.csv
  - tent_1_ins_sta.csv
  - tent_2_ins_sup.csv
  - tent_3_ins_sup.csv
  - tent_9_ins_sup.csv
  
  See more details of sub-actions for the tent pitching task in the 'Action-annotation' dictionary below.

  Description of each column in the file:
  - VideoID: This represents the video ID for each individual video in an activity (e.g., VideoID.MP4). VideoID is defined as ParticipantID_RecordID_10SecondClipID.
  - Vote#: This represents a crowd's vote collected by the Amazon Mechanical Turk service.
  There are 20 votes for the same video clip (except Tower-Struggle: 15). The scale of vote is from 1 to 4. (1: definitely non-struggle, 2: slightly non-struggle, 3: slightly struggle, 4: definitely struggle)
  - StdDev: This represents the standard deviation of the crowd's multiple votes.
  - Mode: This represents the mode statistics (the most frequently selected option) out of - crowd's multiple votes. 
  - GA: Golden Annotation (GA) is a single vote chosen by an expert on the same video.

- Tent-Struggle:
  This folder contains a set of 10-second video segments collected from tent pitching task
  (equivalent to the 'EPIC-Tent' dataset: https://github.com/youngkyoonjang/EPIC_Tent2019).
  The subfolders correspond to the Action_annotaion dictionary as follows:
  ```
  Action_annotation = {0:'assemble support', 1:'insert stake', 2:'insert support', 3:'insert support tab', 4:'instruction', 5:'pickup/open stakebag', 6:'pickup/open supportbag', 7:'pickup/open tentbag', 8:'pickup/place ventcover', 9:'place guyline', 10:'spread tent', 11:'tie top'} 
  ```
  The annotations of Tent-Struggle only contain actions 0, 1, 2, 3, 9 in the EPIC-Tent dataset.
- Pipes-Struggle:
  This folder contains a set of 10-second video segments collected from plumbing pipes task.
- Tower-Struggle:
  This folder contains a set of 10-second video segments collected from tower of Hanoi task.
- Extracted Frames:
  This folder contains extracted frames in JPG format from the video samples from three struggle determination datasets: Pipes-Struggle, Tent-Struggle, and Tower-Struggle. 
- Splits:
  This folder contains the four-fold training and testing splits for cross-validation.
- Tools:
  - build_frames.py is used to extract frames from the video samples.


## Download Links

* **Baidu NetDisk / 百度网盘** 
    * [**EvoStruggle_Dataset**](https://pan.baidu.com/s/1WuCjys0tBzrS3O2OxttfWQ?pwd=wfak) (Full Download Including Original 1080p Video Recordings)
    * [**new_struggle_dataset.tar.gz**](https://pan.baidu.com/s/1b7HKdpTEapa0GiZaNKRrRQ?pwd=g67j) (With 360p Resized Videos)
    * **Size:** 41.81GB (360p resolution), 1.18 TB (Full Download 1080p)

## Contributors

* [Shijia Feng](https://research-information.bris.ac.uk/en/persons/shijia-feng/)
* [Michael Wray](https://mwray.github.io/)
* [Walterio Mayol-Cuevas](http://people.cs.bris.ac.uk/~wmayol/)

## Citation to this work

```
@misc{feng2025evostruggledatasetcapturingevolution,
      title={EvoStruggle: A Dataset Capturing the Evolution of Struggle across Activities and Skill Levels}, 
      author={Shijia Feng and Michael Wray and Walterio Mayol-Cuevas},
      year={2025},
      eprint={2510.01362},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2510.01362}, 
}
```



