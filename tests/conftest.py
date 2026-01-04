"""Pytest configuration and fixtures."""

import pytest


@pytest.fixture
def sample_text() -> str:
    """Sample text for testing."""
    return "Hello, world!"
