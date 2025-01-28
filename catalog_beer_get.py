import os
import requests
import json

import requests

url = "https://api.catalog.beer/beer"

headers = {'Accept': 'application/json', 'Authorization': 'Basic ' + 'ZTFmMDhlY2EtYzUyMi00ZWY3LWI0NjQtOGU5MWQwMTBjNTUzOg=='}

response = requests.get(url, headers=headers).json()


# while response['has_more']:
#     with open(f'beer_names.txt', 'a') as f:
#         for beer in response['data']:
#             f.write(beer['id'] + '\n')
#     params = {'cursor': response['next_cursor']}
#     response = requests.get(url, headers=headers, params=params).json()

with open(f'beer_names.txt', 'r') as f:
    beers = f.readlines()
    beerset = set([n[:-4] for n in os.listdir('data/catalog_beer')])
    for beer in beers:
        if beer in beerset:
            continue
        beer = beer.strip()
        response = requests.get(f'{url}/{beer}', headers=headers).json()
        with open(f'data/catalog_beer/{beer}.json', 'w') as f:
            del response['brewer']
            del response['brewer_verified']
            json.dump(response, f, indent=2)


