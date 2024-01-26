"""Методы для проверки ответов нащих запосов"""
import json


class Checking():

    """Метод для проверки статуса кода"""
    @staticmethod
    def check_status_code(result, status_code):
        assert  status_code == result.status_code
        print(f"Успешно!!! Статус код = {result.status_code}")

    """Метод для проверки наличия обязателных полей в ответе запроса"""
    @staticmethod
    def check_json_token(result, exprcted_velue):
        token = json.loads(result.text)
        assert list(token) == exprcted_velue
        print("Все поля присутсвуют")