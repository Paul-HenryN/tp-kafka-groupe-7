import json
import time
import urllib.request
import threading
from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic


class WeatherDataProducer:
    def __init__(self, topic: str):
        self.topic = topic
        self.init_topic()

    def init_topic(self):
        admin_client = KafkaAdminClient(
            bootstrap_servers="localhost:9092", client_id="test"
        )

        topics = [NewTopic(name=self.topic, num_partitions=10, replication_factor=1)]
        admin_client.create_topics(
            new_topics=filter(
                lambda topic: topic.name not in admin_client.list_topics(), topics
            ),
            validate_only=False,
        )

    def fetch_weather_data(self):
        url = f"https://api.weatherapi.com/v1/current.json?key=2f7d766d3bd8444399083202242106&q={self.topic}&aqi=yes"

        producer = KafkaProducer(bootstrap_servers="localhost:9092")

        while True:
            response = urllib.request.urlopen(url)
            weather_data = json.loads(response.read().decode())
            producer.send(self.topic, json.dumps(weather_data).encode())
            time.sleep(1)

    def start_fetching_thread(self):
        fetching_thread = threading.Thread(target=self.fetch_weather_data)

        print(f"Starting fetching thread for {self.topic}...")
        fetching_thread.start()
