import paho.mqtt.client as mqtt
from app.data_operations import registration
from settings import scan_topic, broker_address, port
from app import logger

client = mqtt.Client()


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        logger.log("Connection established")
    else:
        logger.log(f"Couldn't connect to the broker {broker_address}")


def on_disconnect():
    logger.log("Disconnected from the broker")


def on_message(client, userdata, message):
    message_decoded = (str(message.payload.decode("utf-8"))).split(".")
    if len(message_decoded) == 2:
        card_id = message_decoded[0]
        terminal_id = message_decoded[1]
        registration(card_id, terminal_id)
        return message_decoded
    else:
        logger.log("Wrong message")

def enter_login_details():
    login = input("Enter login: ")
    password = input("Enter password: ")
    return login, password

def server_run():
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message
    client.tls_set("certs/ca.crt")  # path to certification
    login, password = enter_login_details()
    client.username_pw_set(username=login, password=password)     # Authenticate
    client.connect(broker_address, port)
    client.subscribe(scan_topic)
    client.loop_forever()


if __name__ == "__main__":
    server_run()
