# Topics Module: Repository Layer

This document explains the database queries used in `backend/api/topics/repository.py`.

## 1. Why the Repository Pattern?
The repository encapsulates all Django ORM logic. If the database schema changes, only this file changes. The Service Layer does not know it's using PostgreSQL or Django ORM; it just calls functions like `get_topic_by_id`.

## 2. Query Optimizations & Annotations

### Scenario Count
When rendering the topic list (`GET /api/v1/topics`), the frontend needs `scenario_count`.
If we just iterated over topics and called `topic.scenarios.count()`, we would trigger an **N+1 query problem** (1 query for topics + N queries for each topic's count).
**Optimization**: We use Django's `annotate(scenario_count=Count('scenarios'))` in `get_base_topics_query()`. This executes the count via a SQL `JOIN / GROUP BY` directly in the database, reducing it to a single optimized query.

### Fetching Scenarios
`get_topic_scenarios_query(topic_id)` returns an unevaluated QuerySet. We let the Service Layer apply further filters (`is_public`) and sorting before it actually executes. This avoids fetching everything into Python memory.
