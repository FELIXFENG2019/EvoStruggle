# Extracted Features

Video features used for the Struggle Temporal Action Localization experiments can be generated with [`tools/video_feature_extractor.py`](../tools/video_feature_extractor.py).

The script uses a Kinetics-pretrained [SlowFast-R50](https://github.com/facebookresearch/pytorchvideo) backbone with a sliding window of 32 frames and a stride of 16 frames (default settings), and saves one `.npy` file of shape `(num_clips, 2304)` per video:

```
extracted_features/
└── slowfast_features/
    ├── Origami/
    │   ├── 01_01_01.npy
    │   └── ...
    ├── Shuffle_Cards/
    ├── Tangram/
    └── Tying_Knots/
```

Example (after placing the videos as described in [`data/README.md`](../data/README.md)):

```bash
python tools/video_feature_extractor.py --task Origami
```
