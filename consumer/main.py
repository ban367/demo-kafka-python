from kafka import KafkaConsumer
from kafka.structs import OffsetAndMetadata, TopicPartition
import json
import time


def main():
    while True:
        try:
            consumer = KafkaConsumer(
                'test',
                bootstrap_servers=['kafka:9092'],
                auto_offset_reset='earliest',
                group_id='1',
                value_deserializer=lambda x: json.loads(x.decode('utf-8')))
            break
        except Exception:
            print('connection error')
            time.sleep(3)

    for message in consumer:
        print(message.value)

        tp = TopicPartition(message.topic, message.partition)
        offsets = {tp: OffsetAndMetadata(message.offset, None)}
        consumer.commit(offsets=offsets)


if __name__ == '__main__':
    main()
