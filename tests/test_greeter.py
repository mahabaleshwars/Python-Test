"""Tests for the greeter module."""

import unittest
from python_test.greeter import greet, farewell


class TestGreeter(unittest.TestCase):
    """Test cases for greeter functions."""

    def test_greet_default(self):
        """Test greet with default parameter."""
        self.assertEqual(greet(), "Hello, World!")

    def test_greet_with_name(self):
        """Test greet with custom name."""
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        self.assertEqual(greet("Bob"), "Hello, Bob!")

    def test_farewell_default(self):
        """Test farewell with default parameter."""
        self.assertEqual(farewell(), "Goodbye, World!")

    def test_farewell_with_name(self):
        """Test farewell with custom name."""
        self.assertEqual(farewell("Alice"), "Goodbye, Alice!")
        self.assertEqual(farewell("Bob"), "Goodbye, Bob!")


if __name__ == "__main__":
    unittest.main()
