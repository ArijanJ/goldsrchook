# TODO: Figure out why Ï (or something else entirely) crashes the program

from command_builder.command import Command
from instructions.info import echo
from instructions.util import condebug, toggleconsole

from util.logs import log_wrapper as log

line_limit = 1000

def find(args):
    match = args[0]
    if args[0] == 'setlimit' and len(args) == 2:
        new_limit = int(args[1])
        message = "Setting consearch limit to " + str(new_limit)
        log(message)

        Command().add(
            echo(message),
        ).run()

        global line_limit
        line_limit = new_limit
        return

    # Regular operation
    log(f"Looking for: {match} in the last {line_limit} lines")
    
    result = Command().add(condebug())
    for line in find_all(match):
        result.add(echo(line))
    result.add(condebug())
    # Show the console and run
    result.add(toggleconsole()).run()

# Usage: `for line in find_all('killed')`
def find_all(text):
    # This file is handled by the console controller
    with open("consolelog.txt", "r", encoding='latin-1') as file:
        lines = file.readlines()
        search_range = lines[-line_limit:]
        for line in search_range:
            line = line.strip().strip(';').strip('"').strip('\'')#.encode()
            if text.lower() in line.lower():
                log("Found match: " + line)
                line = line.encode('ascii', 'replace').decode()
                yield line

def find_first_match(text):
    # This file is handled by the console controller
    with open("consolelog.txt", "r", encoding='latin-1') as file:
        lines = file.readlines()
        search_range = lines[-line_limit:]
        search_range.reverse()
        for line in search_range:
            line = line.strip().strip(';').strip('"').strip('\'')#.encode()
            if text.lower() in line.lower():
                log("Found match: " + line)
                line = line.encode('ascii', 'replace').decode()
                return line
        # Not found
        return