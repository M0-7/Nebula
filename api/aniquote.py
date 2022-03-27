import requests
import pprint

url = "https://animechan.vercel.app/api/random"
data = requests.get(url).json()

pprint.pprint(data)

character = data['character']
quote = data['quote']