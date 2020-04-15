import paho.mqtt.client as mqtt
from app.data_operations import registration, terminals
from settings import scan_topic, broker_address

client = mqtt.Client()


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connection established")
    else:
        print("Bad connection")


def on_disconnect():
    print("Disconnected from broker")


def on_message(client, userdata, message):
    message_decoded = (str(message.payload.decode("utf-8"))).split(".")
    if len(message_decoded) == 2:
        card = message_decoded[0]
        terminal = message_decoded[1]
        registration(card, terminal)
        return message_decoded
    else:
        print("Wrong message")


def server_run():
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message
    client.connect(broker_address)
    client.subscribe(scan_topic)
    client.loop_forever()


if __name__ == "__main__":
    server_run()
