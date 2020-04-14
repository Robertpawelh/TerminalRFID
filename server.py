import paho.mqtt.client as mqtt
from app.data_operations import registration, terminals
broker_address = "127.0.0.1"
# broker = "10.0.0.1"
client = mqtt.Client()


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connection established")
    else:
        print("Bad connection")


def on_disconnect():
    print("Disconnected from broker")


def register(card_id, terminal_id):
    if terminal_id in terminals:
        registration(card_id, terminal_id)


def on_message(client, userdata, message):
    message_decoded = (str(message.payload.decode("utf-8"))).split(".")
    if len(message_decoded) == 2:
        print("CARD: ",message_decoded[0])
        print("TERMINAL: ",message_decoded[1])
        register(message_decoded[0], message_decoded[1])
        return message_decoded
    else:
        print("Wrong message")


def server_run():
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message
    client.connect(broker_address)
    client.subscribe("card/terminal")
    client.loop_forever()


if __name__ == "__main__":
    server_run()
