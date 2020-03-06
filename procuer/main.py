from kafka import KafkaProducer
import time


def main():
    while True:
        try:
            producer = KafkaProducer(
                bootstrap_servers='kafka:9092')
            break
        except Exception:
            print("connection error")
            time.sleep(3)
    send_count = 1

    while True:
        result = producer.send(
            'test', ("send_count: " + str(send_count)).encode()
            ).get(timeout=60)
        print(result)
        time.sleep(1)
        send_count += 1


if __name__ == '__main__':
    main()
