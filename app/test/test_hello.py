"""Tests for the hello module."""

import pytest

from app.src.hello import hello


class TestHello:
    """Test cases for the hello function."""

    def test_hello_world(self) -> None:
        """Test that hello() returns 'Hello, World!'."""
        assert hello() == "Hello, World!"

    def test_hello_with_name(self) -> None:
        """Test that hello(name) returns personalized greeting."""
        assert hello("Alice") == "Hello, Alice!"
        assert hello("Bob") == "Hello, Bob!"

    def test_hello_empty_string(self) -> None:
        """Test that hello with empty string returns personalized greeting."""
        assert hello("") == "Hello, should fail!!"
