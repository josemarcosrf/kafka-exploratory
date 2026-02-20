"""CLI to Publish and Consume from Kafka using confluent_kafka"""

import click

from confluent_kafka import Producer, Consumer, KafkaError


# Note: See dockrfile PLAINTEXT_HOST uses 29092
BROKER = "localhost:29092"
TOPIC = "demo-topic"


@click.group()
def cli():
    pass


@cli.command()
@click.option("--message", "-m", required=True, help="Message to send")
def produce(message):
    """Produce a message into Kafka."""
    producer = Producer({"bootstrap.servers": BROKER})

    producer.produce(TOPIC, message.encode("utf-8"))
    producer.flush()

    click.echo(f"📨 Produced: {message}")


@cli.command()
def consume():
    """Consume messages from Kafka."""
    consumer = Consumer(
        {
            "bootstrap.servers": BROKER,
            "group.id": "demo-group",
            "auto.offset.reset": "earliest",
        }
    )

    consumer.subscribe([TOPIC])
    click.echo("📥 Consuming... Ctrl+C to stop")

    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() != KafkaError._PARTITION_EOF:
                    click.echo(f"Error: {msg.error()}")
                continue
            click.echo(f"📬 Received: {msg.value().decode('utf-8')}")
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()


if __name__ == "__main__":
    cli()
