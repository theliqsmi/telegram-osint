import unittest

from queries import clean_username, validate_username, generate_queries


class TestQueries(unittest.TestCase):

    def test_clean_username(self):
        self.assertEqual(clean_username("@example_user"), "example_user")
        self.assertEqual(clean_username("  @example_user  "), "example_user")

    def test_valid_username(self):
        self.assertTrue(validate_username("example_user"))
        self.assertTrue(validate_username("@example123"))

    def test_invalid_username(self):
        self.assertFalse(validate_username("abc"))
        self.assertFalse(validate_username("user name"))
        self.assertFalse(validate_username("hello!"))

    def test_generate_queries(self):
        queries = generate_queries("example_user")

        self.assertIsInstance(queries, list)
        self.assertGreater(len(queries), 0)
        self.assertIn('site:t.me "example_user"', queries)


if __name__ == "__main__":
    unittest.main()