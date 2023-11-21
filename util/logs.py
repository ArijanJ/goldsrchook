import time
import inspect

from colorama import Fore as colorama_fore
from colorama import Style as colorama_style

white = colorama_fore.WHITE
green = colorama_fore.GREEN
reset = colorama_style.RESET_ALL

def separator():
    print(white + "="*50 + reset)

def format_log_with_caller(string: str, caller: str) -> str:
    return f'[{green}{caller}{reset} @ {time.strftime("%H:%M:%S", time.localtime())}]: {str(string)}'

def format_log_simple(message: str) -> str:
    return f'[{time.strftime("%H:%M:%S", time.localtime())}]: {str(message)}'

def log_wrapper(message: str):
    frame = inspect.stack()[1]
    caller = inspect.getmodule(frame[0]).__name__

    print(format_log_with_caller(message, caller))

def log_to_console_file(message: str):
    with open('consolelog.txt', 'a', encoding='utf-8') as file:
        file.write(format_log_simple(message))
