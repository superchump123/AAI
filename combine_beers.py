import json
import os

with open('data/big_beer_list/beers.json', 'x') as f:
    beerfiles = os.listdir('data/catalog_beer')
    master_data = dict()
    for file in beerfiles:
        with open('data/catalog_beer/' + file, 'r') as b:
            try:
                jsondata = json.load(b)
            except:
                continue
        try:
            if jsondata['description'] is not None:  
                master_data[jsondata['id']] = jsondata
                print(jsondata['name'])
        except KeyError:
            continue
    json.dump(master_data, f, indent=3)
    

