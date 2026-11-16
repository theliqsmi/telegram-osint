import unittest

from collectors.search import MockSearchProvider, SearchResult


class TestMockSearchProvider(unittest.TestCase):

    def test_search_returns_results(self):
        provider = MockSearchProvider()

        results = provider.search("test query")

        self.assertIsInstance(results, list)
        self.assertGreater(len(results), 0)
        self.assertIsInstance(results[0], SearchResult)
        self.assertEqual(results[0].query, "test query")


if __name__ == "__main__":
    unittest.main()