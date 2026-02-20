"""FastStream App to Publish and Consume from Kafka"""

import asyncio
from faststream import FastStream
from faststream.kafka import KafkaBroker
from aiokafka.errors import KafkaConnectionError

# Note: See dockrfile PLAINTEXT_HOST uses 29092
broker = KafkaBroker("localhost:29092")
app = FastStream(broker)

TOPIC = "demo-topic"


# ------------------
# CONSUMER
# ------------------
@broker.subscriber(TOPIC)
async def handle_message(msg: str):
    print(f"📥 [consumer] received: {msg}")


# ------------------
# PRODUCER AT STARTUP
# ------------------
# @app.after_startup
async def produce(context):
    # Retry loop until Kafka is reachable
    for i in range(10):
        try:
            await broker.publish(f"Hello from FastStream! ({i})", topic=TOPIC)
            print("📤 [producer] message sent")
            break
        except KafkaConnectionError:
            print("📤 [producer] Kafka not ready, retrying...")
            await asyncio.sleep(2)


# if __name__ == "__main__":
#     app.run()
