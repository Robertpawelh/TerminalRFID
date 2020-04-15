import paho.mqtt.client as mqtt
import sys
import keyboard
import time
from settings import scan_topic, broker_address, cards

terminal_id = sys.argv[1] if len(sys.argv) > 1 else "UNDEFINED"
client = mqtt.Client(terminal_id)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connection established")
    else:
        print("Bad connection")


def on_disconnect():
    print("Disconnected from broker")


def call_msg(card_id):
    client.publish(scan_topic, f"{card_id}.{terminal_id}")


def scan():
    for index, card in enumerate(cards):
        if keyboard.is_pressed(f"{index+1}"):
            print("Scanning")
            call_msg(cards[index])
            time.sleep(1)
            print("Waiting for a card")


def client_run():
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.connect(broker_address)
    client.loop_start()
    print("Waiting for a card")
    while True:
        scan()
    client.loop_stop()
    client.disconnect()


if __name__ == "__main__":
    client_run()
