import requests

def test_api_server_status():
    url = "https://httpbin.org"
    response = requests.get(url)
    assert response.status_code == 200
    print("Тест пройден успешно!")

test_api_server_status()
