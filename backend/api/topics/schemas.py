"""
Topics API Schemas.

Defines the request and response data structures using Pydantic via Django Ninja.
Ensures that all incoming query parameters and outgoing JSON payloads strictly adhere
to the defined contracts.
"""
from typing import List, Optional
from ninja import Schema
from ninja import Field
import uuid


# ==========================================
# RESPONSE SCHEMAS
# ==========================================

class TopicCardSchema(Schema):
    """Schema for individual topic cards returned in the list endpoint."""
    id: uuid.UUID
    title: str
    description: str
    difficulty: str
    category: str
    icon: str
    image_url: str
    estimated_turns: int
    grammar_focus: str
    vocabulary_focus: str
    scenario_count: int


class PaginatedTopicResponse(Schema):
    """Paginated wrapper for TopicCardSchema."""
    page: int
    page_size: int
    total: int
    total_pages: int
    has_next: bool
    has_previous: bool
    items: List[TopicCardSchema]


class TopicDetailSchema(Schema):
    """Schema for full topic details returned in the detail endpoint."""
    id: uuid.UUID
    title: str
    description: str
    difficulty: str
    category: str
    grammar_focus: str
    vocabulary_focus: str
    estimated_turns: int
    icon: str
    image_url: str
    learning_objectives: List[str]
    scenario_count: int


class ScenarioCardSchema(Schema):
    """Schema for scenarios returned within a topic."""
    id: uuid.UUID
    title: str
    description: str
    difficulty: str
    ai_role: str
    user_role: str
    grammar_focus: str
    vocabulary_focus: str
    max_turns: int
    is_system: bool
    is_public: bool


class PaginatedScenarioResponse(Schema):
    """Paginated wrapper for ScenarioCardSchema."""
    page: int
    page_size: int
    total: int
    total_pages: int
    has_next: bool
    has_previous: bool
    items: List[ScenarioCardSchema]


# ==========================================
# FILTER SCHEMAS
# ==========================================

class TopicFilterSchema(Schema):
    """Schema for parsing query parameters when listing topics."""
    page: int = Field(1, ge=1)
    limit: int = Field(20, ge=1, le=100)
    search: Optional[str] = None
    difficulty: Optional[str] = None
    category: Optional[str] = None
    ordering: str = "display_order"
    is_active: bool = True


class ScenarioFilterSchema(Schema):
    """Schema for parsing query parameters when listing scenarios."""
    page: int = Field(1, ge=1)
    limit: int = Field(20, ge=1, le=100)
    search: Optional[str] = None
    ordering: str = "title"
    is_active: bool = True
