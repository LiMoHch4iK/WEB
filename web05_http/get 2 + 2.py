import requests


search_api_server = input()
port = input()
a, b = input(), input()
params = {
    "a": a,
    "b": b
}
response = requests.get(f'{search_api_server}:{port}', params=params)
json_response = response.json()
check = json_response['check']
res = json_response['result']
res.sort()
print(*res)
print(check)
