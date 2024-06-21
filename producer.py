import json
import time
import urllib.request

from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic

API_KEY = "2f7d766d3bd8444399083202242106"
url = "https://api.weatherapi.com/v1/current.json?key={}&q=Douala&aqi=yes".format(
    API_KEY
)

admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092", client_id="test")

topics = [NewTopic(name="weather", num_partitions=1, replication_factor=1)]

admin_client.create_topics(
    new_topics=filter(
        lambda topic: topic.name not in admin_client.list_topics(), topics
    ),
    validate_only=False,
)

producer = KafkaProducer(bootstrap_servers="localhost:9092")

while True:
    response = urllib.request.urlopen(url)
    weather_infos = json.loads(response.read().decode())
    producer.send("weather", json.dumps(weather_infos).encode())
    time.sleep(60)
