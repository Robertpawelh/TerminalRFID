import paho.mqtt.client as mqtt
import sys

terminal_id = sys.argv[1] if len(sys.argv)>1 else 'UNDEFINIED'
client = mqtt.Client(terminal_id)
topic_name = "card/terminal"
broker_address = "127.0.0.1"
# host_name = "localhost"
# broker = "10.0.0.1"


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connection established")
    else:
        print("Bad connection")


def on_disconnect():
    print("Disconnected from broker")


def call_msg(card_id):
    client.publish(topic_name, f"{card_id}.{terminal_id}")


def scan():
    a = input("Enter example data")
    call_msg(a)
    # zmienic na keyboard i delay na usera?


def client_run():
    client.on_connect=on_connect
    client.on_disconnect=on_disconnect
    client.connect(broker_address)
    client.loop_start()
    while True:
       scan()
    client.loop_stop()
    client.disconnect()


if __name__ == "__main__":
    client_run()

