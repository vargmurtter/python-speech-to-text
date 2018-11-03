import requests
import json

# INSERT YOUR LUIS ENDPOINT URL HERE *it's example URL*
API_ENDPOINT = "https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/ee2f2869-98d2-476a-9559-cc8389609427?subscription-key=8bf34f219a6140b0a4f9c632f44d7d0d&timezoneOffset=-360&q="

def get_command(command):
	r = requests.get(API_ENDPOINT + command)
	data = json.loads(r.text)
	return data['topScoringIntent']['intent']
