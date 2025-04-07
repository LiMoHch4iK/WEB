import os
import sys

import pygame
import requests

server_address = 'http://geocode-maps.yandex.ru/1.x/?'
api_key = '40d1649f-0493-4b70-98ba-98533de7710b'
geocode = 'Астралия'
geocoder_request = f'{server_address}apikey={api_key}&geocode={geocode}&format=json'
response = requests.get(geocoder_request)
json_response = response.json()
# print(json_response)
lowerCorner = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["boundedBy"]["Envelope"]["lowerCorner"]
upperCorner = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["boundedBy"]["Envelope"]["upperCorner"]
ll1 = list(map(float, lowerCorner.split()))
ll2 = list(map(float, upperCorner.split()))
spn = ','.join(map(str, (abs(ll1[0] - ll2[0]), abs(ll1[1] - ll2[1]))))
ll = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
ll = ','.join(ll.split())
# print(spn)
# print(ll)
#https://static-maps.yandex.ru/v1?lang=ru_RU&ll=37.621202,55.753544&spn=0.02,0.02&apikey=ef67d706-4387-4517-8b08-50f4c0929dd7
server_address_maps = 'https://static-maps.yandex.ru/v1?'
api_key_maps = 'ef67d706-4387-4517-8b08-50f4c0929dd7'
static_maps_request = f'{server_address_maps}lang=ru_RU&ll={ll}&spn={spn}&apikey={api_key_maps}'
response = requests.get(static_maps_request)

map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((600, 450))
# Рисуем картинку, загружаемую из только что созданного файла.
screen.blit(pygame.image.load(map_file), (0, 0))
# Переключаем экран и ждем закрытия окна.
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
os.remove(map_file)