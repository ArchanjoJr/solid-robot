import requests as re
from delete import *
import pprint
import json
import sys

langs = ['en-US', 'de-DE', 'es-ES', 'es-MX', 'fr-FR', 'it-IT', 'ja-JP', 'pl-PL', 'pt-BR', 'ru-RU']
index = 0
if len(sys.argv) > 0:
    if sys.argv[1] in langs:
        index = langs.index(sys.argv[1])
print("Getting a JSON for the " + langs[index] + " indexuage")

url = 'https://api.gwentapi.com/v0/cards'
print('Getting the Amount of Cards of Database')
pag = re.get(url)
if pag.status_code != 200:
    print(pag.status_code)
else:
    limit = pag.json()['count']

url += "?limit=" + str(limit) + '&index=' + langs[index]

pag = re.get(url)
if pag.status_code != 200:
    print(pag.status_code)
else:
    with open('aux.json', 'w') as arquivo:
        arquivo.write(json.dumps(pag.json()["results"]))

size = limit
aux = json.load(open('aux.json', 'r'))
file = open('cards.json', 'w')
file.write('['), file.close()
for i in range(size):
    print("Making the request for : " + aux[i]['name'])
    cart = re.get(aux[i]['href'])
    with open("cards.json", 'a')as file:
        if i < (size - 1):
            print("Writing the request for : " + aux[i]['name'] + " in file.")
            file.write(json.dumps(cart.json()) + ",")
        else:
            print("Writing the request for : " + aux[i]['name'] + " in file.")
            file.write(json.dumps(cart.json()) + "]")

cartas = json.load(open('cards.json', 'r'))
file = open('variations.json', 'w')
file.write('['), file.close()
for i in range(size):
    print('Getting Variations for: ' + cartas[i]['name'])
    var = re.get(cartas[i]['variations'][0]['href'])
    with open('variations.json', 'a') as file:
        if i < (size - 1):
            print('writing variations for :' + cartas[i]['name'])
            file.write(json.dumps(var.json()) + ',')
        else:
            print('writing variations for :' + cartas[i]['name'])
            file.write(json.dumps(var.json()) + ']')
print('CLEANING THE THE JSONS')
clean_cards('cards.json')
clean_variations('variations.json')
delete('aux.json')
print('Done!')
