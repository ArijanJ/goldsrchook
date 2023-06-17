from util.logs import log_wrapper as log
from datetime import datetime, timedelta
import time

from command_builder.command import Command
from instructions.util import condebug
from instructions.info import echo
from instructions.speech import say

# First message
last_message_time = datetime(1, 1, 1)

# + .05 for variable 50ms of ping
spamDelay = 1.55

def slowsay(string):
    global last_message_time
    if last_message_time == None:
        last_message_time = datetime.now()

    log("Attempting to slowsay :" + string)

    if (datetime.now() - last_message_time).total_seconds() < spamDelay:
        timeout_fractions = 0

        while((datetime.now() - last_message_time).total_seconds() < spamDelay or timeout_fractions > spamDelay * 20):
            timeout_fractions += 1
            log((datetime.now()- last_message_time).total_seconds())
            time.sleep(0.1) # TODO: ???????

    last_message_time = datetime.now()
    
    Command(
        condebug(),
        echo('Slowsaying ' + string),
        say(string),
        condebug()
    ).run()