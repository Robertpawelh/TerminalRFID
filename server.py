import json
import uuid
import datetime

workers_filename = "data/workers.json"
cards_filename = "data/cards.json"
terminals_filename = "data/terminals.json"
registrations_filename = "data/registrations.json"

def read_data(path):
    with open (path) as f:
        data = json.load(f)
    return data

def write_data(path, data):
   with open (path, 'w') as f:
        json.dump(data, f, indent=2)

workers = read_data(workers_filename)
cards = read_data(cards_filename)
terminals = read_data(terminals_filename)
registrations = read_data(registrations_filename)

def add_terminal(terminal_id):
    terminal = {'terminalId': terminal_id}
    terminals.append(terminal)
    write_data(terminals_filename, terminals)

def remove_terminal(terminal_id):
    terminals.remove(terminal_id)
    write_data(terminals_filename, terminals)

def add_card(card_id):
    card = {'cardId': card_id}
    cards.append(card)
    write_data(cards_filename, cards)

def remove_card(card_id):
    cards.remove(card_id)
    write_data(cards_filename, cards)

def add_worker(name):
    id = uuid.uuid1().int
    worker = {'name': name}
    workers[id] = worker
    write_data(workers_filename, workers)

def remove_worker(name):
    workers.remove(id)
    write_data(workers_filename, workers)

def assing_card_id(workerId, card_id):
    workers[workerId]['cardId'] = card_id
    write_data(workers_filename, workers)

def remove_card_id(worker_id):
    worker = {'name': workers[worker_id]['name']}
    workers[worker_id] = worker
    write_data(workers_filename, workers)

def registration(card_id, terminal_id):
    flag = False
    worker = None
    for worker_id, worker_data in workers.items():
        if 'cardId' in worker_data:
            if card_id==worker_data['cardId']:
                worker = worker_id
    if worker:
        registrations.append({'worker_id': worker_id, 'date': str(datetime.datetime.now()), 'terminalId': terminal_id})
    else:
        registrations.append({'card_id': card_id, 'date': str(datetime.datetime.now()), 'terminalId': terminal_id})
    write_data(registrations_filename, registrations)

def generate_raport(client):
    pass


""" RASPBERRY PI METHOD TO SERVICE RFID
import time
import RPi.GPIO as GPIO
from config import *  # pylint: disable=unused-wildcard-import
import lib.rfid.MFRC522 as MFRC522
import signal

def rfidRead():
    MIFAREReader = MFRC522.MFRC522()
    print("Press the red or green button to exit this test.")
    while GPIO.input(buttonRed) and GPIO.input(buttonGreen):
        (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
        if status == MIFAREReader.MI_OK:
            (status, uid) = MIFAREReader.MFRC522_Anticoll()
            if status == MIFAREReader.MI_OK:
                num = 0
                for i in range(0, len(uid)):
                    num += uid[i] << (i * 8)
                print(f"Card read UID: {uid} > {num}")
                time.sleep(0.5)
    print("RFID disabled")
    time.sleep(0.5)


def test():
    print('\nRFID test.')
    rfidRead()

"""