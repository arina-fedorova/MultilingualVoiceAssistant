# Data Directory

This folder contains data that is **NOT stored in git**. Data is managed by DVC.

## Structure

```
data/
├── raw/            # Original, unmodified data
├── processed/      # Preprocessed data ready for training
└── external/       # Third-party datasets
```

## How to Get Data

### If DVC remote is configured:

```bash
# Pull all data from remote storage
dvc pull
```

### Manual setup:

1. Download required datasets (see below)
2. Place audio files in appropriate `raw/` subdirectories
3. Run preprocessing: `python scripts/preprocess_data.py`

## Datasets

*To be documented as we add datasets*

| Dataset | Language | Type | Location |
|---------|----------|------|----------|
| TBD | ES/IT/PT | Audio | `raw/` |

## Data Organization Convention

```
raw/{language}/{dataset_name}/
├── audio/          # Audio files
├── transcripts/    # Text transcriptions
└── metadata.csv    # File metadata
```

Metadata columns:
- `utterance_id` - Unique identifier
- `speaker_id` - Speaker identifier
- `language` - Language code (es/it/pt/en)
- `text` - Transcription
- `duration` - Audio duration in seconds
- `split` - train/val/test
