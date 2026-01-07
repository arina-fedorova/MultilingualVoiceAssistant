# MultilingualVoiceAssistant

Голосовой ассистент для изучения романских языков.

## О проекте

Система проводит 10-15 минутные разговорные уроки на испанском, итальянском и португальском. Пользователь говорит — ассистент распознаёт речь, оценивает произношение, даёт обратную связь и ведёт диалог дальше. Взаимодействие только голосом, без текстового ввода.

Проект связан с [PolyLadder](https://github.com/arina-fedorova/PolyLadder) — веб-платформой для параллельного изучения языков.

## Компоненты

- **ASR** — распознавание речи на нескольких языках (Whisper)
- **TTS** — синтез речи с контролем просодии
- **Orchestrator** — LLM для управления диалогом и структурой урока
- **Pronunciation Scoring** — ML-модуль для оценки произношения
- **Language ID** — определение языка при переключении между языками

## Технологии

Python 3.11+, Poetry, FastAPI, PyTorch. Версионирование данных через DVC.

## Разработка

```bash
poetry install
poetry run ruff check .
poetry run mypy src/
poetry run pytest
```

## Статус

В разработке. Завершена фаза 0 (инфраструктура).

## Документация

Документация в [PolyLadderCommon/docs/voice-assistant](../PolyLadderCommon/docs/voice-assistant/):
- [PROJECT_SPECIFICATION.md](../PolyLadderCommon/docs/voice-assistant/PROJECT_SPECIFICATION.md) — спецификация
- [ROADMAP.md](../PolyLadderCommon/docs/voice-assistant/ROADMAP.md) — план на 6 фаз
