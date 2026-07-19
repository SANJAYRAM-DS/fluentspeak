"""
Topics API Router.

Maps HTTP endpoints to the service layer. Defines request methods, response schemas,
and dependency injections (like Query filters). This layer remains strictly thin.
"""
from ninja import Router, Query
from django.http import HttpRequest

from backend.api.topics import service
from backend.api.topics.schemas import (
    TopicFilterSchema,
    ScenarioFilterSchema,
    PaginatedTopicResponse,
    PaginatedScenarioResponse,
    TopicDetailSchema,
)

# Router instance
# For Version 1, these routes are accessible without authentication (auth=None).
# Alternatively, if you want them protected, we would import AuthBearer.
router = Router(tags=["Topics"])


@router.get("/", response=PaginatedTopicResponse, auth=None)
def list_topics(request: HttpRequest, filters: TopicFilterSchema = Query(...)):
    """
    Get All Topics.
    Returns a paginated list of topics based on search, category, difficulty, etc.
    """
    return service.list_topics(filters)


@router.get("/{topic_id}", response=TopicDetailSchema, auth=None)
def get_topic_details(request: HttpRequest, topic_id: str):
    """
    Get Topic Details.
    Returns full information for a specific topic including its derived learning objectives.
    """
    return service.get_topic_details(topic_id)


@router.get("/{topic_id}/scenarios", response=PaginatedScenarioResponse, auth=None)
def get_topic_scenarios(request: HttpRequest, topic_id: str, filters: ScenarioFilterSchema = Query(...)):
    """
    Get Topic Scenarios.
    Returns a paginated list of scenarios belonging to the specified topic.
    """
    return service.list_topic_scenarios(topic_id, filters)
