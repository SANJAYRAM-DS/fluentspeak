# Topics Module: Testing

This document provides a guide to verify the Topics API behavior using `curl` or Postman.

## 1. List Topics
**Success Case (Default)**:
`curl -X GET http://localhost:8000/api/v1/topics`

**Pagination & Filtering**:
`curl -X GET "http://localhost:8000/api/v1/topics?page=1&limit=5&difficulty=A2"`

**Search**:
`curl -X GET "http://localhost:8000/api/v1/topics?search=travel"`

**Edge Case: Page Exceeds Range (Returns empty items)**:
`curl -X GET "http://localhost:8000/api/v1/topics?page=999"`

**Failure Case: Negative Page (Returns 400)**:
`curl -X GET "http://localhost:8000/api/v1/topics?page=-1"`

**Failure Case: Invalid Ordering (Returns 400)**:
`curl -X GET "http://localhost:8000/api/v1/topics?ordering=invalid_column"`

## 2. Topic Details
**Success Case**:
`curl -X GET http://localhost:8000/api/v1/topics/<valid_uuid>`

**Failure Case: Invalid UUID Format (Returns 404)**:
`curl -X GET http://localhost:8000/api/v1/topics/not-a-uuid-123`

**Failure Case: Non-existent UUID (Returns 404)**:
`curl -X GET http://localhost:8000/api/v1/topics/00000000-0000-0000-0000-000000000000`

## 3. Topic Scenarios
**Success Case**:
`curl -X GET http://localhost:8000/api/v1/topics/<valid_uuid>/scenarios`

## Checklist for QA
- [ ] Do endpoints block SQL injection attempts in the `?search=` parameter? (Yes, ORM parameterized queries).
- [ ] Is `scenario_count` returning correct integers?
- [ ] Are inactive topics hidden from standard responses?
