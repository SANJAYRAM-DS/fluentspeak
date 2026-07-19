"""
Topics API Validators.

This module enforces strict validation rules on input data, ensuring business
rules and security constraints are met before data reaches the service layer.
"""
import re
from uuid import UUID

from backend.core.exceptions import ValidationError, NotFoundError
from backend.app.topics.models import Difficulty


def validate_uuid(id_str: str) -> UUID:
    """
    Validates that a string is a proper UUID.
    Raises NotFoundError (404) if invalid, as requested by edge case requirements.
    """
    try:
        return UUID(str(id_str))
    except (ValueError, TypeError, AttributeError):
        raise NotFoundError("Topic not found.")


def validate_pagination(page: int, limit: int) -> None:
    """
    Ensures pagination parameters are within safe and valid bounds.
    (Note: Pydantic schemas also enforce this, but explicit business validation
    is good for layered defense).
    """
    if page < 1:
        raise ValidationError("Page number must be 1 or greater.")
    if limit < 1:
        raise ValidationError("Limit must be 1 or greater.")
    if limit > 100:
        raise ValidationError("Limit cannot exceed 100.")


def validate_difficulty(difficulty: str) -> None:
    """
    Ensures the requested difficulty is a valid CEFR level.
    """
    if not difficulty:
        return
        
    valid_difficulties = [choice[0] for choice in Difficulty.choices]
    if difficulty not in valid_difficulties:
        raise ValidationError(
            f"Invalid difficulty. Must be one of: {', '.join(valid_difficulties)}"
        )


def validate_topic_ordering(ordering: str) -> None:
    """
    Ensures the ordering parameter is allowed for topics to prevent SQL injection
    or exposing internal database structures.
    """
    if not ordering:
        return
        
    # Remove descending prefix for validation
    clean_order = ordering.lstrip('-')
    allowed = ['display_order', 'title', 'difficulty']
    
    if clean_order not in allowed:
        raise ValidationError(
            f"Invalid ordering. Allowed values: {', '.join(allowed)}"
        )


def validate_scenario_ordering(ordering: str) -> None:
    """
    Ensures the ordering parameter is allowed for scenarios.
    """
    if not ordering:
        return
        
    clean_order = ordering.lstrip('-')
    allowed = ['title', 'difficulty']
    
    if clean_order not in allowed:
        raise ValidationError(
            f"Invalid ordering. Allowed values: {', '.join(allowed)}"
        )


def sanitize_search(search: str) -> str:
    """
    Sanitizes plain text search queries.
    Removes potentially dangerous characters and enforces a strict length limit.
    """
    if not search:
        return ""
        
    # Enforce length limit
    if len(search) > 100:
        raise ValidationError("Search query is too long. Maximum 100 characters.")
        
    # Strip dangerous characters. Allow alphanumerics, spaces, and basic punctuation.
    sanitized = re.sub(r'[^\w\s\-.,?]', '', search).strip()
    return sanitized
