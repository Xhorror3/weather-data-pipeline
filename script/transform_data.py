import pandas as pd
import os

RAW_FILE = os.path.join(os.path.dirname(__file__), "../data/raw_weather.csv")
PROCESSED_FILE = os.path.join(os.path.dirname(__file__), "../data/processed_weather.csv")

def transform():
    df = pd.read_csv(RAW_FILE)

    # Convert timestamp to datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # Extract day, hour, weekday
    df["date"] = df["timestamp"].dt.date
    df["hour"] = df["timestamp"].dt.hour
    df["weekday"] = df["timestamp"].dt.day_name()

    # Create a temperature category
    def temp_label(temp):
        if temp < 10:
            return "Cold"
        elif temp < 25:
            return "Moderate"
        else:
            return "Hot"

    df["temp_category"] = df["temp"].apply(temp_label)

    df.to_csv(PROCESSED_FILE, index=False)
    print(f"Processed data saved to {PROCESSED_FILE}")

if __name__ == "__main__":
    transform()
