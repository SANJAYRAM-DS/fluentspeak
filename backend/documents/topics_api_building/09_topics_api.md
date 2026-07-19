# Topics Module: API Documentation

## `GET /api/v1/topics`
**Description**: Fetches a paginated list of topic cards.
**Flow**:
1. Client sends GET request with optional query params (e.g., `?difficulty=A2&page=2`).
2. Django Ninja captures `page=2` and `difficulty="A2"` and injects them into `TopicFilterSchema`.
3. `list_topics` in `service.py` is invoked.
4. `get_base_topics_query` annotates `scenario_count`.
5. Service applies `.filter(difficulty="A2")`.
6. Paginator slices the 2nd page.
7. `PaginatedTopicResponse` formats and returns JSON.

## `GET /api/v1/topics/{topic_id}`
**Description**: Fetches detailed information for one topic.
**Flow**:
1. Client requests UUID in path.
2. `topic_id` passed as string to router.
3. `validators.validate_uuid` parses it; throws 404 if invalid.
4. `repository.get_topic_by_id` fetches the row.
5. Scenarios are queried to derive `learning_objectives`.
6. `TopicDetailSchema` formats the response.

## `GET /api/v1/topics/{topic_id}/scenarios`
**Description**: Fetches scenarios attached to a specific topic.
**Flow**:
1. Path param `topic_id` and query params injected into `ScenarioFilterSchema`.
2. Validates UUID and ensures topic exists (404 otherwise).
3. Fetches scenarios `where topic_id = topic_id` and `is_public = True`.
4. Applies any text search or ordering parameters.
5. Paginated and wrapped in `PaginatedScenarioResponse`.
