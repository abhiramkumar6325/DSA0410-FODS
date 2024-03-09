weather_data = {
    'Sunny': 30,
    'Rainy': 20,
    'Cloudy': 15,
    'Snowy': 10,
    'Foggy': 5
}

most_common_weather = max(weather_data, key=weather_data.get)

print("The most common weather type is:", most_common_weather)
