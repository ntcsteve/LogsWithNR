import json
import requests

# Endpoint for New Relic Log API
url = "https://log-api.newrelic.com/log/v1"

# Headers to include the content-type and Api-Key
headers = {
    'Content-type': 'application/json', 
    'Api-Key': 'INGEST_KEY'
    }

# Loading the JSON file
with open('./sampleWorkshop.json') as file:
    sampleLogs = json.load(file)

# Post request to the url with the sampleLogs data and headers
response = requests.post(url, json=sampleLogs, headers=headers)