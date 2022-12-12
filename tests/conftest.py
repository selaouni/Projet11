import pytest
from ..server import create_app
import os
import tempfile


@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client