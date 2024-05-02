def forecast(*weather_data):
    weather_data = list(weather_data)
    result = {}

    for city, weather in weather_data:
        result[city] = weather

    sorted_result = {k: v for k, v in sorted(result.items(), key=lambda x: (x[1], x[0]))}

    sunny = ''
    cloudy = ''
    rainy = ''

    for city, weather in sorted_result.items():
        if weather == "Sunny":
            sunny += f'{city} - {weather}\n'
        elif weather == "Cloudy":
            cloudy += f'{city} - {weather}\n'
        elif weather == "Rainy":
            rainy += f'{city} - {weather}\n'

    return sunny + cloudy + rainy


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
