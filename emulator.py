import keyboard
import server

flag = True
keyboard.add_hotkey('1', lambda: server.add_worker("Seba"))
keyboard.add_hotkey('2', lambda: server.add_terminal(1234))
keyboard.add_hotkey('tab', lambda: server.add_card(643))
keyboard.add_hotkey('3', lambda: server.assing_card_id("328377771909487252715599941261395726277", 12345))
keyboard.add_hotkey('4', lambda: server.remove_card_id("328377771909487252715599941261395726277"))
keyboard.add_hotkey('5', lambda: server.registration(12345, 123432))
keyboard.add_hotkey('6', lambda: server.registration(123456, 123432))

while(flag):
    if (keyboard.is_pressed('Esc')):
        flag = False