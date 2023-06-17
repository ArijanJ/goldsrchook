## Pseudo-IPC for GoldSrc-based games (mainly Counter-Strike 1.6)

## Quick start:

`./main_example.py` contains enough information, if you want to jump right into it.

## In-game setup:

The only things you need to do are:
- Enable condebug:

``` quake
condebug;
```

- Bind your 'pause' key to `exec configdir/goldsrchook/exec.cfg`:

``` quake
bind pause "exec configdir/goldsrchook/exec.cfg";
```

The program currently assumes that `main.py` is three directories deeper than `qconsole.log` - you can change this in `console.py`.

You can change which key is used for execution in `util/exec.py`.

For easy access to your functions, it's also recommended to bind a key to `messagemode echo`:

``` quake
bind q "messagemode echo";
```

This allows you to use `q` as a prompt for calling all of your commands.

## Writing plugins

All of your plugins (custom commands) should go in either `cmds/` or `util/`.

To write a custom command, create `cmds/mycommand.py` and import:

``` python
from command_builder.command import Command
```

After this, import the instructions that you will need from `instructions/`:

``` python
from instructions.speech import say
from instructions.info import echo
from instructions.util import toggleconsole
```

Next, define your receiver function:

``` python
def add(args):
```

Write all of your custom logic and construct a `command_builder.command.Command`:

``` python
    result = int(args[0]) + int(args[1)]
    my_command = Command()
```

A command can have multiple instructions attached to itself.
Use command.add() to add an instruction and command.extend() to add another Command.
You can also use the + operator, and it will detect what you're trying to add.

``` python
    # These are all valid.
    
    my_command.add(echo("Hi!"))
    my_command.extend(Command(echo("Hi!")))
    my_command += echo("Hi!")
    my_command.add(
        echo("Boo!"),
        toggleconsole()
    )
```

If you plan on echoing tons of stuff, it's recommended to add a `condebug()` instruction before and after the command.
This will prevent `console.py` from logging your echos and getting confused.

When your command is ready, you can run `command.run()` to execute it in-game, or `command.print()` if you want to check it first.

``` python
    Command(say(f'Your result is {result}!')).run()
```

Of course, you need to register your new `add()` function:

`cmds/main.py`

``` python
import cmds.mycommand as mycommand

# register_function(pattern, callback,      alias, argument_count)
  register_function("add/",  mycommand.add, 'add', 2)
```

From now on, when `console.py` detects 'add/', it will split up its arguments and (if the correct number are provided) send them to `mycommand.add`.

## Writing instructions

When you need to use a new instruction, you need to define it like such:

``` python
from command_builder.instruction import Instruction

# You can name the instruction arbitrarily,
# provided that its .text is correct.
class change_name(Instruction):
    def __init__(self, new_name):
        self.text = f'name "{new_name}";'
```

The instruction's `.text` is what gets executed when you `.run()` a Command containing it.
Make sure it conforms to Half-Life standards - don't forget the semicolon.

You should mainly put your instructions in `instructions/`, however if they're only going to be used in one file, you can define them locally, as done in `cmds/pmodmenu.py`.

You can then run your new instruction by adding it to a Command:

`cmds/mynamechange.py`
``` python
def set_my_name(args):
    requested_name = args[0]
    Command(change_name(requested_name)).run()
```
... and registering it as before.

That's all you need to know, enjoy!

P.S. *When* you get in trouble, remove `qconsole.log` and `consolelog.txt`.
