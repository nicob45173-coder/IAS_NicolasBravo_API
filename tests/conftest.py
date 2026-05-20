import pytest
from app import create_app
from app.models import reset_users

@pytest.fixture
def client():
    reset_users()
    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client