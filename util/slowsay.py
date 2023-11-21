from util.logs import log_wrapper as log
from datetime import datetime
import time

from command_builder.command import Command
from instructions.util import condebug
from instructions.info import echo
from instructions.speech import say

# First message
last_message_time = datetime.min

# + .05 for variable 50ms of ping
spamDelay = 1.55

def slowsay(string):
    global last_message_time
    if last_message_time == None:
        last_message_time = datetime.now()

    log(f'Attempting to slowsay: {string}')

    in_spam = (datetime.now() - last_message_time).total_seconds() < spamDelay

    if in_spam:
        timeout_fractions = 0 # Reset before loop

        while(in_spam or timeout_fractions > spamDelay * 20):
            timeout_fractions += 1
            time.sleep(0.1)

    last_message_time = datetime.now()
    
    Command(
        condebug(),
        echo(f'Slowsaying {string}'),
        say(string),
        condebug()
    ).run()
