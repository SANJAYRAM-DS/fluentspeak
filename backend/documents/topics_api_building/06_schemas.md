# Topics Module: Schemas

This document explains the data contracts defined in `backend/api/topics/schemas.py`.

## Why Schemas?
Schemas act as the rigid boundaries of our API. We use Pydantic models to define exactly what an incoming request should look like (e.g., query parameters) and exactly what the JSON response payload must contain. This ensures:
1. **Type Safety**: Django Ninja auto-casts strings from the URL into integers or booleans.
2. **Auto-Documentation**: OpenAPI/Swagger docs are generated automatically based on these fields.
3. **Data Hiding**: We never accidentally leak internal model fields (like `created_at` or `updated_at` if they aren't needed by the client).

## 1. Response Schemas

### `TopicCardSchema`
Used in the list endpoint. It returns only the essential fields needed to render a topic card on the frontend:
- Excludes heavy text fields like full `learning_objectives` if not needed.
- Requires `scenario_count` to immediately show the user how much content is inside.

### `TopicDetailSchema`
Used for fetching a single topic. 
- Includes `learning_objectives`. Because this isn't a column on the `Topic` table, we calculate it dynamically in the Service layer and pass it here.

### `PaginatedTopicResponse` & `PaginatedScenarioResponse`
Wrappers for array payloads. They provide standard pagination metadata (`page`, `total_pages`, `has_next`) so the frontend knows how to render pagination controls.

## 2. Filter (Request) Schemas

### `TopicFilterSchema` & `ScenarioFilterSchema`
Used to validate query parameters from the GET requests (e.g., `?limit=50&category=Travel`).
- Default values are set directly in the schema (`page=1`, `limit=20`, `is_active=True`).
- Pydantic's `Field(ge=1)` naturally catches values like `page=0` and returns a 422, but we also enforce business logic for standard 400 responses in our `validators.py` as requested.
