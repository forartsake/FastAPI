def test_auth_with_valid_token(token, test_client):
    headers = {"Authorization": f"Bearer {token}"}
    response = test_client.get("stats/26", headers=headers)
    assert response.status_code == 200


def test_auth_with_invalid_token(invalid_token, test_client):
    headers = {"Authorization": f"Bearer {invalid_token}"}
    response = test_client.get("stats/1", headers=headers)

    assert response.status_code == 401


def test_get_stats_by_owner(token, test_client):
    headers = {"Authorization": f"Bearer {token}"}
    response = test_client.get("stats/26", headers=headers)
    assert response.status_code == 200


def test_get_stats_by_not_owner(token, test_client):
    headers = {"Authorization": f"Bearer {token}"}
    response = test_client.get("stats/1", headers=headers)
    assert response.status_code == 403
