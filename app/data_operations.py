import json
import uuid
from datetime import datetime
from app import logger

workers_filename = "data/workers.json"
cards_filename = "data/cards.json"
terminals_filename = "data/terminals.json"
registrations_filename = "data/registrations.json"


def read_data(path):
    with open(path) as f:
        data = json.load(f)
    logger.log(str(path) + " loaded")
    return data


def write_data(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)


workers = read_data(workers_filename)
cards = read_data(cards_filename)
terminals = read_data(terminals_filename)
registrations = read_data(registrations_filename)


def add_data_to_id(path, dictionary, data, id):
    if id not in dictionary:
        dictionary[id] = data
        write_data(path, dictionary)
        logger.log(f"New element added to {path}")
    else:
        logger.log(f"{id} already exists")


def remove_data(path, dictionary, id):
    if id in dictionary:
        del dictionary[id]
        write_data(path, dictionary)
        logger.log(f"{id} removed")
    else:
        logger.log(f"Incorrect id")


def add_worker(name):
    id = uuid.uuid1().int
    worker_data = {'name': name, 'card_id': []}
    add_data_to_id(workers_filename, workers, worker_data, id)


def remove_worker(worker_id):
    card_id = workers[worker_id]['card_id']
    if card_id:
        cards[card_id]['owner_id'] = None
    remove_data(workers_filename, workers, worker_id)


def add_card(name, card_id):
    card_data = {'name': name, 'owner_id': None}
    add_data_to_id(cards_filename, cards, card_data, card_id)


def remove_card(card_id):
    worker_id = cards[card_id]['owner_id']
    if worker_id:
        workers[worker_id]['card_id'] = None
    remove_data(cards_filename, cards, card_id)


def add_terminal(name, terminal_id):
    terminal_data = {'name': name}
    add_data_to_id(terminals_filename, terminals, terminal_data, terminal_id)


def remove_terminal(terminal_id):
    remove_data(terminals_filename, terminals, terminal_id)


def assign_card_id(worker_id, card_id):
    if worker_id in workers and card_id in cards:
        if not cards[card_id]['owner_id']:
            workers[worker_id]['card_id'] = card_id
            cards[card_id]['owner_id'] = worker_id
            write_data(workers_filename, workers)
            write_data(cards_filename, cards)
            logger.log(f"{card_id} assigned to {worker_id}")
        else:
            logger.log("Card is already assigned")
    else:
        logger.log("Operation failed")


def unassign_card_id(worker_id, card_id):
    if worker_id in workers:
        if card_id in workers[worker_id]['card_id']:
            workers[worker_id]['card_id'] = None
            cards[card_id]['owner_id'] = None
            write_data(workers_filename, workers)
            write_data(cards_filename, cards)
            logger.log(f"{worker_id} now doesn't have {card_id} assigned")
        else:
            logger.log(f"{worker_id} didn't have this card_id")
    else:
        logger.log("Worker doesn't exist")


def registration(card_id, terminal_id):
    if terminal_id not in terminals:
        logger.log("Unknown terminal. Registration stopped")
        return

    date = str(datetime.now())

    if card_id in cards:
        worker = cards[card_id]['owner_id'] or 'UNKNOWN'
    else:
        worker = 'UNKNOWN'

    if worker is 'UNKNOWN':
        logger.log("Unidentified card. ", False)

    if card_id in registrations:
        data = registrations[card_id]
        if worker in data:
            if len(data[worker]['begin']) == len(data[worker]['end']):
                data[worker]['begin'].append(date)
                data[worker]['begin_t'].append(terminal_id)
                logger.log(f"Worker started job at {date}")
            else:
                data[worker]['end'].append(date)
                data[worker]['end_t'].append(terminal_id)
                logger.log(f"Worker finished job at {date}")
        else:
            data[worker] = {'begin': [date], 'begin_t': [terminal_id], 'end': [], 'end_t': []}
            logger.log(f"Worker started job at {date}")

    else:
        registrations[card_id] = {worker: {'begin': [date], 'begin_t': [terminal_id], 'end': [], 'end_t': []}}
        logger.log(f"Registration at {date}")

    write_data(registrations_filename, registrations)


def delete_all_data():
    global terminals, cards, workers, registrations
    terminals = {}
    cards = {}
    workers = {}
    registrations = {}
    write_data(terminals_filename, terminals)
    write_data(cards_filename, cards)
    write_data(workers_filename, workers)
    write_data(registrations_filename, registrations)
    logger.log("Deleted all data")
