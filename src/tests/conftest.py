import jwt
import os
import pytest
from starlette.testclient import TestClient
from src.main import app


@pytest.fixture(scope="module")
def token():
    payload = {"user_id": 30, "username": "test_user"}
    secret_key = os.getenv('SECRET_KEY')
    algorithm = os.getenv('JWT_ALGORITHM')
    token = jwt.encode(payload, secret_key, algorithm=algorithm)
    return token


@pytest.fixture(scope="module")
def invalid_token():
    payload = {"user_id": 444, "username": "test_user", 'email': "testmail@gmail.com"}
    secret_key = 'MYAWESOMESECRETKEY'
    algorithm = os.getenv('JWT_ALGORITHM')
    token = jwt.encode(payload, secret_key, algorithm=algorithm)
    return token


@pytest.fixture(scope="module")
def test_client():
    client = TestClient(app)
    yield client
