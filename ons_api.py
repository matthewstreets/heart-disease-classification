import json
import requests

reply = requests.get('https://api.beta.ons.gov.uk/v1/datasets')

data = reply.json()

with open('ons.json', 'w') as file:
    json.dump(data, file)
