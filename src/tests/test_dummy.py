"""Dummy test module."""

import unittest


class DummyTest(unittest.TestCase):
    """Dummy tests."""

    def setUp(self):
        """Set up function."""

    def tearDown(self):
        """Tear down function."""

    def dummy_test(self):
        """Dummy test."""
        self.assertEqual(1, 1)


if __name__ == "__main__":
    unittest.main()
