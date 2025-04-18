import requests
import json
import pandas as pd
import os
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

def fetch_weather(city: str, api_key: str):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    print(f"Requesting: {url}")
    response = requests.get(url)
    print(f"Status code: {response.status_code}")
    print(f"Response text: {response.text}")
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch weather data")
        return None


def save_to_csv(data: dict, filepath: str):
    # Extract only relevant fields
    record = {
        "city": data["name"],
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather": data["weather"][0]["main"],
        "timestamp": datetime.now().isoformat()
    }

    df = pd.DataFrame([record])

    # Check if file exists
    if os.path.exists(filepath):
        df.to_csv(filepath, mode='a', header=False, index=False)
    else:
        df.to_csv(filepath, index=False)


if __name__ == "__main__":
    API_KEY = os.getenv("API_KEY")
    CITY = "Mumbai"
    FILEPATH = os.path.join(os.path.dirname(__file__), "../data/raw_weather.csv")

    data = fetch_weather(CITY, API_KEY)
    if data:
        save_to_csv(data, FILEPATH)
        print(f"Weather data for {CITY} saved to {FILEPATH}")
