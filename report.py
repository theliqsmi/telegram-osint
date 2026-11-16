import json
from datetime import datetime, timezone
from pathlib import Path


def save_report(username, queries, results):
    """Save search queries and public results to JSON."""

    report = {
        "username": username,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "queries": queries,
        "results": [
            {
                "title": result.title,
                "url": result.url,
                "snippet": result.snippet,
                "query": result.query,
            }
            for result in results
        ],
    }

    reports_directory = Path("reports")
    reports_directory.mkdir(exist_ok=True)

    filename = reports_directory / f"{username}_report.json"

    with filename.open("w", encoding="utf-8") as file:
        json.dump(report, file, indent=4, ensure_ascii=False)

    return filename