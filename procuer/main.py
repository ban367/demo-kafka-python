from kafka import KafkaProducer
import json
import time


def main():
    while True:
        try:
            producer = KafkaProducer(
                bootstrap_servers='kafka:9092',
                value_serializer=lambda x: json.dumps(x).encode('utf-8'))
            break
        except Exception:
            print('connection error')
            time.sleep(3)
    send_count = 1

    while True:
        result = producer.send(
            'test', {'send_count': send_count, 'message': 'test'}
        ).get(timeout=60)
        print(result)
        time.sleep(1)
        send_count += 1


if __name__ == '__main__':
    main()
