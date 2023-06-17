from util.logs import log_wrapper as log

from command_builder.command import Command
from instructions.util import menuselect
from instructions.info import echo

from command_builder.instruction import Instruction
class pmodmenu(Instruction):
    def __init__(self):
        self.text = 'pmodmenu;'

items = ['gravity', 'speed', 'invis', 'laser', 'antiflash', 'mj', 'bhop', 'hp', 'parachute']

pmod_buy_option  = 1
pmod_sell_option = 2
items_per_page   = 7
page_back_key    = 8
page_forward_key = 9
exit_menu_key    = 0

def select_item(item: int) -> Command:
    command = Command()
    index = items.index(item) + 1
    page = (index / items_per_page)

    currentpage = 1
    while currentpage < page:
        command.add(menuselect(page_forward_key))
        index -= items_per_page # If hp is at index 8, move to index 1
        currentpage += 1

    return command.add(menuselect(index)) # Eventually select the item

def buy(item: int) -> Command:
    if item not in items:
        log(f'Invalid item to buy: {item}')
        return Command(
            echo(f'Item {item} does not exist, therefore it cannot be bought')
        )

    # Buy the item
    return Command(
        pmodmenu(), 
        menuselect(pmod_buy_option), 
    ).extend(select_item(item))

def sell(item: int) -> Command:
    if item not in items:
        log(f'Invalid item to sell: {item}')
        return Command(
            echo(f'Item {item} does not exist, therefore it cannot be sold')
        )

    # Sell the item
    return Command(
        pmodmenu(),
        menuselect(pmod_sell_option)
    ).extend(select_item(item))

def sell_all_items() -> Command:
    command = Command()
    for item in items:
        command += sell(item)
    return command 

buy_aliases  = ['buy' , 'b', 'k']
sell_aliases = ['sell', 's', 'p']

# Usage: pmod/buy/ability
#    OR: pmod/sell/ability
def process(args):
    action = args[0]
    item   = args[1]
    log(f'Trying to run action {action} on item {item}')

    if action in buy_aliases:
        log(f'Trying to buy {item}')
        log('Selling all items...')
        command = sell_all_items()
        command.extend(buy(item)).run()
    elif action in sell_aliases:
        log(f'Trying to sell {item}')
        if item == 'all':
            log('Selling all items...')
            sell_all_items().run()
            return
        (buy(item) + sell(item)).run()
    else:
        log(f'Action {action} does not exist.')