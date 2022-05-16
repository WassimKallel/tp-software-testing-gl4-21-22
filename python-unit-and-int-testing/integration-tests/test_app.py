import pytest
from app import create_app
from utils.create_db import create_db
import os


@pytest.fixture(scope="session", autouse=True)
def create_test_database(tmp_path_factory):
    tmp_dir = tmp_path_factory.mktemp("tmp")
    database_filename = tmp_dir / "test_database.db"
    create_db(database_filename)
    os.environ["DATABASE_FILENAME"] = str(database_filename)


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app(__name__)
    testing_client = flask_app.test_client(use_cookies=False)
    context = flask_app.app_context()
    context.push()
    yield testing_client
    context.pop()


def test_create_user(test_client):
    # Given
    request_payload = {
        "username": "foulen",
        "fullname": "Foulen Ben Foulen"
    }

    expected_body = {
        "username": "foulen",
        "full_name": "Foulen Ben Foulen"
    }
    expected_status_code = 200

    expected_body_keys = ["user_id", "username", "full_name"]

    # When
    response = test_client.post('/users', json=request_payload)

    # Then
    assert expected_status_code == response.status_code
    assert response.json | expected_body == response.json
    assert set(expected_body_keys) == response.json.keys()
    assert int == type(response.json["user_id"])


def test_create_user2(test_client):
    # Given
    request_payload = {
        "username": "amine",
        "fullname": "Amine Haj Ali"
    }

    expected_body = {
        "username": "amine",
        "full_name": "Amine Haj Ali"
    }
    expected_status_code = 200

    expected_body_keys = ["user_id", "username", "full_name"]

    # When
    response = test_client.post('/users', json=request_payload)

    # Then
    assert expected_status_code == response.status_code
    assert response.json | expected_body == response.json
    assert set(expected_body_keys) == response.json.keys()
    assert int == type(response.json["user_id"])


def test_get_all_users(test_client):
    # Given
    expected_response = [
        {
            "user_id": 1,
            "username": "foulen",
            "full_name": "Foulen Ben Foulen"
        },
        {
            "user_id": 2,
            "username": "amine",
            "full_name": "Amine Haj Ali"
        }
    ]

    # When
    response = test_client.get("/users")

    # Then
    assert 200 == response.status_code
    assert expected_response == response.json


def test_delete_existing_user(test_client):
    # Given
    user_id_to_delete = 1
    expected_body = {
        "message": "User deleted successfully"
    }

    # When
    response = test_client.delete(f'/users/{user_id_to_delete}')

    # Then
    assert expected_body == response.json


def test_delete_already_deleted_user(test_client):
    # Given
    user_id_to_delete = 1
    expected_body = {
        "message": "User not deleted successfully"
    }

    # When
    response = test_client.delete(f'/users/{user_id_to_delete}')

    # Then
    assert expected_body == response.json


def test_delete_not_existing_user(test_client):
    # Given
    user_id_to_delete = 70
    expected_body = {
        "message": "User not deleted successfully"
    }

    # When
    response = test_client.delete(f'/users/{user_id_to_delete}')

    # Then
    assert expected_body == response.json


def test_get_users_after_delete(test_client):
    # Given
    expected_response = [
        {
            "user_id": 2,
            "username": "amine",
            "full_name": "Amine Haj Ali"
        }
    ]

    # When
    response = test_client.get("/users")

    # Then
    assert 200 == response.status_code
    assert expected_response == response.json
