import keyboard
import sys
from data_operations import *
from reports import generate_report

keyboard.add_hotkey('Esc', lambda: sys.exit())

def choose_from_dict(dict, label):
    print(f"\n{label}")
    for i, data in enumerate(dict):
        print(f"({i}). {data} {dict[data]}")
    num = input()
    id = list(dict.items())[int(num)][0]

    return id

def add_terminal_ui():
    name = input("Enter terminal name: ")
    id = input("Enter terminal id: ")
    add_terminal(name, id)

def remove_terminal_ui():
    if len(terminals)==0: return
    terminal_id = choose_from_dict(terminals, "Select terminal ID: ")
    remove_terminal(terminal_id)

def assign_card_ui():
    if len(workers)==0 or len(cards)==0: return
    worker_id = choose_from_dict(workers, "Select worker ID: ")
    card_id = choose_from_dict(cards, "Select card ID: ")
    assign_card_id(worker_id, card_id)

def unassign_card_ui():
    if len(workers)==0: return
    worker_id = choose_from_dict(workers, "Select worker ID: ")
    unassign_card_id(worker_id)

def simulate_client():
    test_cards = cards
    test_cards['[176, 111, 225, 37, 27]'] = {}
    test_cards['[217, 125, 80, 211, 39]'] = {}
    card_id = choose_from_dict(test_cards, "Choose card ID: ")
    terminal_id = choose_from_dict(terminals, "Select terminal ID: ")
    return card_id, terminal_id

def register_ui():
    if len(terminals)==0: return
    card_id, terminal_id = simulate_client()
    registration(card_id, terminal_id)

def generate_report_ui():
    if len(workers)==0: return
    filtered_workers = dict(filter(lambda data: data[1]['card_id'], workers.items()))
    worker_id = choose_from_dict(filtered_workers, "Select worker ID: ")
    generate_report(worker_id)

def add_worker_ui():
    name = input("Enter worker name: ")
    add_worker(name)

def remove_worker_ui():
    if len(terminals): return
    worker_id = choose_from_dict(terminals, "Select worker ID: ")
    remove_worker(worker_id)

def add_card_ui():
    name = input("Enter card name: ")
    card_id = input("Enter card id: ")
    add_card(name, card_id)

def remove_card_ui():
    if len(cards): return
    card_id = choose_from_dict(cards, "Select card ID: ")
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
        choice = input()
        function = menu[int(choice)-1][1]
        function()

server_run()