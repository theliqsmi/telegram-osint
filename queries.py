import re


def clean_username(username: str) -> str:
    """Remove spaces and an optional @ symbol from a username."""
    return username.strip().lstrip("@")


def validate_username(username: str) -> bool:
    """Check whether a username has a valid basic format."""

    cleaned = clean_username(username)

    pattern = r"^[A-Za-z0-9_]{5,32}$"

    return bool(re.match(pattern, cleaned))

def generate_queries(username: str) -> list[str]:
    """Generate public web search queries for a username."""

    cleaned = clean_username(username)

    queries = [
        f'"{cleaned}" Telegram',
        f'"@{cleaned}"',
        f'site:t.me "{cleaned}"',
        f'"{cleaned}" profile',
        f'"{cleaned}" social media',
    ]

    return queries