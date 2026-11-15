import re


def clean_username(username: str) -> str:
    """Remove spaces and an optional @ symbol from a username."""
    return username.strip().lstrip("@")


def validate_username(username: str) -> bool:
    """Check whether a username has a valid basic format."""

    cleaned = clean_username(username)

    pattern = r"^[A-Za-z0-9_]{5,32}$"

    return bool(re.match(pattern, cleaned))