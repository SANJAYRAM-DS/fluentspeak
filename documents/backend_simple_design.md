1. Backend Architecture
backend/
|-- apps/
|   |-- users/
|   |-- topics/
|   |-- scenarios/
|   |-- conversations/
|   |   |-- services/
|   |-- vocabulary/
|   |-- ai/
|   |-- analytics/
|   |-- notifications/
|   `-- tasks/
|-- config/
|-- shared/
|-- manage.py
|-- requirements.txt
`-- celery.py

2. Service-Oriented Design

Do not put business logic inside views.

Request flow:
View
  ->
Serializer
  ->
Service Layer
  ->
Repository Layer
  ->
Database

Example:

class SendMessageView(APIView):
    def post(self, request, pk):
        result = ConversationService.send_message(
            user=request.user,
            conversation_id=pk,
            message=request.data["message"]
        )
        return Response(result)

3. PostgreSQL Database Design

Source of truth: `documents/database_schema.png`

USERS
users
id UUID PK
email
password_hash
is_active
is_verified
created_at
updated_at

USER PROFILES
user_profiles
id UUID PK
user_id UUID FK
full_name
avatar_url
level
daily_goal
timezone

USER PROGRESS
user_progress
user_id UUID PK/FK
conversations_completed
words_learned
current_streak
total_minutes

TOPICS
topics
id UUID PK
title
description
difficulty
category
is_active

SCENARIOS
scenarios
id UUID PK
user_id UUID FK
title
description
ai_role
user_role
goal
max_turns
created_at

CONVERSATIONS
conversations
id UUID PK
user_id UUID FK
topic_id UUID FK nullable
scenario_id UUID FK nullable
title
status
current_turn
summary
created_at
updated_at

MESSAGES
messages
id UUID PK
conversation_id UUID FK
role
content
turn_number
created_at

MESSAGE FEEDBACK
message_feedback
id UUID PK
message_id UUID FK
correction
optimized_response
next_question

CONVERSATION STATE
conversation_states
conversation_id UUID PK/FK
stage
tone
goal_progress
last_vocab_word
summary

VOCABULARY WORDS
vocabulary_words
id UUID PK
word
definition
difficulty
examples JSONB

USER VOCABULARY
user_vocabulary
id UUID PK
user_id UUID FK
vocabulary_id UUID FK
mastered
times_seen
learned_at

AI PROVIDERS
ai_providers
id UUID PK
name
model
priority
status

AUDIT LOGS
audit_logs
id UUID PK
user_id UUID FK
action
metadata JSONB
created_at

NOTIFICATIONS
notifications
id UUID PK
user_id UUID FK
title
message
is_read
created_at

Notes:
- The schema image does not include `user_settings`, `ai_requests`, or `analytics_events`, so those are intentionally omitted for now.
- `auth` is handled inside the `users` app through JWT endpoints.
- `messages`, `conversation_states`, and `message_feedback` are part of the conversation domain, not separate standalone apps.

4. DRF API Design

AUTH
Register
POST /api/v1/auth/register

Request:
{
  "name": "Sanjay",
  "email": "abc@gmail.com",
  "password": "*****"
}

Login
POST /api/v1/auth/login

Refresh Token
POST /api/v1/auth/refresh

TOPICS
Get Topics
GET /api/v1/topics

Topic Detail
GET /api/v1/topics/{id}

SCENARIOS
Create Scenario
POST /api/v1/scenarios

Update Scenario
PUT /api/v1/scenarios/{id}

Delete Scenario
DELETE /api/v1/scenarios/{id}

List User Scenarios
GET /api/v1/scenarios

CONVERSATIONS
Create Conversation
POST /api/v1/conversations

Request:
{
  "topic_id": "123"
}

Response:
{
  "conversation_id": "abc",
  "first_message": "Hello..."
}

List Conversations
GET /api/v1/conversations

Get Conversation
GET /api/v1/conversations/{id}

Delete Conversation
DELETE /api/v1/conversations/{id}

SEND MESSAGE

Core endpoint.

POST /api/v1/conversations/{id}/messages

Request:
{
  "message": "I go market yesterday"
}

Response:
{
  "reply": "What did you buy?",
  "correction": "I went to the market yesterday.",
  "optimized": "I went to the market yesterday and bought some fruit.",
  "vocabulary": {
    "word": "fresh",
    "definition": "recently made"
  },
  "examples": []
}

VOCABULARY
Learned Words
GET /api/v1/vocabulary

Mark Mastered
POST /api/v1/vocabulary/{id}/master

Vocabulary Stats
GET /api/v1/vocabulary/stats

PROGRESS
User Progress
GET /api/v1/progress

Response:
{
  "conversations_completed": 120,
  "words_learned": 450,
  "current_streak": 14,
  "total_minutes": 75
}

5. Conversation Engine Design

Create:
apps/conversations/services/

Structure:
services/
|-- conversation_service.py
|-- prompt_builder.py
|-- memory_service.py
|-- vocabulary_service.py
|-- state_machine.py
|-- response_validator.py
`-- ai_router.py

Send Message Flow
User Message
  ->
Load Conversation
  ->
Load Summary
  ->
Load Learned Vocabulary
  ->
Build Prompt
  ->
AI Router
  ->
Validate JSON
  ->
Save Results
  ->
Return Response

6. Redis Design

Store:
conversation:{id}

Contains:
{
  "last_messages": [],
  "summary": "..."
}

Rate Limiting:
user:123:rpm

Provider Health:
provider:groq

7. Celery Jobs

Create:
apps/tasks/

Tasks:
Summarize Conversation
summarize_conversation()

Update Analytics
track_event()

Send Reminder
send_reminder()

Provider Health Check
check_provider_health()

8. Future-Proof Database Decisions

For large scale:
Partition Messages Table
PARTITION BY RANGE(created_at)

Monthly partitions:
messages_2026_01
messages_2026_02
messages_2026_03

This matters because `messages` will become the largest table.
