from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime, timedelta
from util.logs import *
from util.logs import log_wrapper as log
from util.function import function
import re

my_observer = Observer()

# Assuming this is 3 directories deep in main Half-Life folder
# TODO: 
path = "../../../"
console = path + "qconsole.log"

func_list: list[function] = []
def run(passed_list):
    global func_list
    func_list = passed_list
    log('Initializing:')
    
    for func in func_list:
        pattern = func.pattern.strip()
        if func.enabled:
            log(f'{func.alias}'.ljust(15) + f'[{pattern}]'.ljust(20) + '[X]')
        else:
            log(f'{func.alias}'.ljust(15) + f'[{pattern}]'.ljust(20) + '[ ]')

    my_observer.schedule(EventHandler(), path, recursive=False)
    my_observer.start()

def stop():
    my_observer.stop()
    my_observer.join()

class EventHandler(FileSystemEventHandler):
    def __init__(self):
        self.last_modified = datetime.now()

    def on_modified(self, event):
        if datetime.now() - self.last_modified < timedelta(seconds=0.1):
            return

        self.last_modified = datetime.now()

        if event.src_path != console:
            return

        # Process
        separate()
        file = open(console, 'r+', encoding='utf-8')
        for line in list(reversed(file.readlines()))[:25]:
            # TODO: Figure this variable out
            filelogline = True
            cleanLine = line.strip()
            log(cleanLine)
            for func in func_list:
                if not func.pattern in line:
                    continue
                
                if not func.enabled:
                    log(f'Skipping function for entry {func.alias} as it is disabled')
                    continue

                arguments = line.split('/')[1:] # Drop the first argument (the function pattern/command)
                arguments = [x.strip() for x in arguments if x.strip() != ''] # Remove empty arguments
                for arg in arguments:
                    log(f'Argument received: {arg}')

                if len(arguments):
                    log(f'Running function for entry: {func.alias} with arguments: {arguments}')
                else:
                    log(f'Running function for entry: {func.alias} with no arguments')

                # Run the function

                # Pass whole line if requested (TODO: reconsider this)
                if func.line == True and not func.arguments:
                    func.func(line)

                elif type(func.arguments) == int:
                    if func.arguments == 0:
                        func.func()
                    elif len(arguments) == func.arguments:
                        func.func(arguments)
                    else:
                        log(f'Argument count mismatch, needed {func.arguments}, provided {len(arguments)}')

                elif isinstance(func.arguments, list):
                    if len(arguments) in func.arguments:
                        func.func(arguments)
                    else:
                        log(f'Argument count mismatch, needed one of {func.arguments}, provided {len(arguments)}')
                else:
                    log(f'Internal argument conflict: needed {func.arguments} provided {arguments}')

                    filelogline = False

            if filelogline == True:
                log_to_console_file(line)
        # qconsole.log
        file.truncate(0)
        file.close()
