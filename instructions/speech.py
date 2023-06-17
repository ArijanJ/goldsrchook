from command_builder.instruction import Instruction

class amx_say(Instruction):
    def __init__(self, message):
        message = self.clean(message)
        self.text = f'amx_say "{message}";'

class say(Instruction):
    def __init__(self, message):
        message = self.clean(message)
        self.text = f'say "{message}";'

class team_say(Instruction):
    def __init__(self, message):
        message = self.clean(message)
        self.text = f'say_team "{message}";'