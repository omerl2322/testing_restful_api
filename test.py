import requests

BASE = 'http://127.0.0.1:5000/'

response = requests.put(BASE + "video/4", {"likes": 10, "name": "omer", "views": 1000})
print(response.json())
input()
response = requests.get(BASE + "video/4")
print(response.json())