from dataclasses import dataclass


@dataclass
class SearchResult:
    title: str
    url: str
    snippet: str
    query: str

result = SearchResult(
    title="Example Profile",
    url="https://example.com",
    snippet="A publicly indexed profile.",
    query='"example_user" Telegram',
)

class SearchProvider:
    """Base class for public web search providers."""

    def search(self, query: str) -> list[SearchResult]:
        raise NotImplementedError("Search providers must implement search().")

class MockSearchProvider(SearchProvider):
    """Temporary provider that returns sample public search results."""

    def search(self, query: str) -> list[SearchResult]:
        return [
            SearchResult(
                title="Example public result",
                url="https://example.com",
                snippet=f"Sample result generated for: {query}",
                query=query,
            )
        ]