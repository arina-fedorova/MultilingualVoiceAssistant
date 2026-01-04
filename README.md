# PolyVoice - Multilingual Voice Assistant

Multilingual Voice Assistant for learning Romance languages (Spanish, Italian, Portuguese). The system conducts 10-15 minute spoken lessons with voice-only interaction, providing feedback on mistakes and pronunciation.

**Companion project to [PolyLadder](https://github.com/arina-fedorova/PolyLadder)** - a web-based parallel language learning platform.

## Features (Planned)

- **Speech-to-Text (ASR)**: Multi-language speech recognition (ES/IT/PT/EN)
- **Text-to-Speech (TTS)**: Natural speech synthesis with prosody control
- **Lesson Orchestrator**: LLM-powered dialog management for structured lessons
- **Pronunciation Scoring**: Custom ML module for quantified pronunciation feedback
- **Language ID**: Detect code-switching between similar languages

## Tech Stack

- **Python 3.11+** with Poetry
- **FastAPI** for API
- **PyTorch** for ML models
- **Whisper** for ASR
- **DVC** for data versioning
- **Docker** for containerization

## Project Structure

```
├── src/polyvoice/      # Main package
│   ├── asr/            # Speech-to-Text
│   ├── tts/            # Text-to-Speech
│   ├── orchestrator/   # LLM dialog manager
│   ├── pronunciation/  # Pronunciation scoring
│   ├── language_id/    # Language identification
│   ├── api/            # FastAPI endpoints
│   └── common/         # Shared utilities
├── notebooks/          # Jupyter notebooks
├── data/               # Data (DVC managed)
├── models/             # Trained models (DVC managed)
├── tests/              # Tests
└── docs/               # Documentation
```

## Development

```bash
# Install dependencies
poetry install

# Run linting
poetry run ruff check .

# Run type checking
poetry run mypy src/

# Run tests
poetry run pytest

# Start Jupyter
poetry run jupyter lab
```

## Status

🚧 **In Development** - Phase 0: Foundation & Infrastructure

See [docs/ROADMAP.md](docs/ROADMAP.md) for development roadmap.

## License

MIT
