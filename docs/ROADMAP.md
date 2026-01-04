# MultilingualVoiceAssistant Roadmap

This document outlines the development roadmap for the Multilingual Voice Assistant project, a companion to [PolyLadder](https://github.com/arina-fedorova/PolyLadder) that adds voice-based learning capabilities.

---

## Project Context

**Relationship to PolyLadder**: PolyLadder provides the curriculum, vocabulary, grammar content, and user progress tracking. This project adds the voice interaction layer: speech recognition, speech synthesis, pronunciation scoring, and code-switching detection.

**Portfolio Focus**: This project is designed to demonstrate Data Science and ML skills in a production context, including:
- Speech AI (ASR, TTS, pronunciation modeling)
- NLP/LLM orchestration for dialog management
- Custom ML model development and evaluation
- MLOps practices (pipelines, monitoring, experimentation)

---

## Phase 0: Foundation & Infrastructure

### 0.1 Project Setup
- [ ] Initialize Python project structure (poetry/uv for dependency management)
- [ ] Set up pre-commit hooks (ruff, mypy, black)
- [ ] Configure pytest for testing
- [ ] Create Docker development environment
- [ ] Set up CI/CD pipeline (GitHub Actions)

### 0.2 Development Environment
- [ ] Configure environment variables management (.env, secrets)
- [ ] Set up logging infrastructure (structured logging)
- [ ] Create Makefile/justfile for common commands
- [ ] Document local development setup

**Learning Goals**:
- Python project best practices
- Development tooling and automation
- Docker fundamentals

---

## Phase 1: MVP - Voice Lesson with Off-the-Shelf Models

### 1.1 ASR Service
- [ ] Research and select ASR provider/model (Whisper, cloud APIs)
- [ ] Implement ASR service wrapper with language detection
- [ ] Add support for ES/IT/PT/EN
- [ ] Create audio recording/streaming interface
- [ ] Benchmark WER per language on test samples
- [ ] Document ASR limitations and edge cases

### 1.2 TTS Service
- [ ] Research and select TTS provider/model (cloud APIs, Coqui, etc.)
- [ ] Implement TTS service wrapper with multi-language support
- [ ] Add prosody controls (speed, pitch)
- [ ] Create voice profiles (teacher vs casual)
- [ ] Evaluate naturalness and intelligibility

### 1.3 LLM Lesson Orchestrator
- [ ] Design lesson state machine (greeting → exercises → feedback → closing)
- [ ] Define scenario templates (cafe, hotel, introductions, etc.)
- [ ] Implement LLM integration with system prompts
- [ ] Create lesson state persistence (level, scenario, step)
- [ ] Build context management for dialog history
- [ ] Add basic error correction feedback

### 1.4 Integration & Basic UI
- [ ] Create simple CLI interface for testing
- [ ] Build basic web interface for voice interaction
- [ ] Integrate ASR → Orchestrator → TTS pipeline
- [ ] Add session logging (user_id, timestamps, transcripts)
- [ ] End-to-end testing of full conversation flow

**Learning Goals**:
- Working with speech APIs and models
- LLM prompt engineering for dialog systems
- State machine design
- System integration patterns

**Deliverables**:
- Working voice tutor for basic conversations
- Latency measurements (end-of-speech to response)
- WER baseline per language

---

## Phase 2: Pronunciation Scoring Module (Custom ML)

### 2.1 Data Preparation
- [ ] Collect native speaker reference recordings per target phrase
- [ ] Define vocabulary of practice phrases (high-frequency, difficult phonemes)
- [ ] Create data loading and preprocessing pipeline
- [ ] Standardize audio format (sample rate, channels, normalization)
- [ ] Build train/val/test splits

### 2.2 Feature Extraction
- [ ] Research speech embedding models (wav2vec2, HuBERT, x-vectors)
- [ ] Implement embedding extraction pipeline
- [ ] Compute reference embeddings for native examples
- [ ] Analyze embedding space (visualize with t-SNE/UMAP)

### 2.3 Scoring Model
- [ ] Implement distance-based scoring (cosine similarity)
- [ ] Collect small human-rated sample set for calibration
- [ ] Train calibration model (distance → 0-100 score)
- [ ] Evaluate correlation with human ratings
- [ ] Add word/phoneme-level scoring (if alignment available)

### 2.4 Integration
- [ ] Add "repeat after me" exercise type to orchestrator
- [ ] Display pronunciation scores in UI
- [ ] Highlight problematic words/syllables
- [ ] Generate actionable feedback (e.g., "lengthen the vowel")

**Learning Goals**:
- Speech representation learning
- Transfer learning with pretrained models
- Custom ML model development and evaluation
- Feature engineering and data pipelines

**Deliverables**:
- Pronunciation scoring module with documented accuracy
- Correlation analysis with human ratings
- Technical report on model architecture and decisions

---

## Phase 3: Language ID & Code-Switching Detection

### 3.1 Language ID Model
- [ ] Collect/prepare training data for ES/IT/PT/EN classification
- [ ] Research approaches (text-based n-grams, audio embeddings, hybrid)
- [ ] Implement and train language classifier
- [ ] Evaluate accuracy on held-out data
- [ ] Analyze confusion matrix (which languages are confused?)

### 3.2 Code-Switching Detection
- [ ] Design segmentation strategy (time-based, sentence-based)
- [ ] Implement per-segment language ID
- [ ] Define code-switching detection logic
- [ ] Create synthetic mixed utterances for testing
- [ ] Evaluate detection accuracy

### 3.3 User Feedback
- [ ] Aggregate code-switching statistics per session
- [ ] Identify typical confusion pairs (ES↔IT, ES↔PT)
- [ ] Display language mixing report after lesson
- [ ] Suggest targeted exercises for confused language pairs

**Learning Goals**:
- Text and audio classification
- Handling multi-class imbalanced data
- Evaluation metrics for classification (precision, recall, F1)
- Building interpretable ML systems

**Deliverables**:
- Language ID model with accuracy benchmarks
- Code-switching detection module
- Analysis of common confusion patterns

---

## Phase 4: PolyLadder Integration

### 4.1 Data Integration
- [ ] Define API contract with PolyLadder backend
- [ ] Fetch vocabulary and phrases from approved_utterances
- [ ] Query user progress (level, vocabulary state, SRS schedule)
- [ ] Sync voice lesson results back to user_progress

### 4.2 Curriculum-Aware Lessons
- [ ] Map voice scenarios to PolyLadder curriculum topics
- [ ] Personalize exercises based on user's weak areas
- [ ] Integrate SRS items into voice practice
- [ ] Align pronunciation exercises with orthography lessons

### 4.3 Shared Authentication
- [ ] Implement JWT validation from PolyLadder
- [ ] Share user sessions across applications
- [ ] Handle authorization for voice features

**Learning Goals**:
- API design and integration
- Microservices communication patterns
- Authentication/authorization in distributed systems

**Deliverables**:
- Integrated voice assistant with PolyLadder curriculum
- User progress sync across platforms

---

## Phase 5: MLOps & Productionization

### 5.1 Service Architecture
- [ ] Containerize all services (Docker)
- [ ] Create docker-compose for local development
- [ ] Design Kubernetes deployment (optional)
- [ ] Implement health checks and readiness probes

### 5.2 ML Pipelines
- [ ] Set up experiment tracking (MLflow, Weights & Biases)
- [ ] Create training pipelines for pronunciation model
- [ ] Implement model versioning and registry
- [ ] Add automated evaluation on held-out sets

### 5.3 Monitoring & Observability
- [ ] Implement metrics collection (Prometheus)
- [ ] Create dashboards (Grafana)
- [ ] Add alerting for key metrics (WER spike, latency)
- [ ] Log ASR/TTS/scoring results for analysis

### 5.4 Personalization
- [ ] Maintain per-user profiles (level, weaknesses, patterns)
- [ ] Implement adaptive difficulty adjustment
- [ ] Add exercise type selection based on user needs
- [ ] Track and visualize user improvement over time

**Learning Goals**:
- MLOps best practices
- Experiment tracking and reproducibility
- Production monitoring and observability
- A/B testing and experimentation

**Deliverables**:
- Production-ready deployment configuration
- MLOps pipeline with experiment tracking
- Monitoring dashboards

---

## Phase 6: Language Expansion

### 6.1 Add French
- [ ] Extend ASR/TTS services for French
- [ ] Add French to language ID model
- [ ] Create French lesson scenarios
- [ ] Collect French pronunciation references

### 6.2 Add Romanian
- [ ] Extend ASR/TTS services for Romanian
- [ ] Add Romanian to language ID model
- [ ] Create Romanian lesson scenarios
- [ ] Collect Romanian pronunciation references

### 6.3 Scenario Expansion
- [ ] Add travel scenarios (airport, train station)
- [ ] Add work scenarios (meetings, presentations)
- [ ] Add exam preparation mode
- [ ] Add customer service simulations

**Learning Goals**:
- Scaling ML systems to new domains
- Transfer learning across languages
- Content templating and localization

---

## Technical Metrics to Track

| Metric | Target | Measurement |
|--------|--------|-------------|
| ASR WER (per language) | < 15% | Evaluate on test set |
| End-to-end latency | < 2s | From end-of-speech to TTS start |
| Language ID accuracy | > 95% | Per-utterance classification |
| Pronunciation score correlation | > 0.7 | Pearson with human ratings |
| Code-switching detection F1 | > 0.85 | On synthetic + real data |

---

## Product Metrics to Track

| Metric | Description |
|--------|-------------|
| Session completion rate | % of lessons completed vs started |
| Average session length | Time spent in voice lessons |
| Exercises per session | Number of practice items completed |
| User satisfaction | Post-lesson rating (1-5) |
| Return rate | % of users returning within 7 days |

---

## Technology Stack (Recommended)

| Component | Technology | Rationale |
|-----------|------------|-----------|
| Language | Python 3.11+ | ML ecosystem, typing |
| Package Manager | poetry or uv | Modern dependency management |
| API Framework | FastAPI | Async, type hints, OpenAPI |
| ASR | Whisper (OpenAI) | Multi-language, open weights |
| TTS | Coqui TTS or cloud | Open source option available |
| LLM | Claude/GPT API | Dialog management |
| ML Framework | PyTorch | Speech models, training |
| Embeddings | transformers (HuggingFace) | Pretrained speech models |
| Database | PostgreSQL | Shared with PolyLadder |
| Experiment Tracking | MLflow or W&B | Reproducibility |
| Containerization | Docker | Portability |
| CI/CD | GitHub Actions | Automation |

---

## Next Steps

1. Complete Phase 0 (project setup and infrastructure)
2. Start Phase 1.1 (ASR service research and implementation)
3. Create initial benchmarks and baselines
