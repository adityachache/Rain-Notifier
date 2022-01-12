import requests
from twilio.rest import Client

# YOUR COORDINATES
MY_LAT = 19.199485
MY_LONG = 72.968055

# Twilio Info
account_sid = "YOUR TWILIO ACCOUNT_SID"
auth_token = "YOUR TWILIO ACCOUNT AUTH_TOKEN"


# OPENWEATHERMAP API_KEY
AUTH_KEY = "YOUR OPENWEATHERMAP API_KEY"

UNIT = "metric"

parameters = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'appid': AUTH_KEY,
    'units': UNIT,
    'exclude': "current,minutely,daily"
}

response = requests.get(url='https://api.openweathermap.org/data/2.5/onecall', params=parameters)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)

hourly_weather_data = weather_data['hourly']
# print(hourly_weather_data)

current_weather = ''

is_going_to_rain = False
for hour in range(13):
    weather_id = hourly_weather_data[hour]['weather'][0]['id']
    # print(type(weather_id))
    if weather_id < 700:
        current_weather = hourly_weather_data[hour]['weather'][0]['main']
        is_going_to_rain = True

if is_going_to_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(body=f"Bring an Umbrella.\nThere will be {current_weather} Today.",
                                     from_='TWILIO VIRTUAL PHONE NUMBER',
                                     to='YOUR TWILIO REGISTERED PHONE NUMBER')
    print(message.status)

