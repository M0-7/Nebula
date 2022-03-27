import nextcord
import datetime
from config import dark_orange

key_features = {
    'temp': 'Temperature',
    'feels_like' : 'Feels Like',
    'temp_min' : 'Minimum Temperature',
    'temp_max' : 'Maximum Temperature'
}

def parse_data(data):
    data = data['main']
    del data['humidity']
    del data['pressure']
    return data 
    
def weather_message(data, location):
    location = location.title()
    message = nextcord.Embed(title=f"{location}'s current Weather",description = f"Here is the weather data for {location}",color = dark_orange, timestamp = datetime.datetime.utcnow())
    for key in data:
        message.add_field(name=key_features[key], value=str(data[key]), inline=False)
    return message


    
