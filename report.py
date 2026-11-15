import json
from datetime import datetime
from pathlib import Path


def save_report(username: str, queries: list[str]) -> Path:
    """Save generated queries as a JSON report."""

    report = {
        "username": username,
        "generated_at": datetime.now().isoformat(),
        "queries": queries,
    }

    reports_directory = Path("reports")
    reports_directory.mkdir(exist_ok=True)

    filename = reports_directory / f"{username}_report.json"

    with filename.open("w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    return filename