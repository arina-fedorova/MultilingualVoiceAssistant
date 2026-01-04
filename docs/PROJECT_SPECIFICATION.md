# Project Plan: Multilingual Voice Assistant for Learning Romance Languages

Goal: Build a production‑oriented DS/ML project that showcases Speech AI, NLP/LLM orchestration, and light MLOps skills. The assistant conducts spoken lessons in Romance languages (initially ES/IT/PT, later more).

---

## 1. Product Definition and Metrics

1. **Core user scenario**
   - A user selects a target language (Spanish / Italian / Portuguese).
   - They interact by voice only (or voice + text), and the assistant runs a 10–15 minute lesson: small talk, controlled exercises, feedback on mistakes and pronunciation.

2. **Target user outcomes**
   - More speaking practice time.
   - Better pronunciation and fewer “language mixups” between similar languages.
   - Feeling of “talking to a human tutor” rather than a static app.

3. **Key metrics**
   - **Technical**
     - Word Error Rate (WER) for ASR per language.
     - Latency from end of user utterance to assistant’s spoken reply.
     - Accuracy of language ID and code‑switching detection.
   - **Product**
     - Average session length and number of completed sessions per user.
     - Lesson completion rate per scenario.
     - User satisfaction (e.g., 1–5 rating after each lesson or periodic NPS).

---

## 2. Data and Base Infrastructure

1. **Datasets to collect**
   - **Wake‑word / short command datasets** for ES/IT/PT/EN:
     - Speech clips with short commands and wake words from multiple speakers.
     - Labels: language, phrase ID, speaker ID, environment/noise metadata.
   - **Conversational / call‑center speech datasets**:
     - Telephone or close‑talk conversations for Spanish, Italian, Brazilian Portuguese, English.
     - Audio + transcripts, possibly speaker turns, intents, emotions.
   - **Text corpora for exercises**:
     - Parallel and monolingual corpora in the same languages (short dialogs, everyday phrases, etc.).

2. **Data organization**
   - Define a clear folder / bucket structure, e.g.:
     - `speech/{language}/{dataset_name}/{raw|processed}/audio`
     - `speech/{language}/{dataset_name}/transcripts`
     - `text/{language}/{corpus_name}`
   - Maintain metadata tables (e.g., in parquet/CSV) with:
     - `utterance_id, speaker_id, language, text, split, scenario, noise_level, source_dataset`.

3. **Infrastructure basics**
   - A small data processing repo:
     - Scripts/notebooks for:
       - Downloading / importing datasets.
       - Standardizing sample rate, channels, file naming, and transcript format.
       - Creating train/val/test splits per task (ASR fine‑tuning, language ID, pronunciation modeling).

---

## 3. MVP: Voice Lesson Using Off‑the‑Shelf Models

MVP goal: a user can speak to the system in a target language, get a spoken answer and simple feedback.

### 3.1. Input: Speech → Text

1. **ASR component**
   - Choose an off‑the‑shelf speech‑to‑text API or open‑source model that supports ES/IT/PT/EN.
   - Implement a service that:
     - Records audio from the client (web or mobile).
     - Sends it to the ASR.
     - Returns the recognized text and, if available, the detected language.

2. **Language ID fallback**
   - If the ASR does not provide language ID:
     - Implement a lightweight language identification module (text‑based or audio‑based) to detect which language the user spoke.
   - Use this both for routing to the correct lesson logic and later for code‑switching analysis.

### 3.2. “Brain” of the Lesson: LLM Orchestrator

1. **LLM configuration**
   - Use a general‑purpose LLM (e.g., GPT‑style) as the dialog manager.
   - System prompt: “You are a language tutor for Romance languages. You run structured spoken lessons, give brief corrections, adapt to user level, and keep the conversation in the target language.”

2. **Lesson state and scenarios**
   - Maintain explicit lesson state in your backend (not just in the LLM context):
     - Level (A1/A2 initially).
     - Current scenario (greetings, ordering in a café, hotel check‑in, etc.).
     - Lesson steps (e.g., Step 1: introductions; Step 2: questions; Step 3: role‑play).
   - When sending a prompt to the LLM:
     - Include:
       - Target language and user level.
       - Scenario + current step.
       - Recent dialog turns.
       - Any feedback from your ML modules (e.g., pronunciation score, language mixing).
   - LLM outputs:
     - Next assistant message (in the target language).
     - Optional teacher note (e.g., brief explanation in user’s native language) if desired.

### 3.3. Output: Text → Speech (TTS)

1. **TTS component**
   - Choose a multi‑language TTS API or open‑source TTS model with:
     - At least one natural voice per target language.
   - Implement a service that:
     - Receives assistant text + language + voice settings.
     - Returns an audio file or streaming audio for playback.

2. **Prosody and speed controls**
   - Allow simple controls:
     - Normal / slower pace.
     - Optionally “teacher” vs “casual” voice profiles.

### 3.4. Simple Feedback and Logging (MVP level)

1. **Basic feedback**
   - Use the LLM to:
     - Highlight obvious grammar / word choice errors.
     - Suggest 1–2 alternative phrasings.
   - Track:
     - How many times the assistant needed to ask for repetition.
     - Whether the user answered in the correct language.

