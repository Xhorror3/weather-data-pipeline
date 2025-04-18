import pandas as pd
import psycopg2
import os

# Path to the processed CSV
PROCESSED_FILE = os.path.join(os.path.dirname(__file__), "../data/processed_weather.csv")

def load_to_postgres():
    df = pd.read_csv(PROCESSED_FILE)

    # Connect to your PostgreSQL database
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="weather_db",
        user="postgres",
        password="system"  # ← replace this!
    )
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_data (
            city TEXT,
            temp FLOAT,
            humidity INT,
            weather TEXT,
            timestamp TIMESTAMP,
            date DATE,
            hour INT,
            weekday TEXT,
            temp_category TEXT
        );
    """)

    # Insert data into the table
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO weather_data (
                city, temp, humidity, weather,
                timestamp, date, hour, weekday, temp_category
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, tuple(row))

    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Weather data loaded into PostgreSQL successfully!")

if __name__ == "__main__":
    load_to_postgres()
