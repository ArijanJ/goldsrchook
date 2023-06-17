from pynput.keyboard import Key, Controller
from util.logs import log_wrapper as log

keyboard = Controller()

hotkey = Key.pause

def send_hotkey():
    keyboard.press(hotkey)
    keyboard.release(hotkey)

def run(text: str):
    for line in text.splitlines():
        log(f'Executing: {line}')
    
    with open("exec.cfg", "a", encoding="utf-8") as cfg:
        cfg.truncate(0)
        cfg.write(text)

    send_hotkey()