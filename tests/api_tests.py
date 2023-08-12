import pprint

import requests

#
# response = requests.post('http://127.0.0.1:8000/auth/register/', json={
#     'username': 'user',
#     'password': '123',
#     'name': 'Josh',
#     'surname': 'Vurgh',
#     'age': 18
#  })

access_token = requests.post('http://127.0.0.1:8000/auth/login/', json={
    'username': 'user',
    'password': '123'
}).json()['access_token']

# response = requests.get('http://127.0.0.1:8001/notes/create?note_text=Hello!', headers={
#     'Authorization': 'Bearer %s' % access_token
# })

# response = requests.get('http://127.0.0.1:8001/notes/get/', headers={
#     'Authorization': 'Bearer %s' % access_token
# })

response = requests.get(
    'http://127.0.0.1:8001/notes/note/get?note_id=2', headers={
    'Authorization': 'Bearer %s' % access_token
})

pprint.pprint(response.json())
