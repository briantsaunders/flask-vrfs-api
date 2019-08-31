# import third party libs
import pytest

# test /vrfs endpoints

def test_get_vrfs(client):
    """
    """
    response = client.get("/api/vrfs")
    assert response.status_code == 200


def test_post_invalid_vrfs(client):
    """
    """
    parameters = {}
    response = client.post("/api/vrfs", query_string=parameters)
    json_data = response.get_json()
    assert "name" in json_data["error"]
    assert "table" in json_data["error"]
    assert response.status_code == 422


def test_post_vrfs(client):
    """
    """
    parameters = {"name": "test_vrf", "table": 20}
    response = client.post("/api/vrfs", query_string=parameters)
    json_data = response.get_json()
    assert json_data["name"] == parameters["name"]
    assert json_data["table"] == parameters["table"]
    assert "vrf_id" in json_data
    assert response.status_code == 200

# test /vrfs/<vrf_id> endpoints

def test_get_vrf(client):
    """
    """
    vrfs_response = client.get("/api/vrfs")
    for vrf in vrfs_response.get_json():
        vrf_id = vrf["vrf_id"]
        response = client.get(f"/api/vrfs/{vrf_id}")
        json_data = response.get_json()
        assert "vrf_id" in json_data
        assert "name" in json_data
        assert "table" in json_data
        assert response.status_code == 200


def test_get_invalid_vrf(client):
    """
    """
    response = client.get("/api/vrfs/100")
    assert response.status_code == 400


def test_delete_vrf(client):
    """
    """
    vrfs_response = client.get("/api/vrfs")
    for vrf in vrfs_response.get_json():
        vrf_id = vrf["vrf_id"]
        response = client.delete(f"/api/vrfs/{vrf_id}")
        json_data = response.get_json()
        assert json_data == {}
        assert response.status_code == 200
