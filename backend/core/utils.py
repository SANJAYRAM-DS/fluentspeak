"""
General utility functions used across the application.
"""
from django.http import HttpRequest


def get_client_ip(request: HttpRequest) -> str:
    """
    Extract the client's IP address from the request.
    Handles requests passing through reverse proxies (like Nginx).
    """
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        # X-Forwarded-For can be a comma-separated list of IPs.
        # The first one is the original client IP.
        ip = x_forwarded_for.split(",")[0].strip()
    else:
        ip = request.META.get("REMOTE_ADDR", "")
    return ip


def get_user_agent(request: HttpRequest) -> str:
    """
    Extract the User-Agent string from the request headers.
    Useful for audit logging.
    """
    return request.META.get("HTTP_USER_AGENT", "")
