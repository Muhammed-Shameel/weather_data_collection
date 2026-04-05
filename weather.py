import requests
import pandas as pd
import os

api_key = os.getenv("API_KEY")
c = "tirur"

url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={c}"
data = requests.get(url).json()

# 🔥 Handle API errors
if "error" in data:
    print("API Error:", data["error"]["message"])
    exit()

weather_data = {
    "City": data['location']['name'],
    "Country": data['location']['country'],
    "Latitude": data['location']['lat'],
    "Longitude": data['location']['lon'],
    
    "Time": data['location']['localtime'],
    "Day/Night": "Day" if data['current']["is_day"] == 1 else "Night",

    "Temperature": data['current']['temp_c'],
    "Feels Like": data['current']['feelslike_c'],
    "Humidity": data['current']['humidity'],
    "Pressure": data['current']['pressure_mb'],

    "Condition": data["current"]["condition"]["text"],
    "Cloud Cover": data['current']['cloud'],
    "Visibility_km": data['current']['vis_km'],

    "Wind Speed Km/H": data['current']['wind_kph'],
    "Wind Degree": data['current']['wind_degree'],
    "Wind Direction": data['current']['wind_dir'],

    "Precipitation_mm": data['current']['precip_mm'],
    "Will_it_rain": 1 if data['current']['precip_mm'] > 0 else 0,

    "UV Index": data['current']['uv']
}

df = pd.DataFrame([weather_data])

file_name = "weather_data.csv"

if os.path.exists(file_name):
    df.to_csv(file_name, mode='a', header=False, index=False)
else:
    df.to_csv(file_name, index=False)

# optional logging
with open("log.txt", "a") as f:
    f.write(f"Data collected at {weather_data['Time']}\n")
