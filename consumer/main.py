from kafka import KafkaConsumer
import time


def main():
    while True:
        try:
            consumer = KafkaConsumer(
                'test', bootstrap_servers=['kafka:9092'])
            break
        except Exception:
            print("connection error")
            time.sleep(3)

    for message in consumer:
        print(message.value.decode())


if __name__ == '__main__':
    main()
