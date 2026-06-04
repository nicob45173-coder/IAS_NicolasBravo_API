import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app
from app.models import reset_users
@pytest.fixture
def client():
    reset_users()
    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client