import requests

STATIC_MAPS_KEY = ''
GEOCODE_MAPS_KEY = ''


def find_ll_spn(geocoder_api_server, geocoder_params):
    response = requests.get(geocoder_api_server, params=geocoder_params)
    if not response:
        return None, None
    json_response = response.json()
    geo_object = json_response["response"]["GeoObjectCollection"]["featureMember"][0]['GeoObject']
    upperCorner = geo_object["boundedBy"]["Envelope"]['upperCorner']
    lowerCorner = geo_object["boundedBy"]["Envelope"]['lowerCorner']
    lon1, lat1 = map(float, lowerCorner.split())
    lon2, lat2 = map(float, upperCorner.split())
    spn = ','.join(map(str, [abs(lon1 - lon2), abs(lat1 - lat2)]))
    ll = ','.join(geo_object["Point"]["pos"].split(" "))
    return spn, ll


def make_map(server_address_maps, maps_params):
    response = requests.get(server_address_maps, maps_params)
    if not response:
        return None
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    return map_file
