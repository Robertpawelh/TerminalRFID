import keyboard
import server

flag = True
keyboard.add_hotkey('1', lambda: server.add_worker("Seba"))
keyboard.add_hotkey('q', lambda: server.remove_worker("224235145077410045823478833888085905349"))
keyboard.add_hotkey('2', lambda: server.add_terminal("Terminal 1", "1234"))
keyboard.add_hotkey('tab', lambda: server.add_card("Card 1", "643"))
keyboard.add_hotkey('3', lambda: server.assing_card_id(list(server.workers.keys())[0], "643"))
keyboard.add_hotkey('4', lambda: server.disassign_card_id("224235145077410045823478833888085905349"))
keyboard.add_hotkey('5', lambda: server.registration("643", "123432"))
keyboard.add_hotkey('6', lambda: server.registration("123456", "123432"))
keyboard.add_hotkey('r', lambda: server.hard_reset())

while(flag):
    if (keyboard.is_pressed('Esc')):
        flag = False