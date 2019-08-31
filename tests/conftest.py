# import third party libs
import pytest

# import app libs
from app import create_app


@pytest.fixture
def client():
    app = create_app("test")
    client = app.test_client()

    yield client
