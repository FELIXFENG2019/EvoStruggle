# EvoStruggle Dataset

Data of video recordings of manual activities of various people performing manual tasks from a first-person perspective. Activities include origami, card shuffling, tangrams and knot tying.

Please see the paper ["EvoStruggle: A Dataset Capturing the Evolution of Struggle across Activities and Skill Levels"](https://arxiv.org/abs/2510.01362) for more details. The [EvoStruggle Dataset Promo Video](https://youtu.be/UmTwZx0y9ZE) is available on YouTube. 

A related talk was given by Prof Walterio Mayol - [Keynote: From Skill to Struggle at the ICCV 2025 SAUAFG Workshop](https://www.youtube.com/watch?v=4HWLiCvc0LU&t=48s).

## Introduction of the Struggle Determination

<video src="https://github.com/user-attachments/assets/496fe073-8add-42cf-927a-d82a4ea2a522" controls="controls" width="100%"></video>

### Our Definition of Struggle
> *“To struggle, as defined in the dictionary (verb), is to experience difficulty and make a great effort in order to do something.”*

In this work, **struggle** is defined as *observable difficulty* in completing a given activity. It may be characterized by one or more of the following indicators:

* Motor hesitation of the hands  
* Repeated attempts  
* Prolonged actions  
* Body-gesture signs of frustration (e.g., hand and/or head movements)  
* Disruptive errors and pauses  

#### Struggle examples in each of the activities:
| **1. Tying Knots** | **2. Origami** |
| :---: | :---: |
| <video src="https://github.com/user-attachments/assets/45ad35ae-1eaf-40b5-851d-b1a659e36e6f" controls="controls" width="100%"></video> | <video src="https://github.com/user-attachments/assets/ab9296ce-8c4b-4f58-b65e-076345f61356" controls="controls" width="100%"></video> |
| **3. Tangram** | **4. Shuffle Cards** |
| <video src="https://github.com/user-attachments/assets/d224f251-d2ad-4aa1-8b8f-65e785303c2f" controls="controls" width="100%"></video> | <video src="https://github.com/user-attachments/assets/a3e7c8dc-0b22-46b6-97ce-4a641c352f31" controls="controls" width="100%"></video> |

## What's new in this dataset?
* **Over 60 hours video recordings, 2,793 videos, and 5,385 annotated temporal struggle segments from 76 participants.**

* **Evolution of Skill: Five Attempts/Repetitions Each Task.** 

<video src="https://github.com/user-attachments/assets/ec7015c6-c63b-4e6a-bf4f-26f47e16a39d" controls="controls" width="100%"></video>

* **Diversity: 18 Tasks Grouped into Four activities--Tying Knots, Origami, Tangram Puzzles, and Shuffling Cards.**

| **1. Tasks in Tying Knots** | **2. Tasks in Origami** |
| :---: | :---: |
| <video src="https://github.com/user-attachments/assets/a2300d5e-9d23-44a2-8fe7-9b82aedeaae2" controls="controls" width="100%"></video> | <video src="https://github.com/user-attachments/assets/af012349-3ad4-4890-a3ce-6e51ce2702bd" controls="controls" width="100%"></video> |
| **3. Tasks in Tangram** | **4. Tasks in Shuffle Cards** |
| <video src="https://github.com/user-attachments/assets/2b02566a-110a-4693-97c7-7620f4608285" controls="controls" width="100%"></video> | <video src="https://github.com/user-attachments/assets/69fb4fab-9ca1-4289-8093-93b485cf53ae" controls="controls" width="100%"></video> |

### Activities and Tasks

| Activity      | Tasks (Index : Name)                                                                 |
|---------------|---------------------------------------------------------------------------------------|
| Origami       | 01: Paper Plane · 02: Fox · 03: Helmet · 04: Butterfly                                 |
| Shuffle Cards | 01: Hindu Shuffle · 02: Classic Shuffle · 03: Ribbon Spread and Wave · 04: Long Awesome Shuffle · 05: Riffle Shuffle |
| Tangram       | 01: Runner · 02: Kangaroo · 03: Cyclist · 04: Microscope                               |
| Tying Knots   | 01: Ashley Bend · 02: Blakes Hitch · 03: Carrick Bend · 04: Double Fishermans Bend · 05: Slim Beauty Knot |

## Usage of the Data

This section describes the annotation format, video naming convention, and data splits used in the Struggle Temporal Action Localization (Struggle TAL) task.

### 1. Annotations

The annotation files provide metadata for **struggle moments** in each video, including:

- **Start time** of a struggle segment  
- **End time** of a struggle segment  

These timestamps indicate when observable struggle occurs during task execution.

### 2. Video Naming Convention 

Each video follows the naming format: <participant_id><task_index><attempt_id>, where
- `participant_id`: two-digit participant identifier (e.g. `01`)
- `task_index`: two-digit index of the task within the corresponding activity (as listed above)
- `attempt_id`: repetition number of the task, ranging from `01` to `05`

**Example:**  
`01_03_04` denotes *participant 01* performing *task 03* (e.g. Helmet, Ribbon Spread and Wave, Cyclist, or Carrick Bend, depending on the activity) on the *fourth attempt*.

### 3. Code Release

The official code release for the **Struggle Temporal Action Localization** task is available at:

- **GitHub Repository**: [StruggleTAL](https://github.com/FELIXFENG2019/StruggleTAL)

This repository can be used to reproduce the experimental results reported in the paper.

### 4. Data Splits

We provide **three types of data splits** for different training and evaluation settings (see *Figure 6* in the paper for a visual overview).

#### 4.1 Activity-Level Generalization (Cross-Domain)

**Directory**:
splits/crossdomain_generalization

**Description**:  
These splits are used for **Activity-Level Generalization** experiments across the four activities.

**Files**:
- `<activity_name>_crossdomain.json`
- `<activity_name>_crossdomain_testonvalonly.json` *(recommended)*

**Notes**:
- JSON files are used to run the experiments  
- CSV files provide lists of video metadata  
- The `*_testonvalonly.json` file contains **only test samples from the validation split** of the unseen activity

#### 4.2 Task-Level Generalization (In-Domain)

**Directory**:
splits/indomain_generalization

**Description**:  
These splits support **Task-Level Generalization** experiments within each activity.

**Files**:
\<activity_name\>_subactivity<task_index>_data.json.
Use these files to load the corresponding training and testing data.

#### 4.3 Within-Activity and Separate-Attempts Evaluation

**Directory**:
splits/separate_attempts

**Description**:
- **Within-Activity Evaluation**:  
  Provides baseline Struggle TAL performance within the same activity (vanilla setting).
- **Separate Attempts Evaluation**:  
  Investigates the effect of multiple attempts on Struggle TAL performance.

**File**:
\<activity_name\>_sepattempt.json.
Use this file to run both evaluation settings.

<!--
- Directory `splits/crossdomain_generalization` consists of the data splits for the **Activity-Level Generalization** experiments that correspond to the four activities. For running the experiments, the JSON files should be used while the CSV files are the lists of the video metadata. There are two JSON files: "<activity_name>_crossdomain.json" and "<activity_name>_crossdomain_testonvalonly.json", where the later one is recommended to used which only contains the test data that only belongs to the validation splits from the unseen activity. 

- Directory `splits/indomain_generalization` consists of the data splits for the **Task-Level Generalization** experiments corresponding to the four activities. Please use the files with the name in format "<activity_name>_subactivity<task_index>_data.json" to load the training and testing data for the experiments. 

- Directory `splits/separate_attempts` consists of the data splits for both the **Within-Activity Evaluation** and the **Seperate Attempts** experiments where the former provides a baseline results of Struggle TAL within the same activity (vanilla setting) and the later is for investigating the effect of multiple attempts on the Struggle TAL task. Use "<activity_name>_sepattempt.json" for running the experiments. 
-->

## How to Download

### Option 1: Hugging Face Dataset (Recommended)

**[Hugging Face Dataset](https://huggingface.co/datasets/Shijia2025/EvoStruggle)** - Contains 360p resized videos

Please refer to [Downloading Datasets](https://huggingface.co/docs/hub/en/datasets-downloading) documents on Hugging Face to find the suitable command to download the dataset. 

---

### Option 2: Baidu NetDisk / 百度网盘

Choose between the full 1080p version or the compressed 360p version:

- **[EvoStruggle_Dataset](https://pan.baidu.com/s/1WuCjys0tBzrS3O2OxttfWQ?pwd=wfak)** - Full download with original 1080p video recordings (1.18 TB)
- **[new_struggle_dataset.tar.gz](https://pan.baidu.com/s/1b7HKdpTEapa0GiZaNKRrRQ?pwd=g67j)** - Compressed version with 360p resized videos (41.81 GB)

**Note:** The Baidu NetDisk option provides higher resolution videos compared to the Hugging Face version.


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
