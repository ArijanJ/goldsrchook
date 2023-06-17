from command_builder.instruction import Instruction

class amx_say(Instruction):
    def __init__(self, message):
        message = self.clean(message)
        self.text = f'amx_say "{message}";'

class gag(Instruction):
    def __init__(self, name, time):
        self.text = f'amx_gag "{name}" {time};'
        
class gag_with_reason(Instruction):
    def __init__(self, name, time, reason):
        self.text = f'amx_gag "{name}" {time} "{reason}";'
        
class slay(Instruction):
    def __init__(self, name):
        self.text = f'amx_slay "{name}";'