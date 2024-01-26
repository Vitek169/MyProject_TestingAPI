import json

from requests import Response
from utils.Checking import Checking
from utils.api import GoogleMapsApi

"""Создание, изменение, удаление новой локации"""
class TestCreatePlace():

    def test_create_new_place(self):

        print("Метод POST")
        result_post = GoogleMapsApi.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post, 200)
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        # token = json.loads(result_post.text) # Код для получения результато всех полей, чтоб не писать с документауии вручную
        # print(list(token)) # Код для получения результато всех полей, чтоб не писать с документауии вручную

        print('Метод GET POST')
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get,['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        # token = json.loads(result_get.text) # Код для получения результато всех полей, чтоб не писать с документауии вручную
        # print(list(token)) # Код для получения результато всех полей, чтоб не писать с документауии вручную



        print('Метод PUT')
        result_put = GoogleMapsApi.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['msg'])

        print('Метод GET PUT')
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get,['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website','language'])

        print('Метод DELETE')
        result_delete = GoogleMapsApi.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ['status'])


        print('Метод GET DELETE')
        result_get = GoogleMapsApi.delete_new_place(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get, ['msg'])

        print('Тестирование создание, изменение, удаление новой локации, прошло успешно!!!')

