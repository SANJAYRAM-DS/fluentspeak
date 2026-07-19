# Topics Module: Dependencies

This document lists every dependency used to implement the Topics module in FluentSpeak. We are leveraging existing project dependencies to keep the module lightweight. No new external libraries are required.

## 1. Django (v6.0+)
- **Purpose**: Provides the core web framework, ORM (Object-Relational Mapping), and database integration.
- **Installation**: Already installed via `pip install django`.
- **Configuration**: Managed in `backend/core/settings.py`.
- **Common Mistakes**: Forgetting to add new apps to `INSTALLED_APPS` (though `topics` and `scenarios` are already installed). Creating N+1 queries when traversing relationships.

## 2. Django Ninja
- **Purpose**: Provides fast, type-safe API routing and parsing. It bridges standard Django with Pydantic for validation.
- **Installation**: Already installed via `pip install django-ninja`.
- **Configuration**: Instantiated globally in `backend/api/api.py`.
- **Common Mistakes**: Returning raw Django QuerySets without proper schema serialization, causing validation errors.

## 3. Pydantic
- **Purpose**: Defines request and response schemas, ensuring data validation (e.g., pagination constraints, difficulty enum checks).
- **Installation**: Installed as a dependency of `django-ninja`.
- **Configuration**: Used extensively in `schemas.py`.
- **Common Mistakes**: Failing to set `orm_mode = True` (or `from_attributes = True` in Pydantic V2) for schemas that serialize ORM objects.

## 4. PostgreSQL (psycopg2-binary)
- **Purpose**: The primary relational database used in production.
- **Installation**: Already installed via `pip install psycopg2-binary`.
- **Configuration**: Configured in `backend/core/settings.py` using `python-decouple` / environment variables.
- **Common Mistakes**: Not using database-level annotations (`Count`, etc.) and instead iterating over objects in Python to count relationships.
