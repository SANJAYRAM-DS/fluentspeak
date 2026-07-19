# Topics Module: Project Overview

## 1. Purpose of the Topics Module
The Topics module is the foundational data layer of the FluentSpeak application. It exposes learning topics to the frontend. A "Topic" acts as a high-level category or theme (e.g., "Travel", "Daily Life") under which various conversation scenarios are grouped. In Version 1, this module is strictly read-only for standard users, providing them with a browsable, paginated, and searchable catalog of topics. Admin CRUD operations are reserved for future versions.

## 2. Fit Within the Overall Application
Because learning paths and conversational AI interactions are context-dependent, every core feature relies on Topics:
- **Scenarios**: Each scenario belongs to a specific Topic.
- **Conversations**: Conversations are instantiations of Scenarios, inherently linking them back to a Topic.
- **AI & Vocabulary**: AI roleplaying context and vocabulary hints are determined by the active Topic and Scenario.
- **Progress & Analytics**: User progress tracking uses Topics to visualize strengths, weaknesses, and completion rates.

## 3. Request Flow
1. **Frontend Request**: The client requests `/api/v1/topics` with optional query parameters (e.g., `?category=Travel&difficulty=A2`).
2. **API Routing**: Django Ninja's global API (`backend/api/api.py`) routes the request to the `topics` router.
3. **Validation (Schemas/Validators)**: Pydantic schemas validate all incoming parameters (pagination bounds, UUID formatting, valid difficulty levels).
4. **Service Layer**: The `TopicsService` extracts validated filters and dictates business rules (e.g., ensuring inactive topics are excluded for non-admins).
5. **Repository Layer**: The `TopicsRepository` executes an optimized PostgreSQL query, annotating fields like `scenario_count` and avoiding N+1 problems.
6. **Response Generation**: The service processes the queryset and passes it back to the API layer, which serializes it using Pydantic response schemas (e.g., `PaginatedTopicResponse`).

## 4. Module Architecture
The module follows a strict layered architecture to ensure separation of concerns:
- **`router.py` (API Layer)**: Handles only HTTP requests, route definitions, and response formatting. Extremely thin.
- **`schemas.py` & `validators.py` (Schema Layer)**: Defines strict request/response data contracts and custom validators.
- **`service.py` (Business Logic)**: Coordinates data retrieval, pagination calculation, and business rules without caring about HTTP or SQL.
- **`repository.py` (Data Access)**: Centralizes all Django ORM/SQL queries. Optimized for performance using `select_related`, `prefetch_related`, and database annotations.
- **Models (Existing)**: Located in `backend/app/topics/models.py` and `backend/app/scenarios/models.py`. We reuse these without modification.
