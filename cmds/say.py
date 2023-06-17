from command_builder.command import Command
from instructions.speech import *

from util import colorchat as cc

def rainbowsay(args):
    text = args[0]
    string = cc.blank
    count = 1
    for char in text:
        if char == ' ':
            string =+ char
            continue
        elif count % 3 == 0:
            string = string + cc.green  + char
        elif count % 2 == 0:
            string = string + cc.team + char
        else:
            string = string + cc.yellow + char

        count = count + 1

    Command().add(
        amx_say(string)
    ).run()

def teamsay(args):
    text = args[0]
    Command().add(
            amx_say(f'{cc.blank}{cc.team}{text}')
        ).run()

def greensay(args):
    text = args[0]
    Command().add(
            amx_say(f'{cc.blank}{cc.green}{text}')
        ).run()

def yellowsay(args):
    text = args[0]
    Command().add(
            amx_say(f'{cc.blank}{cc.yellow}{text}')
        ).run()

# Use case?
def vanillasay(args):
    text = args[0]
    Command().add(
            say(f'{cc.blank}{cc.yellow}{text}')
        ).run()