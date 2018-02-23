import requests as req
import json

api_key = 345964136b71eed7c4385662c1cd7cc7

url = 'http://api.openweathermap.org/data/2.5/forecast?id=5308655&APPID='

response = req.get(url).json()


print(response)