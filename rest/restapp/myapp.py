import requests
import json

URL="http://127.0.0.1:8000/stureg/"

data={
    "name":"Pratik",
    "roll": "1",
    "city":"Nashik",
}

json_data=json.dumps(data)
r=requests.post(url=URL, data=json_data)
data=r.json
print(data)