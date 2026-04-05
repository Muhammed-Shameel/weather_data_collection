import requests
import pandas as pd
import time

api_key = "149a2890c31e44a9b6c60239260504"
c = "tirur"


all_data = []

for i in range(5):
  url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={c}"
  data = requests.get(url).json()
  weather_data = {
      "City" : data['location']['name'],
      'Time' : data['location']['localtime'],
      'Day/Night' : "Day" if data['current']["is_day"] == 1 else "Night" ,
      'Temperature' : data['current']['temp_c'],
      'Feels Like' : data['current']['feelslike_c'],
      "condition": data["current"]["condition"]["text"],
      'Humidity' : data['current']['humidity'],
      'Wind Speed Km/H' : data['current']['wind_kph']
  }

  all_data.append(weather_data)
  time.sleep(8)

df = pd.DataFrame(all_data)

print(df)


