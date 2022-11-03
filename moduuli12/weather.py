import requests
import json
hakusana = input(f'Kaupunki: ')
pyyntö = 'https://api.openweathermap.org/data/2.5/weather?q=' + hakusana + '&appid=b506dbf5aa172758d111318ced349bb3&units=metric'

vastaus = requests.get(pyyntö).json()

json_vastaus = json.dumps(vastaus, indent=2)
print(f'Weather:\n {vastaus["weather"][0]["description"]}')

print(f'Temp:\n {vastaus["main"]["temp"]}°C')
