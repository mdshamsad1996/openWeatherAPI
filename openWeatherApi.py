import requests
from pprint import pprint
city = input("Enter your city: ")

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=261a4b36f6cfb0dcf3260f99168cf499&units=metric'.format(city)

res = requests.get(url)

data = res.json()
temp = data['main']['temp']
windSpeed = data['wind']['speed']
latitude = data['cord']['lat']
longitude = data['weather'][0]['description']
pprint(data)