"""Basic tests for polyvoice package."""

import polyvoice


def test_version() -> None:
    """Test that version is defined."""
    assert polyvoice.__version__ == "0.1.0"


def test_package_import() -> None:
    """Test that package can be imported."""
    assert polyvoice.__name__ == "polyvoice"
