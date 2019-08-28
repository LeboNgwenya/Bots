import requests


def request(query, variables):
    request = requests.post('*****Link*****', json={'query': query, 'variables': variables}, headers={'api-key': 'token'})
    return request.json()
