from datetime import date
import pymongo
import os

DATABASE_PORT = int(os.getenv('DATABASE_PORT', 24000))
DATABASE_NAME = os.getenv('DATABASE_NAME', 'weather')

client = pymongo.MongoClient(f'mongodb://localhost:{DATABASE_PORT}/')
db = client[DATABASE_NAME]

def add_weather_data(city, temperature, wind_speed, humidity, hour):
    collection = db['city_weather']
    data = {
        'city': city,
        'temperature': temperature,
        'wind_speed': wind_speed,
        'humidity': humidity,
        'hour': hour
    }
    result = collection.insert_one(data)
    print(f'Data inserted for {city}. Document ID: {result.inserted_id}')

def get_weather_data(city):
    collection = db['city_weather']
    query = {'city': city}
    result = collection.find(query)
    return result

if __name__ == '__main__':
    # add_weather_data('Ebolowa', 25.5, 15, 70, 6)
    # add_weather_data('Cachan', 22.0, 12, 65, 4)
    # add_weather_data('Villejuif', 28.3, 18,75, 5)
    # add_weather_data('Rome', 31.5, 6, 70, 12)

    city_name = 'Rome'
    weather_data = get_weather_data(city_name)
    
    if weather_data:
        for data in weather_data:
            print(f"Weather data for {city_name}:")
            print(f"Temperature: {data['temperature']} °C")
            print(f"Wind Speed: {data['wind_speed']} km/h")
            print(f"Humidity: {data['humidity']} %")
            print(f"Hour: {data['hour']} h")

    client.close()
