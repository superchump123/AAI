import json
import requests
import string

query = 'https://thecocktaildb.com/api/json/v1/1/search.php?f='

for char in string.ascii_lowercase + string.digits:
    response = requests.get(query + char)
    data = response.json()
    with open(f'{char}_drinks.json', 'x') as f:
        json.dump(data, f, indent=2)

