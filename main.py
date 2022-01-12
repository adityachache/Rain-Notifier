import requests
from twilio.rest import Client

# Home Coordinates
MY_LAT = 19.199485
MY_LONG = 72.968055

# Twilio Info
account_sid = "ACdb1ebbfe1625fcda5b5e5eb0a31c8035"
auth_token = "649f038544507acaf487c8da2f257bdd"

# Test Coordinates Rio De Janeiro
# MY_LAT = -22.906847
# MY_LONG = -43.172897

AUTH_KEY = "bd79b3023b97c23199a5b0543d86b12d"

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
                                     from_='+18502045510',
                                     to='+917977191236')
    print(message.status)

