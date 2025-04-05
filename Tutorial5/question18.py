import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("weather.csv")
print("\nFirst 10 Rows of Weather Data:\n", df.head(10))
max_temp = df["temperature"].max()
min_temp = df["temperature"].min()
print(f"\nMaximum Temperature: {max_temp}°C")
print(f"Minimum Temperature: {min_temp}°C")
places_below_28 = df[df["temperature"] < 28]["place"]
print("\nPlaces with Temperature < 28°C:\n", places_below_28.tolist())
cloudy_places = df[df["weather"] == "Cloudy"]["place"]
print("\nPlaces with Cloudy Weather:\n", cloudy_places.tolist())
weather_counts = df["weather"].value_counts()
print("\nWeather Type Frequency:\n", weather_counts)
plt.figure(figsize=(10, 5))
plt.bar(df["date"], df["temperature"], color="skyblue")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Trends Over 10 Days")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
