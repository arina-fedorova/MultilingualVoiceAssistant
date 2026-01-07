# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

**Full documentation is in [PolyLadderCommon/docs/voice-assistant/](../PolyLadderCommon/docs/voice-assistant/)**

## Quick Reference

### Core Principle
**This is a learning-first project.** Focus on understanding deeply, not just building quickly.

### Critical Rules
1. **No autonomous decisions** - Present options, wait for user decision
2. **Explain fundamentals** - Theory first, then practice
3. **Document learnings** - Capture decisions for portfolio

### Git Operations
1. Never commit without user approval
2. Always push after commit
3. Run checks before committing: `poetry run ruff check . && poetry run mypy src/`
4. Never use `--no-verify`

### Common Commands
```bash
poetry install              # Install dependencies
poetry run ruff check .     # Linting
poetry run mypy src/        # Type checking
poetry run pytest           # Run tests
poetry run pre-commit run --all-files  # All checks
```

### Project Structure
```
src/polyvoice/
├── asr/           # Speech-to-Text
├── tts/           # Text-to-Speech
├── orchestrator/  # LLM dialog manager
├── pronunciation/ # Pronunciation scoring
├── language_id/   # Language identification
├── api/           # FastAPI endpoints
└── common/        # Shared utilities
```

### Documentation
All detailed documentation is in PolyLadderCommon:
- [Project Specification](../PolyLadderCommon/docs/voice-assistant/PROJECT_SPECIFICATION.md)
- [Development Roadmap](../PolyLadderCommon/docs/voice-assistant/ROADMAP.md)
- [Full Claude Guidelines](../PolyLadderCommon/docs/voice-assistant/CLAUDE.md)

### Key Metrics
| Metric | Target |
|--------|--------|
| ASR WER | < 15% |
| Latency | < 2s |
| Language ID | > 95% |
| Pronunciation correlation | > 0.7 |
