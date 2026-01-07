# MultilingualVoiceAssistant

Voice assistant for learning Romance languages.

## About

The system conducts 10-15 minute conversational lessons in Spanish, Italian, and Portuguese. User speaks, assistant recognizes speech, evaluates pronunciation, provides feedback, and continues the dialog. Voice-only interaction, no text input.

Companion project to [PolyLadder](https://github.com/arina-fedorova/PolyLadder) — a web platform for parallel language learning.

## Components

- **ASR** — multilingual speech recognition (Whisper)
- **TTS** — speech synthesis with prosody control
- **Orchestrator** — LLM for dialog management and lesson structure
- **Pronunciation Scoring** — ML module for pronunciation evaluation
- **Language ID** — language detection during code-switching

## Technology

Python 3.11+, Poetry, FastAPI, PyTorch. Data versioning via DVC.

## Development

```bash
poetry install
poetry run ruff check .
poetry run mypy src/
poetry run pytest
```

## Status

In development. Phase 0 (infrastructure) complete.

## Documentation

Documentation in [PolyLadderCommon/docs/voice-assistant](../PolyLadderCommon/docs/voice-assistant/):
- [PROJECT_SPECIFICATION.md](../PolyLadderCommon/docs/voice-assistant/PROJECT_SPECIFICATION.md) — specification
- [ROADMAP.md](../PolyLadderCommon/docs/voice-assistant/ROADMAP.md) — 6-phase plan
