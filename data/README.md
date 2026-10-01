# Video Data

The videos are not stored in this repository. Download them from one of the sources listed in [How to Download](../README.md#how-to-download):

| Source | Resolution | Link |
|--------|-----------|------|
| Hugging Face (recommended) | 360p | [Shijia2025/EvoStruggle](https://huggingface.co/datasets/Shijia2025/EvoStruggle) |
| Baidu NetDisk / 百度网盘 | 360p (41.81 GB) | [new_struggle_dataset.tar.gz](https://pan.baidu.com/s/1b7HKdpTEapa0GiZaNKRrRQ?pwd=g67j) |
| Baidu NetDisk / 百度网盘 | 1080p (1.18 TB) | [EvoStruggle_Dataset](https://pan.baidu.com/s/1WuCjys0tBzrS3O2OxttfWQ?pwd=wfak) |

## Expected Layout

The feature extraction script [`tools/video_feature_extractor.py`](../tools/video_feature_extractor.py) expects the videos in this directory, organised by resolution and activity, and named after the `video_name` column of the annotation files:

```
data/
└── 360p/
    ├── Origami/
    │   ├── 01_01_01.mp4
    │   └── ...
    ├── Shuffle_Cards/
    ├── Tangram/
    └── Tying_Knots/
```
