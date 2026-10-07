# Uses Open-Meteo: no API key required.
import requests

city = input("City: ")
geo = requests.get(
    "https://geocoding-api.open-meteo.com/v1/search",
    params={"name": city, "count": 1, "language": "en", "format": "json"},
    timeout=10
).json()
if not geo.get("results"):
    print("City not found.")
    raise SystemExit
place = geo["results"][0]
data = requests.get(
    "https://api.open-meteo.com/v1/forecast",
    params={"latitude": place["latitude"], "longitude": place["longitude"],
            "current":"temperature_2m,relative_humidity_2m,wind_speed_10m",
            "timezone":"auto"},
    timeout=10
).json()["current"]
print(f'{place["name"]}, {place.get("country","")}')
print("Temperature:", data["temperature_2m"], "°C")
print("Humidity:", data["relative_humidity_2m"], "%")
print("Wind:", data["wind_speed_10m"], "km/h")
