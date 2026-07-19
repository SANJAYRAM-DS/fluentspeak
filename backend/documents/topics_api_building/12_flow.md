# Topics Module: Complete Lifecycle Flow

This document serves as the master flow diagram explaining exactly how the Topics module processes requests from start to finish.

## 1. Request Entry & Routing
- An HTTP `GET` request reaches `api.py` under the `/api/v1/topics` namespace.
- It is delegated to `backend/api/topics/router.py`.

## 2. Validation & Schema Parsing
- Django Ninja inspects the function signature in `router.py`.
- It sees `filters: TopicFilterSchema = Query(...)`.
- It parses the URL query string, casting `page=2` into an integer. 
- If parsing fails, a 422 error is returned.

## 3. Business Service Execution
- `service.py` receives the strictly typed `filters` object.
- It performs explicit business validation by calling functions in `validators.py` (e.g., ensuring `page >= 1` and `limit <= 100`).
- If validation fails, a `ValidationError` (400) is raised.

## 4. Repository Execution
- `service.py` calls `repository.get_base_topics_query()`.
- The repository returns a Django `QuerySet` that is inherently optimized using `.annotate(scenario_count=Count('scenarios'))`. The database hasn't been touched yet (Lazy loading).
- `service.py` chains `.filter()` and `.order_by()` onto this queryset based on the sanitized user inputs.

## 5. Pagination & Database Hit
- The modified `QuerySet` is passed to Django's `Paginator`.
- The moment `paginator.page(page_number)` is called, the ORM generates a `LIMIT / OFFSET` SQL query and hits PostgreSQL.
- If the requested page exceeds the available records, `EmptyPage` is raised. The service catches this and prepares an empty JSON payload instead of an error.

## 6. Response Serialization
- `service.py` maps the raw database records into the final `PaginatedTopicResponse` wrapper, injecting properties like `has_next`.
- This is returned up to `router.py`, where Django Ninja serializes it back to JSON strings for the client.

## 7. Error Handling
- If any custom exception (`ValidationError`, `NotFoundError`) is raised during this lifecycle, it completely halts execution.
- It bubbles up to the global `@api.exception_handler` in `api.py`.
- The global handler intercepts the exception and cleanly formats it as `{"message": "error description"}` with the corresponding HTTP status code.

## Future Modifiability
To safely modify this module:
- **New Query Parameter**: Add it to `TopicFilterSchema`, then update `service.py` to filter by it.
- **New Response Field**: Add it to `TopicCardSchema` and the ORM model.
- **Admin Endpoints**: Create a new router prefix (e.g., `/admin/topics`) and ensure it requires `AuthBearer` with admin claims. Do not attach CRUD logic to the read-only public router.
