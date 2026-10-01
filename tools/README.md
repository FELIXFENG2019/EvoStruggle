# Tools

Scripts used to build the data splits and extract video features. All paths default to locations inside this repository, so the scripts can be run from any directory.

Install the dependencies with:

```bash
pip install -r tools/requirements.txt
```

## Data Splits

The split files in [`splits/`](../splits) are the **official splits** used in the paper. Always use them for training and evaluation so that results stay comparable and reproducible.

These scripts are only needed to inspect how the splits were built or to create new splits. To avoid overwriting the official splits, they **read** from `annotations/` and `splits/` but **write** to `regenerated_splits/` by default (git-ignored).

> **Note:** The participant-level train/validation split in `indomain_generalization_split_generator.py` depends on the pandas/scikit-learn versions, so re-running it with recent library versions does not reproduce the released files exactly. Do not replace the files in `splits/` with regenerated ones.

| Script | Output (under `regenerated_splits/`) | Example |
|--------|--------|---------|
| `indomain_generalization_split_generator.py` | `indomain_generalization/<Activity>/` (CSVs + `<Activity>_subactivity<XX>_data.json`) | `python tools/indomain_generalization_split_generator.py -domain_name Origami -annotation_file origami_tsa_full.csv` |
| `crossdomain_generalization_split_generator.py` | `<Activity>_crossdomain.json` | `python tools/crossdomain_generalization_split_generator.py -domain_name Origami` |
| `crossdomain_generalization_split_generator2.py` | `<Activity>_crossdomain_testonvalonly.json` | `python tools/crossdomain_generalization_split_generator2.py -domain_name Origami` |
| `separate_attempts_split_generator.py` | `<Activity>_sepattempt.json` | `python tools/separate_attempts_split_generator.py -domain_name Origami` |
| `separate_attempts_split_generator2.py` | `<Activity>_allattempts_sample<XX>.json` | `python tools/separate_attempts_split_generator2.py -domain_name Origami -seed 42 -suffix allattempts_sample01` |

`-domain_name` is one of `Origami`, `Shuffle_Cards`, `Tangram`, `Tying_Knots`.

The cross-domain and separate-attempts scripts read the train/validation CSV files of the official splits in `splits/`.

## Video Features

`video_feature_extractor.py` extracts SlowFast-R50 features from the 360p videos (see [`extracted_features/README.md`](../extracted_features/README.md)):

```bash
python tools/video_feature_extractor.py --task Origami
```

It additionally requires [PyTorch](https://pytorch.org/), torchvision and [PyTorchVideo](https://github.com/facebookresearch/pytorchvideo).

## Other

`video_mover.py` was used internally to copy the raw recordings into the `data/<resolution>/<Activity>/` layout and is not needed when using the released videos.
