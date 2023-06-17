import time
from colorama import init as colorama_init

import console as console

from util.function import func_list
from util.function import register_function

# Housekeeping
from util.utilfuncs import plugin_handler

# Pretty-ish output
colorama_init()

# Import all of your custom commands from cmds/
# They are imported as modules to avoid name conflicts.
import cmds.add as add
import cmds.random as random
import cmds.pmodmenu as pmodmenu
import cmds.whokilled as whokilled
import cmds.consearch as consearch
import cmds.slay as slay
import cmds.say as say

import util.slowsay as slowsay
import util.namereplace as namereplace

# Optional - for some chat processing
namereplace.load()

# Register all of your commands
#
# Format:
# register_function(pattern, func, alias, arguments, (keyworded arguments))
#
# 'arguments' can either be an integer of the exact number of arguments needed ...
# or it can be a list [1, 2, 3] of valid counts of arguments that the function can take.

# This was imported as a function, not a module (line 10).
# %plugin/verb[/alias]
register_function("%plugin/", plugin_handler, 'plugin', [1, 2])

# add/x/y
register_function("add/", add.add, 'add', 2)

# [rvtg]say/message
register_function("rsay/", say.rainbowsay, 'rsay', 1)
register_function("vsay/", say.vanillasay, 'vsay', 1)
register_function("tsay/", say.teamsay,    'tsay', 1)
register_function("gsay/", say.greensay,   'gsay', 1)

# cs/[text]||[setlimit/new_limit]
register_function("cs/", consearch.find, 'consearch', [1, 3])

# slay/names
register_function("slay/", slay.slay, 'slay', [1, 2, 3, 4, 5])

# wk/victim_name
register_function("wk_say/", whokilled.slowsay_death, 'whokilled', 1)
register_function("wk/", whokilled.amx_say_death, 'wk_amx', 1)

register_function("slowsay/", slowsay.slowsay, 'slowsay', 1)

# pmod/[buy||sell]/item
register_function("pmod/", pmodmenu.process, 'pmodmenu', 2)

# random/5       5x(1-6)   OR 
# random/2/10    (2-10)    OR
# random/2/5/15  2x(5-15)
register_function("random/", random.generate, 'random', [1, 2, 3])

# Send over the list
console.run(func_list)

try:
    while (True):
        time.sleep(.1)
except KeyboardInterrupt:
    console.stop()