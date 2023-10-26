import requests

PARAMETERS = {
    "amount": 10,
    "type": "boolean",
    "category": 18
}

range_value = PARAMETERS["amount"]

response = requests.get(url="https://opentdb.com/api.php", params=PARAMETERS)
response.raise_for_status()
data = response.json()
question_data = data["results"]

