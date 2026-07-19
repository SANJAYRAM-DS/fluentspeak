# Topics Module: Configuration

This document outlines the configurations necessary for the Topics module.

## 1. URLs and API Versioning
The Topics module will be exposed under the `/api/v1/topics` path.
We leverage Django Ninja's router registration in `backend/api/api.py`.

```python
# backend/api/api.py
from backend.api.topics.router import router as topics_router

# The router will be mounted at the global API instance:
api.add_router("/v1/topics", topics_router)
```

## 2. Environment Variables
No new environment variables are strictly required for the Topics module to function beyond standard database configurations:
- `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`: Required for PostgreSQL connectivity.
- `MAX_PAGE_SIZE`: A potential environment variable for global API rate limiting or pagination max sizes, though we will hardcode the limit of `100` in the validator for this module.

## 3. Security and Permissions
For Version 1, the Topics module endpoints are **read-only** and **publicly accessible** (or accessible to any authenticated user, depending on global settings, though topics generally should be browseable).
- Admin endpoints (e.g., `POST`, `PUT`, `DELETE`) will be added in a future module and will require strict RBAC/Permission dependencies.

## 4. Settings
Ensure that the `topics` and `scenarios` applications are registered in `backend/core/settings.py` under `INSTALLED_APPS` (they already are in the current architecture).
