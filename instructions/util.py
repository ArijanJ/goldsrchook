from command_builder.instruction import Instruction

class condebug(Instruction):
    def __init__(self):
        self.text = 'condebug;'
        
class toggleconsole(Instruction):
    def __init__(self):
        self.text = 'toggleconsole;'
        
class menuselect(Instruction):
    def __init__(self, item: int):
        self.text = f'menuselect {item};'