# Base Dependencies
# -----------------
from typing import Any
from uuid import UUID, uuid1

# FastAPI Dependencies
# --------------------
from fastapi.testclient import TestClient

# Local Dependencies
# ------------------
from .conf import app, test_db


client = TestClient(app)

# Auxiliar Functions
# ------------------
def is_valid_uuid(value: Any):
    """Determine if a value is a valid UUID"""
    try:
        UUID(str(value))

        return True
    except ValueError:
        return False


# Tests
# --------------

# -- Users --
def test_list_all_users_empty(test_db):
    response = client.get("/users/")

    assert response.status_code == 200
    assert response.json() == []


def test_list_all_users(test_db):

    the_wire_users = ["John", "Mary", "Johannes"]
    breaking_bad_users = ["Pablo", "Peter", "James"]

    for name in the_wire_users:
        client.post("/users", params={"name": name, "favorite_tv_show": "the_wire"})

    for name in breaking_bad_users:
        client.post("/users", params={"name": name, "favorite_tv_show": "breaking_bad"})

    response = client.get("/users/")
    all_users = response.json()

    assert response.status_code == 200
    for user in all_users:
        assert is_valid_uuid(user["id"])
        assert (user["name"] in the_wire_users) or (user["name"] in breaking_bad_users)
        assert user["favorite_tv_show"] in ["the_wire", "breaking_bad"]


def test_list_users_tv_show(test_db):

    the_wire_users = ["John", "Mary", "Johannes"]
    breaking_bad_users = ["Pablo", "Peter", "James"]

    for name in the_wire_users:
        client.post("/users/", params={"name": name, "favorite_tv_show": "the_wire"})

    for name in breaking_bad_users:
        client.post(
            "/users/", params={"name": name, "favorite_tv_show": "breaking_bad"}
        )

    response = client.get("/users/", params={"favorite_tv_show": "the_wire"})
    all_users = response.json()

    assert response.status_code == 200
    for user in all_users:
        assert is_valid_uuid(user["id"])
        assert (user["name"] in the_wire_users) and (
            user["name"] not in breaking_bad_users
        )
        assert user["favorite_tv_show"] == "the_wire"


def test_list_users_tv_show_invalid(test_db):
    response = client.get("/users/", params={"favorite_tv_show": "dexter"})

    assert response.status_code == 422


def test_create_user(test_db):
    user = {"name": "James", "favorite_tv_show": "breaking_bad"}
    response = client.post("/users/", params=user)
    data = response.json()

    assert response.status_code == 200
    assert data["name"] == user["name"]
    assert data["favorite_tv_show"] == user["favorite_tv_show"]
    assert is_valid_uuid(data["id"])


def test_create_user_tv_show_wrong(test_db):
    user = {"name": "Jane", "favorite_tv_show": "game_of_thrones"}
    response = client.post("/users/", params=user)

    assert response.status_code == 422


def test_get_user(test_db):
    # create a user
    user = {"name": "Peter", "favorite_tv_show": "breaking_bad"}
    post_response = client.post("/users/", params=user)

    id = post_response.json()["id"]

    # get the created user
    response = client.get("/users/{}".format(id))
    assert response.status_code == 200
    assert response.json() == post_response.json()


def test_get_user_not_found(test_db):
    random_id = uuid1()
    response = client.get("/users/{}".format(random_id))
    assert response.status_code == 404


def test_update_user_user_name(test_db):
    user = {"name": "Tobias", "favorite_tv_show": "breaking_bad"}

    # create user
    response = client.post("/users/", params=user)
    data = response.json()
    user_id = data["id"]

    assert response.status_code == 200

    # udpate user's name
    user["name"] = "Tobias Hank"
    response = client.put("/users/{}".format(user_id), params=user)
    data = response.json()
    assert response.status_code == 200

    # get user
    response = client.get("/users/{}".format(user_id))
    data = response.json()
    assert response.status_code == 200
    assert data["id"] == user_id
    assert data["name"] == user["name"]
    assert data["favorite_tv_show"] == user["favorite_tv_show"]


def test_update_user_tv_show(test_db):
    user = {"name": "Brad", "favorite_tv_show": "the_wire"}

    # create user
    response = client.post("/users/", params=user)
    data = response.json()
    user_id = data["id"]

    assert response.status_code == 200

    # udpate user's name
    user["favorite_tv_show"] = "breaking_bad"
    response = client.put("/users/{}".format(user_id), params=user)
    data = response.json()
    assert response.status_code == 200

    # get user
    response = client.get("/users/{}".format(user_id))
    data = response.json()
    assert response.status_code == 200
    assert data["id"] == user_id
    assert data["name"] == user["name"]
    assert data["favorite_tv_show"] == user["favorite_tv_show"]


def test_update_user_name_tv_show(test_db):
    user = {"name": "Ben", "favorite_tv_show": "the_wire"}

    # create user
    response = client.post("/users/", params=user)
    data = response.json()
    user_id = data["id"]
    assert response.status_code == 200

    # udpate user's name
    user["name"] = "Ben Junior"
    user["favorite_tv_show"] = "breaking_bad"
    response = client.put("/users/{}".format(user_id), params=user)
    data = response.json()
    assert response.status_code == 200

    # get user
    response = client.get("/users/{}".format(user_id))
    data = response.json()
    assert response.status_code == 200
    assert data["id"] == user_id
    assert data["name"] == user["name"]
    assert data["favorite_tv_show"] == user["favorite_tv_show"]


def test_update_user_not_found(test_db):
    random_id = uuid1()
    response = client.put("/users/{}".format(random_id), params={"name": "Jimmy"})

    assert response.status_code == 404


def test_delete_user(test_db):
    user = {"name": "Charles", "favorite_tv_show": "the_wire"}

    # create user
    response = client.post("/users/", params=user)
    data = response.json()
    user["id"] = data["id"]
    assert response.status_code == 200

    # delete user
    response = client.delete("/users/{}".format(user["id"]))
    assert response.status_code == 200

    # user not found
    response = client.get("/users/{}".format(user["id"]))
    assert response.status_code == 404


def test_delete_not_found(test_db):
    random_id = uuid1()
    response = client.delete("/users/{}".format(random_id))
    assert response.status_code == 404
