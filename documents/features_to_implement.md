# FluentFlow AI — Feature Checklist

> Cross-referenced from `prd.md`, `api_design.md`, and `backend_simple_design.md`.

---

## Core Features (PRD)

### Feature 1 — Topic-Based Conversations
- [x] Topics model with title, description, difficulty, category, is_active
- [x] 50 seed topics via `seed_topics` management command
- [x] GET /api/v1/topics — list active topics
- [x] GET /api/v1/topics/{id} — topic detail
- [x] Dashboard shows topic cards and "Start lesson" buttons
- [x] Clicking a topic creates a conversation and opens the chat page

### Feature 2 — Scenario-Based Conversations
- [x] Scenarios model with user_id, title, description, ai_role, user_role, goal, max_turns
- [x] POST /api/v1/scenarios — create scenario
- [x] GET /api/v1/scenarios — list user scenarios
- [x] GET /api/v1/scenarios/{id} — scenario detail
- [x] PUT /api/v1/scenarios/{id} — update scenario
- [x] DELETE /api/v1/scenarios/{id} — delete scenario
- [x] Conversations can link to either a topic_id or scenario_id

### Feature 3 — Conversation Learning Loop
- [x] POST /api/v1/conversations/{id}/turns — send message, get AI turn
- [x] AI returns: reply, correction, optimized_response, vocabulary, next_question
- [x] Five example sentences returned in vocabulary payload
- [x] Prompt builder sends topic, scenario, level, summary, learned_words, message
- [x] Response validator checks all required keys

### Feature 4 — Vocabulary Memory System
- [x] VocabularyWord model (word, definition, difficulty, examples JSONB)
- [x] UserVocabulary model (user, vocabulary, mastered, times_seen, learned_at)
- [x] VocabularyService checks seen words before generating new vocabulary
- [x] GET /api/v1/vocabulary/learned — list learned words
- [x] POST /api/v1/vocabulary/learned — manually add a word
- [x] DELETE /api/v1/vocabulary/learned/{id} — remove a word
- [x] POST /api/v1/vocabulary/learned/{id}/master — mark mastered
- [x] GET /api/v1/vocabulary/stats — stats (learned, mastered, total seen)

### Feature 5 — Difficulty Levels
- [x] User profile stores `level` (beginner, intermediate, advanced)
- [x] Level is passed in prompt payload
- [x] System prompt instructs AI to adapt language per difficulty level

### Feature 6 — Progress Dashboard
- [x] UserProgress model (conversations_completed, words_learned, current_streak, total_minutes)
- [x] GET /api/v1/me/progress — user progress endpoint
- [x] Frontend progress page shows stats

### Feature 7 — Conversation Switch
- [x] POST /api/v1/conversations/{id}/switch — change topic/scenario mid-conversation
- [x] Previous conversation state preserved

---

## API Endpoints (api_design.md)

### Auth
- [x] POST /api/v1/auth/register
- [x] POST /api/v1/auth/login
- [x] POST /api/v1/auth/refresh
- [x] POST /api/v1/auth/logout (with refresh token blacklist)

### User Profile
- [x] GET /api/v1/me
- [x] PATCH /api/v1/me
- [x] GET /api/v1/me/progress

### Topics
- [x] GET /api/v1/topics
- [x] GET /api/v1/topics/{id}

### Scenarios
- [x] POST /api/v1/scenarios
- [x] GET /api/v1/scenarios
- [x] GET /api/v1/scenarios/{id}
- [x] PUT /api/v1/scenarios/{id}
- [x] DELETE /api/v1/scenarios/{id}

### Conversations
- [x] POST /api/v1/conversations
- [x] GET /api/v1/conversations
- [x] GET /api/v1/conversations/{id}
- [x] DELETE /api/v1/conversations/{id}
- [x] POST /api/v1/conversations/{id}/switch

### Messages / Turns
- [x] POST /api/v1/conversations/{id}/turns
- [x] GET /api/v1/conversations/{id}/messages
- [x] GET /api/v1/conversations/{id}/turns/{turn_id}
- [x] GET /api/v1/conversations/{id}/turns/stream (SSE)

### Vocabulary
- [x] GET /api/v1/vocabulary/learned
- [x] POST /api/v1/vocabulary/learned
- [x] DELETE /api/v1/vocabulary/learned/{id}
- [x] POST /api/v1/vocabulary/learned/{id}/master
- [x] GET /api/v1/vocabulary/stats

---

## Backend Architecture (backend_simple_design.md)

### Apps
- [x] users
- [x] topics
- [x] scenarios
- [x] conversations (with services/)
- [x] vocabulary
- [x] ai
- [x] analytics
- [x] notifications
- [x] tasks

### Service Layer
- [x] conversation_service.py
- [x] prompt_builder.py
- [x] memory_service.py
- [x] vocabulary_service.py
- [x] state_machine.py
- [x] response_validator.py
- [x] ai_router.py

### Database Models
- [x] users
- [x] user_profiles
- [x] user_progress
- [x] topics
- [x] scenarios
- [x] conversations
- [x] messages
- [x] message_feedback
- [x] conversation_states
- [x] vocabulary_words
- [x] user_vocabulary
- [x] ai_providers
- [x] audit_logs
- [x] analytics_events
- [x] notifications

### Infrastructure
- [x] Multi-Groq API key rotation
- [x] Celery task stubs (summarize, track_event, send_reminder, check_provider_health)
- [x] PostgreSQL database configuration
- [x] Redis/Celery broker configuration
- [x] CORS middleware
- [x] JWT authentication

---

## Frontend Pages
- [x] Auth page (login + register)
- [x] Dashboard (topics, scenarios, stats)
- [x] Chat (message thread, correction sidebar, vocabulary sidebar)
- [x] Vocabulary (learned words list, mark mastered, delete)
- [x] Progress (stats display)

---

## Nice To Have (not yet implemented)
- [ ] Docker Compose for PostgreSQL, Redis, and Django
- [ ] Fixture or migration-based demo data
- [ ] Streaming frontend that consumes the SSE turn endpoint
- [ ] Real-time conversation summarization via Celery
- [ ] Provider health check that actually pings Groq
- [ ] Push notifications via the notifications model
