# Topics Module: Service Layer

This document explains the business logic mapped inside `backend/api/topics/service.py`.

## 1. Separation of Concerns
The Service Layer intercepts data between the router (API HTTP request) and the repository (Database). It orchestrates exactly how data should be filtered, paginated, and processed.

## 2. Search and Filtering Logic
When `list_topics` is called:
- `is_active=True` is always applied by default.
- If a `search` string is provided, we construct a logical `OR` condition using Django's `Q` objects: `Q(title__icontains=search) | Q(description__icontains=search)`.
- Because the input was sanitized by `validators.py` earlier, we safely pass it to the ORM.

## 3. Pagination Engine
We use Django's native `Paginator`.
- **Edge Case Handling**: If a user asks for `page=99` but only 5 pages exist, `Paginator` throws an `EmptyPage` exception.
- Rather than throwing a 404 or 400 error (which disrupts frontend list rendering), we catch this exception and return an empty `items: []` list. This is the standard behavior expected by robust frontend infinite-scroll implementations.

## 4. Deriving Learning Objectives
In `get_topic_details`, the `learning_objectives` field is not physically stored on the `Topic` model.
- We query all public scenarios tied to this topic.
- We pull only the `learning_objective` column (`.only('learning_objective')`) to minimize memory.
- We deduplicate them using a Python `set()` and exclude empty strings.
- This creates a dynamic, always-accurate array of objectives for the frontend topic view.
