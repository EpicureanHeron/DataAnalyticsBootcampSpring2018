import requests as req
import json

user_num = input("What number would you like to learn about? ")

user_type = input("What type of ")

url = "http://numbersapi.com/" + user_num + "/trivia?json"

response = req.get(url).json()

print("Fun Fact about the number " + str(response['number']) + ": \n" + response['text'])