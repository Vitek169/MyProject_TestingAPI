from utils.http_methods import HttpMethods

"""Методы для тестирования Google maps api"""

base_url ='https://rahulshettyacademy.com' # Базовая URL
key = '?key=qaclick123' # Параметры для всех запросов
class GoogleMapsApi():

    """Метод для создания новой локации"""
    @staticmethod
    def create_new_place():

        json_for_create_new_place = {

            "location": {
            "lat": -38.383494,
            "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
             "shoe park",
            "shop"
             ],
             "website": "http://google.com",
             "language": "French-IN"
        }

        post_resource = "/maps/api/place/add/json" # Ресурс метода POST
        post_url = base_url + post_resource + key
        print(post_url)
        result_post = HttpMethods.post(post_url, json_for_create_new_place)
        print(result_post.text)
        return result_post

    """Метод для проверки новой локации"""

    @staticmethod
    def get_new_place(place_id):

        get_resource = "/maps/api/place/get/json" #Ресурс метода GET
        get_url = base_url + get_resource + key + '&place_id=' + place_id
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        return result_get


    """Метод для изменения новой локации"""

    @staticmethod
    def put_new_place(place_id):
        put_resource = '/maps/api/place/update/json' # Ресурс метда PUT
        put_url = base_url + put_resource + key
        print(put_url)
        json_for_update_new = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        result_put = HttpMethods.put(put_url, json_for_update_new)
        print(result_put)
        return result_put



        """Метод для удаления новой локации"""

    @staticmethod
    def delete_new_place(place_id):
        delete_resource = '/maps/api/place/delete/json' # Ресурс метда PUT
        put_url = base_url + delete_resource + key
        print(put_url)
        json_for_delete_new = {
            "place_id": place_id
        } 
        result_delete = HttpMethods.delete(put_url, json_for_delete_new)
        print(result_delete)
        return result_delete