import requests
import json


def get_joke():
	response = requests.get(
	    "https://v2.jokeapi.dev/joke/Any?blacklistFlags=religious")
	json_data = json.loads(response.text)
	setup = json_data["setup"]
	punchline = json_data["delivery"]
	return setup, punchline