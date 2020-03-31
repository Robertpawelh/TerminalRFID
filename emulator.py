import keyboard
import data_operations
cards = [[176, 111, 225, 37, 27], [217, 125, 80, 211, 39], [210, 113, 89, 23, 36]]
#keyboard.add_hotkey('1', lambda: server.registration(cards[0], '13579'))
#keyboard.add_hotkey('2', lambda: server.registration(cards[1], '13579'))
#keyboard.add_hotkey('3', lambda: server.registration(cards[2], '13579'))
active = True
keyboard.add_hotkey('1', lambda: data_operations.add_worker("Seba"))
keyboard.add_hotkey('q', lambda: data_operations.remove_worker("224235145077410045823478833888085905349"))
keyboard.add_hotkey('2', lambda: data_operations.add_terminal("Terminal 1", "1234"))
keyboard.add_hotkey('tab', lambda: data_operations.add_card("Card 1", "643"))
keyboard.add_hotkey('3', lambda: data_operations.assign_card_id(list(data_operations.workers.keys())[0], "643"))
keyboard.add_hotkey('e', lambda: data_operations.assign_card_id(list(data_operations.workers.keys())[1], "643"))
keyboard.add_hotkey('4', lambda: data_operations.disassign_card_id(list(data_operations.workers.keys())[0]))
keyboard.add_hotkey('5', lambda: data_operations.registration("643", "123432"))
keyboard.add_hotkey('6', lambda: data_operations.registration("123456", "123432"))
keyboard.add_hotkey('r', lambda: data_operations.hard_reset())


while(active):
 #   if (keyboard.is_pressed('1')): server.registration(cards[0], '13579')
 #   if (keyboard.is_pressed('2')): server.registration(cards[1], '13579')
  #  if (keyboard.is_pressed('3')): server.registration(cards[2], '13579')
    if (keyboard.is_pressed('Esc')): active = False
  #  if (keyboard.is_pressed('9')): server_configuration()
