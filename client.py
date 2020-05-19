import paho.mqtt.client as mqtt
import sys
import keyboard
import time
from settings import scan_topic, broker_address, cards, port
from app import logger

terminal_id = sys.argv[1] if len(sys.argv) > 1 else "UNDEFINED"
keys_shift = int(sys.argv[2]) if len(sys.argv) > 2 else 1

client = mqtt.Client(terminal_id)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        logger.log("Connection established")
    else:
        logger.log(f"Couldn't connect to the broker {broker_address}")


def on_disconnect():
    logger.log("Disconnected from the broker")


def call_msg(card_id):
    client.publish(scan_topic, f"{card_id}.{terminal_id}")


def scan():
    for index, card in enumerate(cards):
        if keyboard.is_pressed(f"{(index+keys_shift) % 10}"):
            logger.log("Scanning")
            call_msg(cards[index])
            time.sleep(1)
            logger.log("Waiting for a card")
        if keyboard.is_pressed('q'):
            sys.exit()

def enter_login_details():
    login = input("Enter login: ")
    password = input("Enter password: ")
    return login, password

def client_run():
    logger.log(f"Terminal ID: {terminal_id}")
    logger.log(f"Keys for simulation:  {[(keys_shift+i)%10 for i in range(len(cards))]}")
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.tls_set("certs/ca.crt") # path to certification
    login, password = enter_login_details()
    client.username_pw_set(username=login, password=password)     # Authenticate (client, client_password)
    client.connect(broker_address, port)
    client.loop_start()
    logger.log("Waiting for a card")
    while True:
        scan()
    client.loop_stop()
    client.disconnect()

if __name__ == "__main__":
    client_run()
