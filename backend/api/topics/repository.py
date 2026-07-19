"""
Topics API Repository.

This module encapsulates all database interactions related to Topics and Scenarios.
It strictly returns Django QuerySets or Model instances, preventing business logic
from leaking into the database layer.
"""
from typing import Optional
from uuid import UUID

from django.db.models import Count, QuerySet, Q

from backend.app.topics.models import Topic
from backend.app.scenarios.models import Scenario


def get_base_topics_query() -> QuerySet[Topic]:
    """
    Returns the base queryset for topics.
    Annotates the scenario_count to prevent N+1 queries when rendering topic cards.
    We only count active scenarios if there is an is_active flag (defaulting to True if none).
    """
    # Assuming scenarios don't have an explicit 'is_active' flag yet, 
    # but we'll use Count('scenarios') safely.
    return Topic.objects.annotate(
        scenario_count=Count('scenarios')
    )


def get_topic_by_id(topic_id: UUID) -> Optional[Topic]:
    """
    Fetches a single topic by ID, including its annotated scenario count.
    """
    return get_base_topics_query().filter(id=topic_id).first()


def get_topic_scenarios_query(topic_id: UUID) -> QuerySet[Scenario]:
    """
    Returns the base queryset for scenarios belonging to a specific topic.
    """
    return Scenario.objects.filter(topic_id=topic_id)
