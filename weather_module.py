import requests
from config import WEATHER_API_KEY

'''
Data comes from Openweather like this:
{"coord":{"lon":77.2167,"lat":28.6667},"weather":[{"id":721,"main":"Haze","description":"haze","icon":"50n"}],"base":"stations","main":{"temp":292.2,"feels_like":291.7,"temp_min":292.2,"temp_max":292.2,"pressure":1011,"humidity":59,"sea_level":1011,"grnd_level":986},"visibility":1800,"wind":{"speed":2.57,"deg":110},"clouds":{"all":20},"dt":1768739075,"sys":{"type":1,"id":9165,"country":"IN","sunrise":1768700671,"sunset":1768738674},"timezone":19800,"id":1273294,"name":"Delhi","cod":200}
'''

def get_weather(city="bihar"):
    try:
        
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json() 

        if data["cod"] != 200:
            return f"Sorry, I couldn't find weather details for {city}."

        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        weather_desc = data["weather"][0]["description"]

        return (f"Weather in {city}: {weather_desc}. "
                f"Temperature is {temp}°C, feels like {feels_like}°C, "
                f"humidity {humidity} percent.")
    except:
        return "Sorry, weather service is not responding."
