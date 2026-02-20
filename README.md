# Kafka Exploratory


## How to


### ⚙️ Setup

You'll need [uv](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://docs.astral.sh/uv/&ved=2ahUKEwifh_7d8-eSAxVBKRAIHZtYDM0QFnoECB8QAQ&usg=AOvVaw2VJVt0jrah2S9tIgdc1yRc), then run:

```shell
uv pip install -r requirements.txt
```

### 🏃 Run

1. Run the docker services: 

	```shell
	make up
	```

2. In one terminal start the `FastStream` app:

	```shell
	make app
	```

3. Fire up a message with the CLI:

	```shell
	uv run python -m cli produce -m a-pretty-message
	```
