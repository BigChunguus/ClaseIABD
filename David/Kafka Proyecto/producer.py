from kafka import KafkaProducer
from json import dumps
import time

producer = KafkaProducer(
    value_serializer=lambda m: dumps(m).encode('utf-8'),
    bootstrap_servers=['127.0.0.1:29092'] # Usa la IP de tu host expuesta en docker-compose
)
for i in range(10):
    producer.send("iabd-topic", value={"nombre": "producer " + str(i)})
# Esperar un poco antes de cerrar
time.sleep(1)