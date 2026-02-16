import requests

def test_find_available_pets_returns_list():
    base_url = "https://petstore.swagger.io/v2/pet/findByStatus"
    params = {"status": "available"}

    response = requests.get(base_url, params=params)

    # 1. API svarar
    assert response.status_code == 200

    # 2. Svaret är JSON och en lista
    data = response.json()
    assert isinstance(data, list)

    # 3. Det ska inte vara tom minnst 1 pet i listan
    assert len(data) > 0

