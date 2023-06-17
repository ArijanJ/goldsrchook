import util.exec as exec
from util.logs import log_wrapper as log

from command_builder.command import Command
from instructions.amxmodx import slay as amx_slay

def slay(args):
    names = args
    command = Command()
    for name in names:
        log(f'Slaying {name}')
        command += amx_slay(name)
    command.run()