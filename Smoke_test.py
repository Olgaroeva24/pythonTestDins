import pytest
import requests

class TestSmoke:
    data = [
        {
            "id": "1",
            "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        },
        {
            "id": "10",
            "title": "optio molestias id quia eum",
        },
        {
            "id": "100",
            "title": "at nam consequatur ea labore ea harum",
        }
    ]

    @pytest.mark.parametrize('data', data)
    def test_status_code_equals_200(self, data):
        url = "https://jsonplaceholder.typicode.com/posts?userId"
        params = {'data': data}
        response = requests.get(url, params=params)
        print(response.status_code)
        assert response.status_code == 200, f"response.status_code is not 200"

    def test_body_is_correct_type(self, data):
        url = "https://jsonplaceholder.typicode.com/posts?userId"
        params = {'data': data}
        response = requests.get(url, params=params)
        response_body = response.json()
        assert "id" in response_body,f"id is not in response"
        assert "title" in response_body,f"title is not in response"
        # check type response.body
        assert type(response_body) == list

    def test_body_is_correct_type(self):
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        response_body = response.json()
        assert type(response_body["id"]) == int
        assert type(response_body["title"]) == str
        assert type(response_body["userId"]) == int
        assert type(response_body["body"]) == str

