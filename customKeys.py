import time

from global_hotkeys import *
import keyboard as kb

isAlive = True
bindings = []
def clear_all():
    kb.send('ctrl+a')
    kb.send('backspace')

def print_hello():
    kb.write("Hello")

def exit_application():
    global is_alive
    print("exiting")
    # try:
    #     remove_hotkey(bindings)
    # except:
    #     print("Invalid Keystroke")
    stop_checking_hotkeys()
    is_alive = False
    return

bindings += [["space, space", None, clear_all, True],
             ["escape", None, exit_application, True]]
def listen_for_custom_keys():
    print(bindings)
    register_hotkeys(bindings)
    print("Listening to hotkeys..")
    start_checking_hotkeys()
    while isAlive:
        time.sleep(0.1)
    return

def main():
    listen_for_custom_keys()

# main()