import requests


resp = requests.get('http://localhost:5050/api/v1/advs/').json()
print(resp)


resp = requests.post('http://localhost:5050/api/v1/advs/',
                          json={"owner": "Test",
                                "name": "test",
                                "description": "test"})
print(resp)



resp = requests.get('http://localhost:5050/api/v1/adv/1').json()
print(resp)


response = requests.put('http://localhost:5050/api/v1/adv/1', json={"name": "name", "description": "description"})
print(response)

#Try DELETE by id
response = requests.delete('http://localhost:5050/api/v1/adv/3')
print(response)