
import os
import requests

from dataclasses import dataclass
from dotenv import load_dotenv


load_dotenv()


@dataclass
class SearchResult:
    title: str
    url: str
    snippet: str
    query: str


class SearchProvider:
    """Base class for public web search providers."""

    def search(self, query: str) -> list[SearchResult]:
        raise NotImplementedError(
            "Search providers must implement search()."
        )


class TavilySearchProvider(SearchProvider):
    """Search the public web using the Tavily API."""

    API_URL = "https://api.tavily.com/search"

    def __init__(self):
        self.api_key = os.getenv("TAVILY_API_KEY")

        if not self.api_key:
            raise ValueError(
                "TAVILY_API_KEY is missing. Check your .env file."
            )

    def search(self, query: str) -> list[SearchResult]:

        payload = {
            "api_key": self.api_key,
            "query": query,
            "search_depth": "basic",
            "max_results": 5,
        }

        try:
            response = requests.post(
                self.API_URL,
                json=payload,
                timeout=30,
            )

            response.raise_for_status()

        except requests.RequestException as error:
            raise RuntimeError(
                f"Tavily search failed: {error}"
            ) from error

        data = response.json()

        results = []

        for item in data.get("results", []):
            result = SearchResult(
                title=item.get("title", ""),
                url=item.get("url", ""),
                snippet=item.get("content", ""),
                query=query,
            )

            results.append(result)

        return results
