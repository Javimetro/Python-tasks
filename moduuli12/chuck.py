import requests
import json
pyynto = 'https://api.chucknorris.io/jokes/random'

vastaus = requests.get(pyynto).json()


print(vastaus['value'])