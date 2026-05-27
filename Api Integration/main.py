import requests
from dotenv import load_dotenv
import os
from datetime import datetime

# Return emoji based on weather
def get_weather_emoji(weather):

    if "cloud" in weather.lower():
        return "☁️"

    elif "rain" in weather.lower():
        return "🌧️"

    elif "clear" in weather.lower():
        return "☀️"

    return "🌍"

try:

    load_dotenv()
    apiKey = os.getenv("API_KEY")

    while True:

        city = input("Enter city (or type exit): ")

        if city.lower() == "exit":
            print("Program terminated....")
            break

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&units=metric"

        response = requests.get(url)
        data = response.json()

        if data['cod'] != 200:
            print("City not found")

        else:

            city_name = data["name"]
            humidity = data["main"]["humidity"]
            temperature = data["main"]["temp"]
            weather = data["weather"][0]["description"]
            wind_speed = data["wind"]["speed"]

            emoji = get_weather_emoji(weather)

            print("-" * 35)
            print(f"{'Weather Report':^35}")
            print("-" * 35)

            print(f"{'City':<15}: {city_name.title()}")
            print(f"{'Weather':<15}: {weather.title()} {emoji}")
            print(f"{'Humidity':<15}: {humidity}%")
            print(f"{'Temperature':<15}: {temperature} °C")
            print(f"{'Wind Speed':<15}: {wind_speed} m/s")

            print("-" * 35)

            with open("weather_report.txt", "a") as f:

                current_time = datetime.now()

                f.write(
                    f"{current_time.strftime('%d-%m-%Y %H:%M:%S')} | "
                    f"{city_name} - {temperature} °C\n"
                )

except Exception:
    print("No Internet Connection")