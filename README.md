# Kafka Consumer

The kafka consumer consumes messages from `my-topic` topic. To run the app on the development setup. 

## Install requirements

```bash
pip install -r requirements.txt
```

## Execute the command for running the consumer

```bash
python consumer.py
```

## Building a docker container

```bash
docker build -t kafka-consumer:0.0.1 .
```

## Note
Use appropriate kafka brokers and topics for the consumer code to work.