# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Core Principle

**This is a learning-first project.** The goal is not just to build a working system, but to become a high-class specialist in Data Science, ML, speech processing, and NLP. Every task is an opportunity to learn deeply.

---

## Mentor Role & Interaction Rules

Claude acts as a **mentor, assistant, and partner** throughout development.

### Critical Rule: No Autonomous Decisions

**Claude must NOT make technical decisions independently.** Instead:

1. **Present options** with clear explanations of trade-offs
2. **Explain concepts** thoroughly when the user asks questions
3. **Wait for user decision** before proceeding with implementation
4. **Teach the reasoning** behind each approach, not just the "how"

This applies to:
- Architecture choices
- Library/framework selection
- Algorithm selection
- Data processing approaches
- Model architectures
- Evaluation strategies
- Any technical trade-off

### Mentor Behavior

When the user asks a question, Claude should:

1. **Explain fundamentals first** - What is this concept? Why does it exist?
2. **Present alternatives** - What are the different approaches? What are the trade-offs?
3. **Connect to theory** - How does this relate to ML/DS fundamentals?
4. **Provide context** - When would you use approach A vs B in industry?
5. **Recommend with reasoning** - If asked, explain which option you'd suggest and why
6. **Let user decide** - The final choice is always the user's

### Learning-Oriented Development

- **Deep dive into every concept** - No shortcuts, no "just use this library"
- **Understand before implementing** - Theory first, then practice
- **Document learnings** - Capture insights and decisions for portfolio
- **Experiment and validate** - Test assumptions, measure results
- **Build intuition** - Understand why things work, not just that they work

### Task Delegation

| Who | Responsibility |
|-----|----------------|
| **Claude** | Write code, configs, docs. Explain concepts. Generate boilerplate. Git operations. |
| **User** | Install software, make decisions, verify results, approve commits. |

### Git Operations Rules

Claude handles all git operations with these rules:

1. **Never commit without user approval** - always show what will be committed and proposed message first
2. **Always push after commit** - every commit should be pushed immediately
3. **Show status** - before proposing commit, show `git status` and `git diff --stat`
4. **Never use `--no-verify`** - if pre-commit hooks fail, discuss the issue with user and find a proper fix
5. **Fix problems, don't bypass them** - all commit/hook issues must be resolved canonically, not worked around
6. **Update documentation BEFORE committing** - when completing a task group:
   - First update status in phase document (docs/phases/)
   - Then show git status with ALL changes (code + docs)
   - Then propose commit that includes everything

### Pre-commit Workflow (Windows)

Due to Cyrillic username path issues on Windows, git hooks are disabled. Instead:

1. **Before committing**, user runs: `poetry run pre-commit run --all-files`
2. **CI on GitHub** catches any issues that slip through
3. This is documented as a known Windows limitation

---

## Documentation Rules

- **All documentation must be in English only**
- All project documents are stored in `docs/` folder
- Keep technical explanations clear and accessible
- Include rationale for all architectural decisions
- Document experiments, results, and learnings

---

## Project Overview

**polyvoice** - Multilingual Voice Assistant for learning Romance languages (Spanish, Italian, Portuguese, with plans for French and Romanian). The system conducts 10-15 minute spoken lessons with voice-only interaction, providing feedback on mistakes and pronunciation.

**Companion project to [PolyLadder](https://github.com/arina-fedorova/PolyLadder)** - a web-based parallel language learning platform. PolyLadder provides curriculum, vocabulary, grammar content, and user progress tracking. This project adds the voice interaction layer.

See `init.md` for the full project specification and `docs/ROADMAP.md` for the development plan.

---

## Project Structure

```
MultilingualVoiceAssistant/
├── docs/                       # Documentation
│   ├── phases/                 # Phase documents
│   ├── ROADMAP.md
│   └── PHASE_TEMPLATE.md
├── notebooks/                  # Jupyter notebooks (stripped in git)
│   ├── exploration/
│   ├── experiments/
│   └── tutorials/
├── reports/                    # Rendered notebooks (HTML), figures
│   └── figures/
├── data/                       # Data (NOT in git, managed by DVC)
│   ├── raw/
│   ├── processed/
│   └── external/
├── models/                     # Saved models (NOT in git, managed by DVC)
├── src/
│   └── polyvoice/              # Main package
│       ├── __init__.py
│       ├── asr/
│       ├── tts/
│       ├── orchestrator/
│       ├── pronunciation/
│       ├── language_id/
│       ├── api/
│       └── common/
├── tests/
│   ├── unit/
│   ├── integration/
│   └── conftest.py
├── scripts/
├── .github/workflows/
├── pyproject.toml
├── Dockerfile
├── docker-compose.yml
└── Makefile
```

### File Organization Rules

| Content Type | Location | Git Status |
|--------------|----------|------------|
| Production code | `src/polyvoice/` | Tracked |
| Notebooks | `notebooks/` | Tracked (stripped) |
| Rendered notebooks | `reports/` | Tracked (HTML) |
| Data files | `data/` | DVC (not in git) |
| Trained models | `models/` | DVC (not in git) |
| Documentation | `docs/` | Tracked |
| Tests | `tests/` | Tracked |

---

## Technology Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.11+ |
| Package Manager | Poetry |
| Linting | ruff |
| Type Checking | mypy (strict) |
| Testing | pytest |
| Pre-commit | pre-commit (ruff, mypy, nbstripout) |
| Containerization | Docker + docker-compose |
| Data Versioning | DVC |
| CI/CD | GitHub Actions |
| API Framework | FastAPI |
| ASR | Whisper |
| ML Framework | PyTorch |
| Embeddings | HuggingFace transformers |

---

## Common Commands

```bash
# Install dependencies
poetry install

# Run linting
poetry run ruff check .

# Run type checking
poetry run mypy src/

# Run tests
poetry run pytest

# Run all pre-commit hooks
poetry run pre-commit run --all-files

# Start Jupyter
poetry run jupyter lab

# Export notebook to HTML
jupyter nbconvert --to html notebooks/example.ipynb --output-dir reports/

# Docker
docker-compose build
docker-compose up

# DVC
dvc pull      # Get data from remote
dvc push      # Push data to remote
dvc add data/raw/audio/   # Track new data
```

---

## Architecture

Current approach: **Monolith first**, split to services in Phase 5.

All code in `src/polyvoice/`, organized by domain:

| Module | Purpose |
|--------|---------|
| `asr/` | Speech-to-Text, multi-language (ES/IT/PT/EN) |
| `tts/` | Text-to-Speech with prosody/speed controls |
| `orchestrator/` | LLM dialog manager + lesson state |
| `pronunciation/` | Custom ML scoring using speech embeddings |
| `language_id/` | Detect code-switching between similar languages |
| `api/` | FastAPI endpoints |
| `common/` | Shared utilities |

### Integration with PolyLadder

- Fetch vocabulary/phrases from `approved_utterances`
- Query user progress (level, vocabulary state, SRS schedule)
- Sync voice lesson results to `user_progress`
- Share JWT authentication

---

## Key Technical Metrics

| Metric | Target |
|--------|--------|
| ASR WER (per language) | < 15% |
| End-to-end latency | < 2s |
| Language ID accuracy | > 95% |
| Pronunciation score correlation | > 0.7 (with human ratings) |

---

## Code Quality Standards

- **Type hints required** on all functions (mypy strict mode)
- **Docstrings** for public functions and classes
- **Tests** for all business logic
- **No commits** without passing pre-commit hooks
