import keyboard
import sys
from data_operations import *
from reports import generate_report

keyboard.add_hotkey('Esc', lambda: sys.exit())

def extended_input(min, max, label=""):
    while True:
        try:
            num = int(input(label))
            if num >= min and num < max:
                return num
            print(f"Number should be between {min} and {max-1}")
        except Exception:
            print("Invalid input")

def choose_from_dict(dict, label):
    print(f"\n{label}")
    for i, data in enumerate(dict):
        print(f"({i}). {data} {dict[data]}")
    print(f"({i+1}). CANCEL")
    num = extended_input(0, len(dict.keys())+1)
    if num == i+1: return None
    id = list(dict.items())[int(num)][0]
    return id

def add_terminal_ui():
    name = input("Enter terminal name: ")
    id = input("Enter terminal id: ")
    add_terminal(name, id)

def remove_terminal_ui():
    if len(terminals)==0:
        logger.log("No terminals available")
        return
    terminal_id = choose_from_dict(terminals, "Select terminal ID: ")
    if terminal_id:
        remove_terminal(terminal_id)

def assign_card_ui():
    if len(workers)==0 or len(cards)==0:
        logger.log("No workers or cards available")
        return
    worker_id = choose_from_dict(workers, "Select worker ID: ")
    card_id = choose_from_dict(cards, "Select card ID: ")
    if worker_id and card_id:
        assign_card_id(worker_id, card_id)

def unassign_card_ui():
    filtered_workers = dict(filter(lambda data: data[1]['card_id'], workers.items()))
    if len(filtered_workers)==0:
        logger.log("No workers with card")
        return
    worker_id = choose_from_dict(filtered_workers, "Select worker ID: ")
    if worker_id:
        unassign_card_id(worker_id)

def simulate_client():
    test_cards = dict.copy(cards)
    test_cards['[176, 111, 225, 37, 27]'] = {}
    test_cards['[217, 125, 80, 211, 39]'] = {}
    card_id = choose_from_dict(test_cards, "Choose card ID: ")
    terminal_id = choose_from_dict(terminals, "Select terminal ID: ")
    return card_id, terminal_id

def register_ui():
    if len(terminals)==0:
        logger.log("No terminals available")
        return
    card_id, terminal_id = simulate_client()
    if card_id and terminal_id:
        registration(card_id, terminal_id)

def generate_report_ui():
    filtered_workers = workers#dict(filter(lambda data: data[1]['card_id'], workers.items()))
    if len(filtered_workers)==0:
        logger.log("Can't generate a report")
        return
    worker_id = choose_from_dict(filtered_workers, "Select worker ID: ")
    generate_report(worker_id)

def add_worker_ui():
    name = input("Enter worker name: ")
    add_worker(name)

def remove_worker_ui():
    if len(workers)==0: return
    worker_id = choose_from_dict(workers, "Select worker ID: ")
    if worker_id:
        remove_worker(worker_id)

def add_card_ui():
    name = input("Enter card name: ")
    card_id = input("Enter card id: ")
    add_card(name, card_id)

def remove_card_ui():
    if len(cards)==0: return
    card_id = choose_from_dict(cards, "Select card ID: ")
    if card_id:
        remove_card(card_id)

def other_functions_ui():
    menu = [        ("Add worker", add_worker_ui),
        ("Remove worker", remove_worker_ui),
        ("Add id card", add_card_ui),
        ("Remove card", remove_card_ui),
        ("DANGEROUS. Delete all data", delete_all_data)
    ]

    for i, command in enumerate(menu):
        print(f"({i+1}). {command[0]}")
    choice = input()
    function = menu[int(choice)-1][1]
    function()

def server_run():
    menu=[
        ("Add terminal", add_terminal_ui),
        ("Remove terminal", remove_terminal_ui),
        ("Assign card to worker", assign_card_ui),
        ("Unassign card from worker", unassign_card_ui),
        ("Register", register_ui),
        ("Generate report", generate_report_ui),
        ("Other", other_functions_ui),
        ("Exit", sys.exit)
    ]
    while(True):
        for i, command in enumerate(menu):
            print(f"({i+1}). {command[0]}")
        choice = extended_input(1, len(menu)+1)
        function = menu[int(choice)-1][1]
        function()