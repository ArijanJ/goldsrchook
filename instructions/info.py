from command_builder.instruction import Instruction

class echo(Instruction):
    # TODO: Consider
    # def __init__(self, *lines: list[str]):
    #     for line in lines:
    def __init__(self, message):
        message = self.clean(message)
        self.text = f'echo "{message}";'

"""Print one or more newlines"""
class newline(Instruction):
    def __init__(self, count: int = 1):
        self.text = "echo; " * count