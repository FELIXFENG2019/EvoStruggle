# EvoStruggle Dataset

[![arXiv](https://img.shields.io/badge/arXiv-2510.01362-b31b1b.svg)](https://arxiv.org/abs/2510.01362)
[![ICPR 2026](https://img.shields.io/badge/ICPR-2026-blue.svg)](#citation)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow.svg)](https://huggingface.co/datasets/Shijia2025/EvoStruggle)
[![Code: StruggleTAL](https://img.shields.io/badge/Code-StruggleTAL-black.svg?logo=github)](https://github.com/FELIXFENG2019/StruggleTAL)
[![Promo Video](https://img.shields.io/badge/YouTube-Promo%20Video-red.svg?logo=youtube)](https://youtu.be/UmTwZx0y9ZE)
[![Dataset License: CC BY-NC 4.0](https://img.shields.io/badge/Data%20License-CC%20BY--NC%204.0-lightgrey.svg)](LICENSE-DATASET.md)
[![Code License: Apache 2.0](https://img.shields.io/badge/Code%20License-Apache%202.0-green.svg)](LICENSE)

Data of video recordings of manual activities of various people performing manual tasks from a first-person perspective. Activities include origami, card shuffling, tangrams and knot tying.

Please see the paper ["EvoStruggle: A Dataset Capturing the Evolution of Struggle across Activities and Skill Levels"](https://arxiv.org/abs/2510.01362) (ICPR 2026) for more details. The [EvoStruggle Dataset Promo Video](https://youtu.be/UmTwZx0y9ZE) is available on YouTube.

A related talk was given by Prof Walterio Mayol - [Keynote: From Skill to Struggle at the ICCV 2025 SAUAFG Workshop](https://www.youtube.com/watch?v=4HWLiCvc0LU&t=48s).

**Contents:**
[Introduction](#introduction-of-the-struggle-determination) ·
[Dataset at a Glance](#whats-new-in-this-dataset) ·
[Download](#how-to-download) ·
[Quick Start](#quick-start) ·
[Usage of the Data](#usage-of-the-data) ·
[Repository Structure](#repository-structure) ·
[Citation](#citation) ·
[License](#license) ·
[Contact](#contact)

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

### Statistics per Activity

Computed from the annotation files in [`annotations/`](annotations). All videos are recorded at 50 fps.

| Activity      | Annotation file                 | Tasks | Videos | Struggle segments | Videos without struggle | Total duration |
|---------------|---------------------------------|:-----:|-------:|------------------:|------------------------:|---------------:|
| Origami       | `origami_tsa_full.csv`          | 4     | 637    | 974               | 197                     | 17.3 h         |
| Shuffle Cards | `shufflecards_tsa_full.csv`     | 5     | 750    | 2,146             | 83                      | 16.5 h         |
| Tangram       | `tangram_tsa_full.csv`          | 4     | 600    | 1,098             | 80                      | 14.4 h         |
| Tying Knots   | `tyingknots_tsa_full.csv`       | 5     | 806    | 1,167             | 137                     | 13.4 h         |
| **Total**     |                                 | **18**| **2,793** | **5,385**      | **497**                 | **61.7 h**     |

## How to Download

The annotations and data splits are included in this repository. The videos are hosted externally:

| Source | Resolution | Size | Link |
|--------|-----------|------|------|
| Hugging Face (recommended) | 360p | – | [Shijia2025/EvoStruggle](https://huggingface.co/datasets/Shijia2025/EvoStruggle) |
| Baidu NetDisk / 百度网盘 | 360p (compressed `.tar.gz`) | 41.81 GB | [new_struggle_dataset.tar.gz](https://pan.baidu.com/s/1b7HKdpTEapa0GiZaNKRrRQ?pwd=g67j) |
| Baidu NetDisk / 百度网盘 | 1080p (original recordings) | 1.18 TB | [EvoStruggle_Dataset](https://pan.baidu.com/s/1WuCjys0tBzrS3O2OxttfWQ?pwd=wfak) |

To download from Hugging Face, e.g. with the [`huggingface_hub`](https://huggingface.co/docs/huggingface_hub) CLI:

```bash
pip install -U huggingface_hub
huggingface-cli download Shijia2025/EvoStruggle --repo-type dataset --local-dir EvoStruggle
```

See [Downloading Datasets](https://huggingface.co/docs/hub/en/datasets-downloading) for other options.

**Note:** The original 1080p recordings are currently only available via Baidu NetDisk.

## Quick Start

Clone this repository to get the annotations and splits:

```bash
git clone https://github.com/FELIXFENG2019/EvoStruggle.git
cd EvoStruggle
```

Load the struggle annotations of one activity (list-valued columns are stored as JSON strings):

```python
import json
import pandas as pd

df = pd.read_csv("annotations/origami_tsa_full.csv")
for col in ["keyframes", "keyframes(frames)", "struggle", "struggle(frames)"]:
    df[col] = df[col].apply(json.loads)

row = df.iloc[0]
print(row["video_name"], row["duration"], row["fps"])  # 01_01_01 83.66 50
print(row["struggle"])  # [[16.184, 21.79392], [45.16892, 59.16892], [69.97771, 75.85271]]
```

Load a benchmark split (ActivityNet-style JSON, directly usable by temporal action localization codebases such as [StruggleTAL](https://github.com/FELIXFENG2019/StruggleTAL)):

```python
import json

with open("splits/separate_attempts/Origami/Origami_sepattempt.json") as f:
    split = json.load(f)

for video_name, info in split["database"].items():
    subset = info["subset"]  # e.g. "train_attempt01", "validation"
    segments = [ann["segment"] for ann in info["annotations"]]  # [[start_sec, end_sec], ...]
```

## Usage of the Data

This section describes the annotation format, video naming convention, and data splits used in the Struggle Temporal Action Localization (Struggle TAL) task.

### 1. Annotations

There is one annotation file per activity in [`annotations/`](annotations). Each row corresponds to one video:

| Column | Description |
|--------|-------------|
| `video_name` | Video identifier, see [Video Naming Convention](#2-video-naming-convention) |
| `duration` | Video duration in seconds |
| `fps` | Frame rate (50 for all videos) |
| `keyframes` | Keyframe timestamps (seconds) marked during annotation; they lie within the struggle segments |
| `keyframes(frames)` | Same keyframes as frame indices |
| `struggle` | Struggle segments as `[[start, end], ...]` in seconds |
| `struggle(frames)` | Same struggle segments as frame indices |

Videos without any observed struggle have empty lists (`[]`). There is a single action class, `Struggle` (see [`annotations/category_idx.txt`](annotations/category_idx.txt)).

### 2. Video Naming Convention

Each video follows the naming format `<participant_id>_<task_index>_<attempt_id>`, where
- `participant_id`: two-digit participant identifier (e.g. `01`)
- `task_index`: two-digit index of the task within the corresponding activity (as listed above)
- `attempt_id`: repetition number of the task, ranging from `01` to `05`

**Example:**
`01_03_04` denotes *participant 01* performing *task 03* (e.g. Helmet, Ribbon Spread and Wave, Cyclist, or Carrick Bend, depending on the activity) on the *fourth attempt*.

Video names are only unique within an activity, so always use them together with the activity name.

### 3. Code Release

The official code release for the **Struggle Temporal Action Localization** task is available at:

- **GitHub Repository**: [StruggleTAL](https://github.com/FELIXFENG2019/StruggleTAL)

This repository can be used to reproduce the experimental results reported in the paper.

### 4. Data Splits

We provide **three types of data splits** for different training and evaluation settings (see *Figure 6* in the paper for a visual overview).

All JSON split files share the same structure:

```json
{
  "version": "...",
  "database": {
    "<video_name>": {
      "subset": "train",
      "duration": 83.66,
      "fps": 50,
      "annotations": [
        {"label": "Struggle", "segment": [16.184, 21.79392], "segment(frames)": [809, 1090], "label_id": 1}
      ]
    }
  }
}
```

The CSV files next to each JSON file list the videos (with their annotations and metadata) in each subset. The JSON files were generated from them with the scripts in [`tools/`](tools).

| Setting | Directory | JSON file | `subset` values | Video key |
|---------|-----------|-----------|-----------------|-----------|
| Activity-level generalization | `splits/crossdomain_generalization/<Activity>/` | `<Activity>_crossdomain_testonvalonly.json` *(recommended)* | `train`, `validation`, `test` | `<Activity>-<video_name>` |
| | | `<Activity>_crossdomain.json` | `train`, `validation`, `test_subactivity<XX>` | `<Activity>-<video_name>` |
| Task-level generalization | `splits/indomain_generalization/<Activity>/` | `<Activity>_subactivity<XX>_data.json` | `Train`, `Validation`, `Test` | `<video_name>` |
| Within-activity / separate attempts | `splits/separate_attempts/<Activity>/` | `<Activity>_sepattempt.json` | `train_attempt01` … `train_attempt05`, `validation` | `<video_name>` |
| | | `<Activity>_allattempts_sample0{1,2,3}.json` | `train`, `validation` | `<video_name>` |

`<Activity>` is one of `Origami`, `Shuffle_Cards`, `Tangram`, `Tying_Knots`.

#### 4.1 Activity-Level Generalization (Cross-Domain)

**Directory**: `splits/crossdomain_generalization`

These splits are used for **Activity-Level Generalization** experiments across the four activities: `<Activity>` is held out as the unseen test activity, and the train/validation splits of the other three activities are used for training and validation.

**Files**:
- `<Activity>_crossdomain_testonvalonly.json` *(recommended)*: the test set contains **only the validation split** of the unseen activity
- `<Activity>_crossdomain.json`: the test set contains all videos of the unseen activity, grouped by task (`test_subactivity<XX>`)

#### 4.2 Task-Level Generalization (In-Domain)

**Directory**: `splits/indomain_generalization`

These splits support **Task-Level Generalization** experiments within each activity: task `<XX>` is held out as the unseen test task, and the remaining tasks of the same activity are split by participant into train and validation sets.

**Files**: `<Activity>_subactivity<XX>_data.json`. Use these files to load the corresponding training and testing data.

#### 4.3 Within-Activity and Separate-Attempts Evaluation

**Directory**: `splits/separate_attempts`

- **Within-Activity Evaluation**: Provides baseline Struggle TAL performance within the same activity (vanilla setting).
- **Separate Attempts Evaluation**: Investigates the effect of multiple attempts on Struggle TAL performance. Training videos are grouped by attempt (`train_attempt01` … `train_attempt05`).

**Files**:
- `<Activity>_sepattempt.json`: use this file to run both evaluation settings.
- `<Activity>_allattempts_sample0{1,2,3}.json`: training sets of the same size as a single attempt, sampled evenly from all five attempts with three different random seeds.

## Repository Structure

```
EvoStruggle/
├── annotations/            # Struggle annotations, one CSV per activity
├── splits/
│   ├── crossdomain_generalization/   # Activity-level generalization splits
│   ├── indomain_generalization/      # Task-level generalization splits
│   └── separate_attempts/            # Within-activity / separate-attempts splits
├── tools/                  # Scripts for generating splits and extracting video features
├── data/                   # Place the downloaded videos here (see data/README.md)
├── extracted_features/     # Place extracted video features here (see extracted_features/README.md)
├── LICENSE                 # Apache-2.0 (code)
└── LICENSE-DATASET.md      # CC BY-NC 4.0 (dataset)
```

See [`tools/README.md`](tools/README.md) for how to use the scripts.

## Contributors

* [Shijia Feng](https://research-information.bris.ac.uk/en/persons/shijia-feng/)
* [Michael Wray](https://mwray.github.io/)
* [Walterio Mayol-Cuevas](http://people.cs.bris.ac.uk/~wmayol/)

## Citation

If you use this dataset, please cite our paper:

```bibtex
@inproceedings{feng2026evostruggle,
  title={{EvoStruggle}: A Dataset Capturing the Evolution of Struggle across Activities and Skill Levels},
  author={Feng, Shijia and Wray, Michael and Mayol-Cuevas, Walterio},
  booktitle={International Conference on Pattern Recognition (ICPR)},
  pages={96--111},
  year={2026},
  organization={Springer}
}
```

arXiv version:

```bibtex
@misc{feng2025evostruggledatasetcapturingevolution,
  title={{EvoStruggle}: A Dataset Capturing the Evolution of Struggle across Activities and Skill Levels},
  author={Shijia Feng and Michael Wray and Walterio Mayol-Cuevas},
  year={2025},
  eprint={2510.01362},
  archivePrefix={arXiv},
  primaryClass={cs.CV},
  url={https://arxiv.org/abs/2510.01362}
}
```

## License

The code in this repository is released under the Apache-2.0 License (see [`LICENSE`](LICENSE)).
The EvoStruggle dataset (videos, annotations and splits) is released under CC BY-NC 4.0 (see [`LICENSE-DATASET.md`](LICENSE-DATASET.md)).
If you use this dataset, please cite our paper.

## Contact

For questions, bug reports, or requests, please [open an issue](https://github.com/FELIXFENG2019/EvoStruggle/issues) in this repository.
