import requests as re
import pprint
import json

url = 'https://api.gwentapi.com/v0/cards'
pag = re.get(url)
if pag.status_code != 200:
    print(pag.status_code)
else:
    limit = pag.json()['count']

url += "?limit=" + str(limit)

pag = re.get(url)
if pag.status_code != 200:
    print(pag.status_code)
else:
    with open('aux.json','w') as arquivo:
        arquivo.write(json.dumps(pag.json()["results"]))

aux = json.load(open('aux.json','r'))
pprint.pprint(aux[77]['name'])