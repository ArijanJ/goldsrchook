from cmds import consearch
from command_builder.command import Command
from instructions.info import echo
from instructions.speech import amx_say

from util.logs import log_wrapper as log
from datetime import datetime, timedelta
from util.slowsay import slowsay
import util.colorchat as cc

import time
import math

# TODO: Fix headshots

from dataclasses import dataclass

@dataclass
class Death:
    killer: str
    victim: str
    method: str
    time_string: str

def find_death(args) -> Death:
    match = args[0]
    death_line = consearch.find_first_match('killed ' + match)
    if not death_line:
        log("Could not find " + match + "'s death, sorry!'")
        Command(echo(f'Could not find {match}\'s death, sorry!')).run()
        return

    log(f'Death found: {death_line}')

    death_line = death_line.replace('***', '')
    death_line = death_line.strip()
    #log(f'stripped line: {killerLine}')

    # Get rid of timestamp from util.logs
    splitLine = death_line.split()
    
    print(f'splitLine: {splitLine}')
    timestamp = splitLine[0].strip()[:-1]
    death_line = death_line.split(' ', 1)[1]

    # Begin at start and go until 'killed'
    killer = death_line[:death_line.find('killed')].strip()

    # From end of killed to beginning of ' with '
    victim = death_line[death_line.find('killed') + 7:death_line.find(' with ')]

    # Method
    method = death_line.rsplit(' ', 1)[1]

    log(f'Parsed {death_line}')

    log(f'Killer: [{killer}]')
    log(f'Victim: [{victim}]')
    log(f'Method: [{method}]')

    # Timestamp
    log("Timestamp: " + timestamp)

    # Turn into datetime object
    time_of_death = datetime.strptime(timestamp, "[%H:%M:%S]")
    
    # Calculate time difference
    seconds = (datetime.now() - time_of_death).seconds
    if seconds/60 < 1:
        time_string = f'{str(seconds)} seconds ago'
    elif seconds/60 == 1:
        time_string = 'a minute ago'
    elif seconds/60 >= 1:
        time_string = f'{str(math.floor(seconds/60))} minutes ago'

    return Death(killer, victim, method, time_string)

def amx_say_death(args):
    death = find_death(args)

    if not death:
        return
    
    print(death)

    Command(
        amx_say(f'{cc.blank}{cc.team}{death.killer} {cc.yellow}->{cc.team} {death.victim} {cc.yellow}({death.method}) - {cc.green}{death.time_string}{cc.yellow}')
    ).run()

def slowsay_death(args):
    death = find_death(args)
    
    if not death:
        return
    
    print(death)

    # Headshot
    # if 'with a headshot' in killer_line:
    #     slowsay(f'{killer} -> {victim} ({method}) [HS!] - {timeString}', True)

    # # Not a headshot
    # else:
    slowsay(f'{death.killer} -> {death.victim} ({death.method}) - {death.time_string}')

    # # Headshot
    # if 'with a headshot' in killerLine:
    #     exec.run(f'amx_say "{cc.blank}{cc.team}{killer} {cc.yellow}->{cc.team} {victim} {cc.yellow}({method}) {cc.green}[HS!] {cc.yellow}- {cc.green}{timeString}{cc.yellow}"')

    # # Not a headshot
    # else:
    #     exec.run(f'amx_say "{cc.blank}{cc.team}{killer} {cc.yellow}->{cc.team} {victim} {cc.yellow}({method}) {cc.yellow}- {cc.green}{timeString}{cc.yellow}"')