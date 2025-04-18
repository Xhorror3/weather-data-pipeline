import streamlit as st
import pandas as pd
import requests

# Set up the OpenWeather API endpoint and your API key
API_KEY = "076d6dd5946fb1b198b90b532cab36ba"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def fetch_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()


def display_weather(data):
    if data.get('cod') != 200:
        st.error(f"Error: {data.get('message')}")
    else:
        city = data['name']
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']

        st.write(f"### Weather for {city}")
        st.write(f"**Temperature**: {temp}°C")
        st.write(f"**Description**: {description}")
        st.write(f"**Humidity**: {humidity}%")


# Streamlit UI
st.title("Weather Data Pipeline")
city = st.text_input("Enter city name", "Mumbai")

if st.button("Get Weather"):
    st.write("Fetching weather data...")
    data = fetch_weather(city)
    display_weather(data)

