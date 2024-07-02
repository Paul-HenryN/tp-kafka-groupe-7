from datetime import datetime
import json
import streamlit as st
from producer import WeatherDataProducer
from consumer import WeatherDataConsumer

st.title("☀️ Live Weather Data")

city_name = st.text_input(
    "Location",
    placeholder="Choose a location",
    label_visibility="hidden",
)

if "city_name" not in st.session_state:
    st.session_state["city_name"] = "Douala"


if city_name:
    st.session_state["city_name"] = city_name

st.header(st.session_state["city_name"].capitalize())

if str(st.session_state["city_name"]).lower() not in st.session_state:
    weather_data_producer = WeatherDataProducer(
        str(st.session_state["city_name"]).lower()
    )
    weather_data_producer.start_fetching_thread()
    st.session_state[st.session_state["city_name"].lower()] = weather_data_producer

weather_data_consumer = WeatherDataConsumer(st.session_state["city_name"].lower())

with st.empty():
    temperature_chart_data = []

    for message in weather_data_consumer.consumer:
        weather_infos = json.loads(message.value.decode())

        country = weather_infos["location"]["country"]
        temperature_celsius = weather_infos["current"]["temp_c"]
        wind_speed_mph = weather_infos["current"]["wind_mph"]
        humidity = weather_infos["current"]["humidity"]
        weather_description = weather_infos["current"]["condition"]["text"]

        temperature_chart_data.append(
            {"Temperature": temperature_celsius, "Time": datetime.now()}
        )

        c = st.container()

        c.caption(country)

        c.write(weather_description)

        col1, col2, col3 = c.columns(3)
        col1.metric("Temperature", str(temperature_celsius) + " °C")
        col2.metric("Wind", str(wind_speed_mph) + " mph")
        col3.metric("Humidity", str(humidity) + " %")

        c.line_chart(temperature_chart_data, x="Time", y="Temperature")
