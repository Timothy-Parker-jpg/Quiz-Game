import requests
import json
paramaters = {
    "amount": 10,
    "type": "boolean"
}
r = requests.get(url="https://opentdb.com/api.php", params=paramaters)
r.raise_for_status()
question_data = r.json()["results"]