2. **Logging for later analytics**
   - Log per session:
     - User ID (or anonymous ID), language, scenario, timestamps.
     - ASR text, LLM prompts, LLM responses.
     - Basic measures (number of turns, session duration, completion flags).
   - Store logs in a queryable store (e.g., relational DB or analytics warehouse) for future analysis.

> At this point the **MVP ends**: there is already a working multilingual voice tutor with minimal analysis and tracking.

---

## 4. Pronunciation Scoring Module (Custom ML)

Goal: go beyond “chat with voice” and provide quantified feedback on pronunciation.

1. **Data preparation**
   - Use native‑speaker speech from your wake‑word / command datasets and conversational corpora for each target language.
   - Select a vocabulary of target phrases / words for practice (e.g., high‑frequency phrases, difficult phonemes).
   - For each phrase:
     - Collect multiple native examples; optionally normalize transcripts and pronunciations.

2. **Feature extraction**
   - Choose a pretrained speech representation model (e.g., wav2vec‑like, x‑vector, or similar).
   - For each utterance (native or learner):
     - Extract embeddings at utterance level or aligned to words/phonemes.
   - For each target phrase:
     - Compute a reference embedding (e.g., average embedding over multiple native examples).

3. **Scoring model**
   - For a learner utterance:
     - Compute distance between the learner embedding and the reference embedding(s) (e.g., cosine distance).
     - Convert distance to a normalized score (e.g., 0–100) using a simple function or a small regression model trained on a small set of human‑rated samples.
   - Optionally compute scores at:
     - Phrase level.
     - Word or phoneme level (if alignment is available).

4. **Integration into UX**
   - After a “repeat after me” exercise:
     - Display a global pronunciation score.
     - Highlight words / syllables with particularly low scores.
     - Provide short, actionable advice (e.g., “lengthen the final vowel”, “soften the ‘t’ sound”).

---

## 5. Code‑Switching and Language Mixing Detection

Goal: unique feature for parallel learning of similar languages—detect when the user accidentally switches languages.

1. **Data for language ID**
   - Use your speech/text corpora for ES/IT/PT/EN.
   - Optionally augment with synthetic mixed utterances:
     - Combine phrases from different languages in one sentence using text generation, then synthesize with TTS.

2. **Language ID model**
   - Choose approach:
     - Text‑based: character or word n‑grams / embeddings + classifier (logistic regression, transformer, etc.).
     - Audio‑based: short‑segment embeddings + classifier.
   - Train / fine‑tune to:
     - Predict language for short segments (e.g., 1–2 seconds or one sentence).

3. **Code‑switching logic**
   - During each user utterance:
     - Split into segments (time‑based or sentence‑based).
     - Run language ID per segment.
   - If a significant share of segments is predicted as a non‑target language:
     - Flag the utterance as code‑switched.
   - Aggregate statistics for the session:
     - Percentage of off‑language segments.
     - Typical confusion pairs (e.g., ES↔IT, ES↔PT).

4. **User feedback**
   - After the lesson:
     - Show how often the user drifted into another language.
     - Suggest targeted exercises for the most confused language pair.

---

## 6. Productionization, MLOps, and Scaling

Goal: demonstrate “expensive” skills—reliability, observability, and extensibility.

1. **Service architecture**
   - Break the system into services:
     - `frontend` (web/mobile UI).
     - `gateway` / API.
     - `asr-service`.
     - `tts-service` (if self‑hosted; otherwise thin wrappers around providers).
     - `lesson-orchestrator` (LLM logic + state).
     - `pronunciation-service`.
     - `language-id-service`.
   - Containerize services and define basic deployment setup (docker‑compose or k8s).

2. **Pipelines and experimentation**
   - Set up lightweight pipelines for:
     - Training / fine‑tuning ML models (pronunciation, language ID).
     - Periodic evaluation on held‑out sets.
   - Track experiments:
     - Hyperparameters.
     - Metrics (e.g., WER, language ID accuracy, correlation of pronunciation score with human ratings).

3. **Monitoring and logging**
   - Collect operational metrics:
     - Request counts, latency, error rates per service.
     - ASR WER trends, language‑ID accuracy on labeled samples.
   - Set up dashboards and basic alerts (e.g., if WER spikes for a language, or latency surpasses a threshold).

4. **Personalization and adaptive lessons**
   - Maintain per‑user profiles:
     - Level estimate, common grammar mistakes, pronunciation weaknesses, code‑switching patterns.
   - Use simple decision logic or bandit‑style policies to:
     - Choose the next exercise type.
     - Adjust difficulty and speech speed.
   - Expose this personalization clearly in the UI to emphasize the “intelligent tutor” aspect.

5. **Language and domain expansion**
   - Add more Romance languages (French, Romanian) and later others.
   - Introduce new scenarios:
     - Travel, work, exam preparation, customer‑support simulations, etc.
   - Reuse the same architecture:
     - Add language data.
     - Extend configuration for ASR/TTS and language ID.
     - Add scenario definitions and prompt templates for the LLM.

---
