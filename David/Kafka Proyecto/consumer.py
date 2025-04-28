from kafka import KafkaConsumer
from json import loads
consumer = KafkaConsumer(
    'iabd-topic',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='iabd-grupo-1',
    value_deserializer=lambda m: loads(m.decode('utf-8')),    
    bootstrap_servers=['127.0.0.1:29092'] # Usa la IP del host
)
for m in consumer:
    print(m.value)