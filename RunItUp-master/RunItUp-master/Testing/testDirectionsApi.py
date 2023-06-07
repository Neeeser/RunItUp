
import requests
import json

url = "https://maps.googleapis.com/maps/api/directions/json?origin=Toronto&destination=Montreal&key=AIzaSyA-BRYsxwC4d1mNlFOwwjJtaQI9HGLm5u0"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

with open('directionsDump.json','w') as fp:
    json.dump(response, fp)