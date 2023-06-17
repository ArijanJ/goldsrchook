from util.logs import log_wrapper as log 
import random

from command_builder.command import Command
from instructions.speech import say

def generate(args):
    randcount = 1
    start = 1
    end = 6 # For dice

    # syntax:  random/5       5x(1-6)     OR 
    #          random/2/10    (2-10)    OR
    #          random/2/5/15  2x(5-15)
    if len(args) == 1:
        randcount = int(args[0])
    elif len(args) == 2:
        start = int(args[0])
        end = int(args[1])
    elif len(args) == 3:
        randcount = int(args[0])
        start = int(args[1])
        end = int(args[2])

    string = ""

    if start > end:
        start, end = end, start

    for i in range(randcount):
        number = random.randrange(start, end+1) # ...?
        string += f'{str(number)}'
        if i != randcount - 1: # If not last element, add comma
            string += ", "

    log(string)

    output = str(randcount) # 4 [numbers between 2 and 10:]

    output += " random"

    if randcount == 1:
        output += " number "
    else:
        output += " numbers "
    output += f'between {start, end}: {string}'

    Command().add(
        say(output)
    ).run()