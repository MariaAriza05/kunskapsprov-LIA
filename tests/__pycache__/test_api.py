import requests

def test_api_response():
    base_url = "https://test-379574553568.us-central1.run.app/"
    headers = {
        "api-key": "maria-1234"
    }

    response = requests.get(base_url, headers=headers)

    # 1. API svarar
    assert response.status_code == 200

    # 2. Svaret är JSON
    data = response.json()
    assert isinstance(data, dict)

    # 3. Kontrollera att API:et returnerar något vettigt
    assert "message" in data or "status" in data
