import requests


def request(query, variables):
    request = requests.post('https://wellzesta-health-proxy-stg.herokuapp.com/graphql', json={'query': query, 'variables': variables}, headers={'api-key': 'token ny3oTYMz8kNEtk8o9dqGo8Xk'})
    return request.json()
