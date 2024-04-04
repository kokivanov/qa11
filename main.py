import requests
import allure


@allure.description("Перевірка отримання даних про конкретного користувача за допомогою API ендпоінту SINGLE USER")
def test_single_user():
    with allure.step("Відправка запиту на отримання даних користувача"):
        response = requests.get("https://reqres.in/api/users/2")
        assert response.status_code == 200
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'

    with allure.step("Перевірка вмісту відповіді"):
        assert 'data' in response.json()
        assert response.json()['data']['id'] == 2


@allure.description("Перевірка можливості створення нового користувача за допомогою API ендпоінту CREATE")
def test_create_user():
    user_data = {
        "name": "morpheus",
        "job": "leader"
    }
    with allure.step("Відправка запиту на створення нового користувача"):
        response = requests.post("https://reqres.in/api/users", json=user_data)
        assert response.status_code == 201
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'

    with allure.step("Перевірка вмісту відповіді"):
        response_json = response.json()
        assert 'id' in response_json
        assert response_json['name'] == user_data['name']
        assert response_json['job'] == user_data['job']


@allure.description("Перевірка оновлення даних користувача за допомогою API ендпоінту UPDATE")
def test_update_user():
    user_data = {
        "name": "morpheus",
        "job": "zion resident"
    }
    with allure.step("Відправка запиту на оновлення даних користувача"):
        response = requests.put(
            "https://reqres.in/api/users/2", json=user_data)
        assert response.status_code == 200
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'

    with allure.step("Перевірка вмісту відповіді"):
        response_json = response.json()
        assert response_json['name'] == user_data['name']
        assert response_json['job'] == user_data['job']


@allure.description("Перевірка видалення користувача за допомогою API ендпоінту DELETE")
def test_delete_user():
    with allure.step("Відправка запиту на видалення користувача"):
        response = requests.delete("https://reqres.in/api/users/2")
        assert response.status_code == 204

    with allure.step("Перевірка відсутності вмісту в відповіді"):
        assert response.text == ''
