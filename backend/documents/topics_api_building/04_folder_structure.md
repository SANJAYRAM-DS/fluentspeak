# Topics Module: Folder Structure

This document details the folders and files that constitute the Topics module implementation.

## 1. Documentation (`backend/documents/topics_api_building/`)
Contains all the Markdown files explaining the architecture, setup, models, and flow of the Topics module. This serves as the blueprint for current and future developers.

## 2. API Package (`backend/api/topics/`)
This is the core directory being built in this implementation. It separates concerns into clear layers.

### `__init__.py`
Initializes the Python package.

### `schemas.py`
**Responsibility**: Defines the shape of the data entering and leaving the API.
**Dependencies**: `pydantic`.
- Contains `TopicCardSchema` (for list view).
- Contains `TopicDetailSchema` (for individual topic details).
- Contains `ScenarioCardSchema` (for topic scenarios list).
- Contains `PaginatedResponse` wrappers.

### `validators.py`
**Responsibility**: Enforces data integrity before it reaches the service layer.
**Dependencies**: `pydantic`, `uuid`.
- Contains helper functions to sanitize search strings.
- Contains validators for `limit`, `page`, and `difficulty` choices.

### `repository.py`
**Responsibility**: Encapsulates all database interactions.
**Dependencies**: `backend.app.topics.models.Topic`, `backend.app.scenarios.models.Scenario`, `django.db.models`.
- Responsible for querying, filtering, annotating (`scenario_count`), and selecting related objects efficiently.

### `service.py`
**Responsibility**: Implements the business logic of the module.
**Dependencies**: `repository.py`, `schemas.py`, `backend.core.exceptions`.
- Translates API requests into repository calls.
- Constructs pagination metadata (`total_pages`, `has_next`, etc.).
- Derives `learning_objectives` from related scenarios for the detail view.

### `router.py`
**Responsibility**: Defines the HTTP endpoints and routes requests to the service layer.
**Dependencies**: `django-ninja`, `service.py`, `schemas.py`.
- Maps `GET /` to listing topics.
- Maps `GET /{topic_id}` to fetching a single topic.
- Maps `GET /{topic_id}/scenarios` to fetching scenarios.
