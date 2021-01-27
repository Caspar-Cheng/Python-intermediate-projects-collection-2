import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {"https": os.environ["https_proxy"]}

# Use OpenWeather One Call API to get Brisbane's weather data, only get hourly weather data back
api_key = "Your_open_weather_API"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall?"
account_sid = os.environ["Twilio account sid"]
auth_token = os.environ["Twilio auth token"]

parameters = {
    "lat": -27.469770,
    "lon": 153.025131,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()

# Slice the data to choose only 12 hours weather data
predicted_weather = data["hourly"][: 11]

will_rain = False
# Use for loop to see whether it will rain in next 12 hours, condition_code is checked through API docs
for hour_data in predicted_weather:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

# Print out reminder message
if will_rain:
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today, remember to bring an UMBRELLA~!",
        from_='+13072889180',
        to='+61432500916'
    )
    print(message.status)
