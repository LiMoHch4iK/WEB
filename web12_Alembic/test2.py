from requests import get, post, delete

# print(get('http://localhost:8080/api/v2/news').json())
# print(get('http://localhost:8080/api/v2/news/1').json())
# print(get('http://localhost:8080/apinews/999').json())
# print(get('http://localhost:8080/api/v2/news/q').json())

# print(post('http://localhost:8080/api/v2/news', json={}).json())
#
# print(post('http://localhost:8080/api/news',
#            json={'title': 'Заголовок'}).json())
#
# print(post('http://localhost:8080/api/v2/news',
#            json={'title': 'Заголовок',
#                  'content': 'Используйте flask-result',
#                  'user_id': 2,
#                  'is_private': False}).json())

# print(delete('http://localhost:8080/api/v2/news/999').json())
# # новости с id = 999 нет в базе

print(delete('http://localhost:8080/api/v2/news/6').json())