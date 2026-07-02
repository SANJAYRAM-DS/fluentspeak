Best choice: REST + action endpoints + SSE
Why this is the best fit

REST is the cleanest match for:

users
topics
scenarios
conversations
messages
vocabulary
progress

Your app also needs one critical action: send message → generate AI reply → correction → optimized version → vocab → examples → save state. That part is not a normal CRUD action, so it should be a dedicated endpoint like /conversations/{id}/turns. The PRD already describes this exact turn-by-turn flow and the need to save conversation state and learned vocabulary.

Why this is better than the other options
1) Better than GraphQL

GraphQL is powerful, but for your app it adds unnecessary complexity.

Use GraphQL only if:

many frontend screens need deeply nested data in many different shapes
you have many client types with wildly different needs
you want a single flexible query layer

For this product, GraphQL is not the best first choice because:

chat writes are frequent and stateful
caching becomes harder
auth and rate limiting are more complex
AI turn execution is an action, not just data fetching
Django + DRF is faster and simpler to build and maintain
2) Better than pure RPC

RPC is good for internal microservices, but as a public API it is less self-describing than REST.

RPC works well for:

internal service-to-service calls
very action-heavy systems
low-level performance tuning

But for your app, RPC alone is weaker because:

the frontend still wants resource-based access
browser clients benefit from standard HTTP semantics
documentation is less intuitive
caching and versioning are less elegant
3) Better than pure WebSocket

WebSockets are useful only for live streaming chat text.

But your app is not only streaming chat. It also needs:

topic browsing
scenario management
conversation history
vocabulary stats
progress pages
account/profile operations

So WebSocket should be a small part of the design, not the whole API.

The API I would design
Core principle

Use REST for everything, and use SSE or WebSocket only for AI response streaming.

I would actually prefer SSE over WebSocket here because:

simpler in browsers
easier to scale through proxies and load balancers
perfect for one-way AI token streaming
easier to reconnect
easier to debug
Recommended API structure
Auth
POST /api/v1/auth/register
POST /api/v1/auth/login
POST /api/v1/auth/refresh
POST /api/v1/auth/logout
User profile
GET /api/v1/me
PATCH /api/v1/me
GET /api/v1/me/progress
Topics
GET /api/v1/topics
GET /api/v1/topics/{topic_id}
Scenarios
POST /api/v1/scenarios
GET /api/v1/scenarios
GET /api/v1/scenarios/{scenario_id}
PATCH /api/v1/scenarios/{scenario_id}
DELETE /api/v1/scenarios/{scenario_id}
Conversations
POST /api/v1/conversations
GET /api/v1/conversations
GET /api/v1/conversations/{conversation_id}
PATCH /api/v1/conversations/{conversation_id}
POST /api/v1/conversations/{conversation_id}/switch
DELETE /api/v1/conversations/{conversation_id}
Messages / turns
POST /api/v1/conversations/{conversation_id}/turns
GET /api/v1/conversations/{conversation_id}/messages
GET /api/v1/conversations/{conversation_id}/turns/{turn_id}
Vocabulary
GET /api/v1/vocabulary/learned
POST /api/v1/vocabulary/learned
DELETE /api/v1/vocabulary/learned/{word_id}
GET /api/v1/vocabulary/stats
AI streaming
GET /api/v1/conversations/{conversation_id}/turns/{turn_id}/stream
Best request shape for the chat endpoint

Use one turn endpoint that handles everything for a user message:

POST /api/v1/conversations/{conversation_id}/turns
{
  "message": "I go to market yesterday.",
  "client_message_id": "uuid",
  "conversation_revision": 12
}
Response
{
  "turn_id": "uuid",
  "conversation_id": "uuid",
  "reply": "That sounds interesting. What did you buy there?",
  "correction": "I went to the market yesterday.",
  "optimized_response": "I went to the market yesterday and bought some fresh fruit.",
  "vocabulary": {
    "word": "fresh",
    "definition": "recently made or picked",
    "examples": [
      "The vegetables are fresh.",
      "I like fresh juice in the morning.",
      "Fresh air makes me feel better.",
      "She bought fresh flowers.",
      "This bread is still fresh."
    ]
  },
  "next_question": "What was the best thing you bought?",
  "conversation_revision": 13
}

That shape matches your PRD exactly, because the app needs one natural reply, one correction, one optimized sentence, one new word, five examples, and the next question.

Best backend behavior for Django
Use Django REST Framework for:
CRUD endpoints
auth
topic lists
scenario management
vocabulary and progress
conversation history
Use a service layer for:
conversation orchestration
prompt building
provider fallback
vocabulary dedupe
state transitions
schema validation
Use SSE for:
streaming AI response tokens
streaming “thinking/loading” states
incremental UX updates
Why this design is the best overall

This API design is better because it gives you:

Simple mental model
Everything is a resource except the AI turn, which is a single explicit action.
Easy Django implementation
DRF is a natural fit for this style.
Better caching
Topics, scenarios, progress, and history can all be cached or paginated normally.
Cleaner scaling
Chat generation is isolated, so you can scale the turn engine separately from read-heavy endpoints.
Better reliability
Idempotency keys, revision numbers, and retries fit naturally into a REST turn endpoint.
Easier mobile future
A REST API is straightforward for web, mobile, and third-party clients.
Cleaner analytics
Every turn becomes a discrete event you can track, replay, and analyze.
My final recommendation

Use this combination:

Public API style: REST
Special chat action: /conversations/{id}/turns
Streaming: SSE
Backend framework: Django + DRF
Database: PostgreSQL
Cache / rate limit / state: Redis

That is the best balance of simplicity, scalability, maintainability, and product fit for your English practice app.