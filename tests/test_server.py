import pytest
from ..server import create_app
import os
import tempfile


def test_should_status_code_ok(client):
    response1 = client.get('/')
    assert response1.status_code == 200


def test_home_without_email(client):
    rv = client.get("/", follow_redirects=True)
    data = rv.data.decode()
    assert data.find("email") != -1

