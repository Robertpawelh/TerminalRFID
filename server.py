import json
import uuid
import datetime
import logger

workers_filename = "data/workers.json"
cards_filename = "data/cards.json"
terminals_filename = "data/terminals.json"
registrations_filename = "data/registrations.json"

def read_data(path):
    with open (path) as f:
        data = json.load(f)
    logger.log(str(path) + " loaded")
    return data

def write_data(path, data):
   with open (path, 'w') as f:
        json.dump(data, f, indent=2)

workers = read_data(workers_filename)
cards = read_data(cards_filename)
terminals = read_data(terminals_filename)
registrations = read_data(registrations_filename)

def add_terminal(name, terminal_id):
    if terminal_id not in terminals:
        terminals[terminal_id] = {'name': name}
        write_data(terminals_filename, terminals)
        logger.log(f"{name} added")
    else:
        logger.log("Terminal already exists")

def remove_terminal(terminal_id):
    terminals.remove(terminal_id)
    write_data(terminals_filename, terminals)
    logger.log(f"Terminal with {terminal_id} removed")

def add_card(name, card_id):
    cards[card_id] = {'name': name}
    write_data(cards_filename, cards)
    logger.log(f"{name} added")

def remove_card(card_id):
    cards.remove(card_id)
    write_data(cards_filename, cards)
    logger.log(f"Card with {card_id} removed")

def add_worker(name):
    id = uuid.uuid1().int
    worker = {'name': name}
    workers[id] = worker
    write_data(workers_filename, workers)
    logger.log(f"{name} added")

def remove_worker(worker_id):
    if worker_id in workers:
        del workers[worker_id]
        write_data(workers_filename, workers)
        logger.log(f"Worker with {worker_id} removed")
    else:
        logger.log(f"Incorrect id")
def assing_card_id(worker_id, card_id):
    if worker_id in workers and card_id in cards:
        workers[worker_id]['card_id'] = card_id
        write_data(workers_filename, workers)
        logger.log(f"{card_id} assigned to {worker_id}")
    else:
        logger.log("Operation didn't succeed")

def disassign_card_id(worker_id):
    if worker_id in workers:
        worker = {'name': workers[worker_id]['name']}
        workers[worker_id] = worker
        write_data(workers_filename, workers)
        logger.log(f"{worker_id} now doesn't have card_id")
    else:
        logger.log("Worker doesn't exist")

def registration(card_id, terminal_id):
    flag = False
    worker = None
    for worker_id, worker_data in workers.items():
        if 'cardId' in worker_data:
            if card_id==worker_data['card_id']:
                worker = worker_id
    date = str(datetime.datetime.now())
    if worker:
        registrations.append({'worker_id': worker_id, 'date': date, 'terminal_id': terminal_id})
    else:
        registrations.append({'card_id': card_id, 'date': date, 'terminal_id': terminal_id})
    write_data(registrations_filename, registrations)
    logger.log(f"New unidentified registration at {date}")

def generate_raport(client):
    pass

def hard_reset():
    terminals = {}
    cards = {}
    workers = {}
    registrations = []
    write_data(terminals_filename, terminals)
    write_data(cards_filename, cards)
    write_data(workers_filename, workers)
    write_data(registrations_filename, registrations)
    logger.log("Deleted all data")

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