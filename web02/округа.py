import requests

server_address = 'http://geocode-maps.yandex.ru/1.x/?'
api_key = '40d1649f-0493-4b70-98ba-98533de7710b'
geocodes = ['Хабаровск', 'Уфа', 'Нижний Новгород', 'Калининград']
# geocode = 'Исторический музей Москва красная площадь 1'
# Готовим запрос.
for geocode in geocodes:
    geocoder_request = f'{server_address}apikey={api_key}&geocode={geocode}&format=json'

    # Выполняем запрос.
    response = requests.get(geocoder_request)
    if response:
        # Запрос успешно выполнен, печатаем полученные данные.
        json_response = response.json()
        # print(json_response)
        # Получаем первый топоним из ответа геокодера.
        # Согласно описанию ответа, он находится по следующему пути:
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        # Полный адрес топонима:
        toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][1]["name"]
        print(f'{geocode} - {toponym_address}')
    else:
        # Произошла ошибка выполнения запроса. Обрабатываем http-статус.
        print("Ошибка выполнения запроса:")
        print(geocoder_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")