import requests

# получим API_KEY после регистрации на сайте источника и верификации по эл. почте
API_KEY = "ff26c39c713dc6c5f738cb2d1fd3aa87"

#
response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q=Moscow&appid={API_KEY}')

print(response.json())
