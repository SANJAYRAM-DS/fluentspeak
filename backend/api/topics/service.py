"""
Topics API Service.

This module contains the business logic. It takes validated input from schemas,
interacts with the repository, processes the data, and returns the response payload.
"""
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q

from backend.api.topics import repository, validators
from backend.api.topics.schemas import (
    TopicFilterSchema,
    ScenarioFilterSchema,
    PaginatedTopicResponse,
    PaginatedScenarioResponse,
    TopicDetailSchema,
)
from backend.core.exceptions import NotFoundError


def list_topics(filters: TopicFilterSchema) -> PaginatedTopicResponse:
    """
    Fetches a paginated list of topics based on applied filters.
    """
    # 1. Start with the base optimized queryset
    queryset = repository.get_base_topics_query()

    # 2. Apply filtering
    if filters.is_active:
        queryset = queryset.filter(is_active=True)

    if filters.category:
        queryset = queryset.filter(category=filters.category)

    if filters.difficulty:
        validators.validate_difficulty(filters.difficulty)
        queryset = queryset.filter(difficulty=filters.difficulty)

    if filters.search:
        sanitized_search = validators.sanitize_search(filters.search)
        if sanitized_search:
            # Search by title or description
            queryset = queryset.filter(
                Q(title__icontains=sanitized_search) | 
                Q(description__icontains=sanitized_search)
            )

    # 3. Apply ordering
    if filters.ordering:
        validators.validate_topic_ordering(filters.ordering)
        queryset = queryset.order_by(filters.ordering)

    # 4. Pagination
    validators.validate_pagination(filters.page, filters.limit)
    paginator = Paginator(queryset, filters.limit)
    
    try:
        page_obj = paginator.page(filters.page)
    except EmptyPage:
        # Edge case: page exceeds available records -> return empty list, not an error
        return PaginatedTopicResponse(
            page=filters.page,
            page_size=filters.limit,
            total=paginator.count,
            total_pages=paginator.num_pages,
            has_next=False,
            has_previous=paginator.count > 0,
            items=[]
        )

    return PaginatedTopicResponse(
        page=filters.page,
        page_size=filters.limit,
        total=paginator.count,
        total_pages=paginator.num_pages,
        has_next=page_obj.has_next(),
        has_previous=page_obj.has_previous(),
        items=list(page_obj.object_list)
    )


def get_topic_details(topic_id_str: str) -> TopicDetailSchema:
    """
    Fetches details for a single topic and dynamically calculates learning objectives.
    """
    # 1. Validate UUID format manually to throw 404
    topic_id = validators.validate_uuid(topic_id_str)

    # 2. Fetch from DB
    topic = repository.get_topic_by_id(topic_id)
    if not topic or not topic.is_active:
        raise NotFoundError("Topic not found.")

    # 3. Derive learning objectives from active scenarios
    # Extract non-empty learning_objective fields from related scenarios and deduplicate
    scenarios_qs = repository.get_topic_scenarios_query(topic_id)
    # Assuming we only want active/public ones for learning objectives
    scenarios_qs = scenarios_qs.filter(is_public=True)
    
    objectives_set = set()
    for scenario in scenarios_qs.only('learning_objective'):
        if scenario.learning_objective:
            # We assume it might be comma separated or just single strings.
            # For simplicity, we just add the non-empty string.
            objectives_set.add(scenario.learning_objective.strip())
            
    learning_objectives = sorted(list(objectives_set))

    # 4. Construct and return response
    return TopicDetailSchema(
        id=topic.id,
        title=topic.title,
        description=topic.description,
        difficulty=topic.difficulty,
        category=topic.category,
        grammar_focus=topic.grammar_focus,
        vocabulary_focus=topic.vocabulary_focus,
        estimated_turns=topic.estimated_turns,
        icon=topic.icon,
        image_url=topic.image_url,
        learning_objectives=learning_objectives,
        scenario_count=topic.scenario_count
    )


def list_topic_scenarios(topic_id_str: str, filters: ScenarioFilterSchema) -> PaginatedScenarioResponse:
    """
    Fetches paginated scenarios belonging to a specific topic.
    """
    # 1. Validate UUID and Topic Existence
    topic_id = validators.validate_uuid(topic_id_str)
    topic = repository.get_topic_by_id(topic_id)
    if not topic or not topic.is_active:
        raise NotFoundError("Topic not found.")

    # 2. Get Scenarios QuerySet
    queryset = repository.get_topic_scenarios_query(topic_id)
    
    # 3. Apply Filtering
    # The requirement specifically mentions "Active only", but Scenarios model uses `is_public` 
    # and maybe `is_system` instead of `is_active`. We'll filter on `is_public=True`.
    if filters.is_active:
        queryset = queryset.filter(is_public=True)

    if filters.search:
        sanitized_search = validators.sanitize_search(filters.search)
        if sanitized_search:
            queryset = queryset.filter(
                Q(title__icontains=sanitized_search) | 
                Q(description__icontains=sanitized_search)
            )

    # 4. Apply Ordering
    if filters.ordering:
        validators.validate_scenario_ordering(filters.ordering)
        queryset = queryset.order_by(filters.ordering)

    # 5. Pagination
    validators.validate_pagination(filters.page, filters.limit)
    paginator = Paginator(queryset, filters.limit)
    
    try:
        page_obj = paginator.page(filters.page)
    except EmptyPage:
        return PaginatedScenarioResponse(
            page=filters.page,
            page_size=filters.limit,
            total=paginator.count,
            total_pages=paginator.num_pages,
            has_next=False,
            has_previous=paginator.count > 0,
            items=[]
        )

    return PaginatedScenarioResponse(
        page=filters.page,
        page_size=filters.limit,
        total=paginator.count,
        total_pages=paginator.num_pages,
        has_next=page_obj.has_next(),
        has_previous=page_obj.has_previous(),
        items=list(page_obj.object_list)
    )
