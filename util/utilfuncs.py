from util.function import func_list as func_list
from util.logs import log_wrapper as log

from command_builder.command import Command

from instructions.util import condebug, toggleconsole
from instructions.info import echo, newline

def plugin_handler(args):
    verb = args[0]
    if verb not in ['list', 'enable', 'disable']:
        log(f'Unknown verb supplied: {verb}')
    match verb:
        case 'list':
            list_plugins()
        case 'enable':
            enable_plugin(args[1])
        case 'disable':
            disable_plugin(args[1])
        case _:
            log(f'Unknown verb supplied: {verb}')


def list_plugins():
    disabled_funcs = []

    command = Command()
    command.add(
        condebug(),
        newline(),
        echo('Loaded plugins:'),
        newline()
    )

    for func in func_list:
        if func.enabled:
            command.add(echo(func.alias))
        else:
            disabled_funcs.append(func)

    if not disabled_funcs: 
        command.run() # We're done
        return

    command.add(
        newline(),
        echo('Unloaded plugins:'),
        newline()
    )

    for func in disabled_funcs:
        command.add(echo(func.alias))
    
    command.add(condebug(), toggleconsole()).run()

def enable_plugin(plugin):
    log('Enabling plugin ' + plugin)

    command = Command().add(
        echo('Enabling plugin ' + plugin),
    )

    for func in func_list:
        if func.alias == plugin:
            func.enabled = True
            log(f'Enabled plugin {plugin}')
            command.add(
                echo('Enabled plugin ' + plugin), 
                toggleconsole()
            ).run()
            return

    log(f'Could not find plugin {plugin}')

def disable_plugin(plugin):
    log(f'Disabling plugin {plugin}')

    for func in func_list:
        if func.alias == plugin:
            func.enabled = False
            log('Disabled plugin')
            Command().add(
                echo('Disabled plugin ' + plugin)
            ).run()
            return

    log(f'Could not find plugin {plugin}')
