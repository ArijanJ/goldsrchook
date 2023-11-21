from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime, timedelta
from util.logs import *
from util.logs import log_wrapper as log
from util.function import function

my_observer = Observer()

# Assuming this is 3 directories deep in the main Half-Life folder
path = "../../../"
console = path + "qconsole.log"

func_list: list[function] = []
def run(passed_list):
    global func_list
    func_list = passed_list
    log(f'Initializing with {console}:')
    with open(console, 'r') as f:
        print(f.readlines())

    longest_alias = max(map(lambda f : len(f.alias), func_list))
    longest_pattern = max(map(lambda f : len(f.pattern), func_list))
    
    for func in func_list:
        print(f'{func.alias}'.ljust(longest_alias+1) + f'[{func.pattern.strip()}]'.ljust(longest_pattern+3) + '[{}]'.format('X' if func.enabled else ' '))

    my_observer.schedule(EventHandler(), path, recursive=False)
    my_observer.start()

class EventHandler(FileSystemEventHandler):
    def __init__(self):
        self.last_modified = datetime.now()

    def on_modified(self, event):
        if datetime.now() - self.last_modified < timedelta(seconds=0.1):
            return

        self.last_modified = datetime.now()

        if event.src_path != console:
            return

        separator()

        file = open(console, 'r+', encoding='utf-8')
        for line in list(reversed(file.readlines()))[:25]:
            cleanLine = line.strip()
            log(cleanLine)
            for func in func_list:
                if not func.pattern in line:
                    continue
                
                if not func.enabled:
                    log(f'Skipping function for entry {func.alias} as it is disabled')
                    continue

                arguments = line.split('/')[1:] # Drop the first argument (pattern)
                arguments = [x.strip() for x in arguments if x.strip() != ''] # Remove empty arguments
                for arg in arguments:
                    log(f'Argument received: {arg}')

                log(f'Running function for entry: {func.alias} with ' 'no arguments' if not len(arguments) else f'with arguments: {arguments}')

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
                        log(f'Argument count mismatch, {func.arguments} needed, {len(arguments)} provided')

                elif isinstance(func.arguments, list):
                    if len(arguments) in func.arguments:
                        func.func(arguments)
                    else:
                        log(f'Argument count mismatch, needed one of {func.arguments}, {len(arguments)} provided')
                else:
                    log(f'Internal argument conflict: {func.arguments} needed, {arguments} provided')

            log_to_console_file(line)
        # qconsole.log
        file.truncate(0)
        file.close()

