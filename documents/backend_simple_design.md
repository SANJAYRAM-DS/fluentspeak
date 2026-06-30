1. Backend Architecture
backend/
│
├── apps/
│   │
│   ├── users/
│   ├── auth/
│   ├── topics/
│   ├── scenarios/
│   ├── conversations/
│   ├── messages/
│   ├── vocabulary/
│   ├── ai/
│   ├── memory/
│   ├── analytics/
│   ├── billing/
│   └── notifications/
│
├── config/
│
├── shared/
│
├── celery.py
│
├── manage.py
│
└── requirements.txt
2. Service-Oriented Design

Do NOT put business logic inside views.

Bad:

class SendMessageView(APIView):
    def post(self, request):
        # 300 lines here

Good:

View
  ↓
Serializer
  ↓
Service Layer
  ↓
Repository Layer
  ↓
Database

Example:

class SendMessageView(APIView):
    def post(self, request):

        result = ConversationService.send_message(
            user=request.user,
            conversation_id=id,
            message=text
        )

        return Response(result)
3. PostgreSQL Database Design
USERS
users
id UUID PK
email
name
level
avatar
country
timezone

created_at
updated_at
deleted_at
USER SETTINGS
user_settings
id
user_id

daily_goal

preferred_topics

difficulty

notifications_enabled
TOPICS

50 predefined topics.

topics
id
title

description

category

difficulty

image_url

is_active

created_at

Examples:

Travel
Technology
Movies
Business
Health
Sports
SCENARIOS

Custom roleplay.

scenarios
id

user_id

title

description

ai_role

user_role

goal

difficulty

is_public

created_at

Example:

Interview

AI Role:
HR Manager

User Role:
Job Candidate
CONVERSATIONS

Most important table.

conversations
id UUID

user_id

topic_id

scenario_id

status

current_stage

current_turn

summary

started_at

last_activity

created_at
MESSAGES

High volume table.

messages
id

conversation_id

role

content

token_count

latency_ms

provider

model

created_at

role:

USER
ASSISTANT
SYSTEM
MESSAGE FEEDBACK

Stores correction.

message_feedback
id

message_id

correction

optimized_version

created_at
VOCABULARY WORDS

Master vocabulary table.

vocabulary_words
id

word

definition

difficulty

part_of_speech
USER VOCABULARY

Tracks learned words.

user_vocabulary
id

user_id

word_id

mastered

times_seen

times_used

learned_at
CONVERSATION STATE

Stores FSM state.

conversation_state
conversation_id

stage

goal_progress

last_vocab_word

summary

updated_at
AI PROVIDERS

Provider health.

ai_providers
id

name

status

priority

rpm_limit

last_failure
AI REQUESTS

Audit table.

ai_requests
id

user_id

provider

model

prompt_tokens

completion_tokens

cost

latency

status

created_at
ANALYTICS EVENTS

Event sourcing.

analytics_events
id

user_id

event_name

payload JSONB

created_at
4. DRF API Design
AUTH
Register
POST /api/v1/auth/register

Request:

{
  "name":"Sanjay",
  "email":"abc@gmail.com",
  "password":"*****"
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
  "topic_id":"123"
}

Response:

{
  "conversation_id":"abc",
  "first_message":"Hello..."
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
  "message":"I go market yesterday"
}

Response:

{
  "reply":"What did you buy?",
  "correction":"I went to the market yesterday.",
  "optimized":"I went to the market yesterday and bought some fruit.",
  "vocabulary":{
     "word":"fresh",
     "definition":"recently made"
  },
  "examples":[]
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
  "words_learned":450,
  "sessions":120,
  "hours_practiced":75
}
5. Conversation Engine Design

Create:

apps/conversations/services/

Structure:

services/
│
├── conversation_service.py
├── prompt_builder.py
├── memory_service.py
├── vocabulary_service.py
├── state_machine.py
├── response_validator.py
└── ai_router.py
Send Message Flow
User Message
      │
      ▼
Load Conversation
      │
      ▼
Load Summary
      │
      ▼
Load Learned Vocabulary
      │
      ▼
Build Prompt
      │
      ▼
AI Router
      │
      ▼
Validate JSON
      │
      ▼
Save Results
      │
      ▼
Return Response
6. Redis Design

Store:

conversation:{id}

Contains:

{
 "last_messages":[],
 "summary":"..."
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

This is critical because messages will become the largest table.