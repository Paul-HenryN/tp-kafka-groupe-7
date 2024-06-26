import json
from kafka import KafkaConsumer


class WeatherDataConsumer:
    def __init__(self, topic):
        self.consumer = KafkaConsumer(topic, bootstrap_servers="localhost:9092")
