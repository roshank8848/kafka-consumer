from confluent_kafka import Consumer, KafkaError
from confluent_kafka import OFFSET_BEGINNING

def on_assign(consumer, partitions):
    """ Callback for when partition assignments change """
    for partition in partitions:
        partition.offset = OFFSET_BEGINNING

def on_message(message):
    """ Callback for when a message is received """
    if message.error() is not None:
        if message.error().code() == KafkaError._PARTITION_EOF:
            print("Reached end of partition event for {} [{}] at offset {}".format(
                message.topic(), message.partition(), message.offset()))
        else:
            print("Error in receiving message: {}".format(message.error()))
    else:
        print("Received message from {} [{}] at offset {}: key={}, value={}".format(
            message.topic(), message.partition(), message.offset(), message.key(), message.value()))

# Set up the Kafka consumer configuration
conf = {
    'bootstrap.servers': 'k8s-kafka-cluster-kafka-bootstrap.kafka:9092',  # Replace with the address of your Kafka broker(s)
    'group.id': 'python-consumer-group',
    'auto.offset.reset': 'earliest'
}

# Create the Kafka consumer instance
consumer = Consumer(conf)

# Subscribe to the desired topic
consumer.subscribe(['my-topic'], on_assign=on_assign)

# Continuously poll for new messages
while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError.PARTITION_EOF:
            print("Reached end of partition event for {} [{}] at offset {}".format(
                msg.topic(), msg.partition(), msg.offset()))
        else:
            print("Error in receiving message: {}".format(msg.error()))
    else:
        on_message(msg)
