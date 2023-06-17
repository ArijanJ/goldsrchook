from command_builder.instruction import Instruction
from util.exec import run

class Command:
    """Only for initialization"""
    def __init__(self, *instructions: list[Instruction]):
        self.instructions: list[Instruction] = list(instructions)

    """Add an Instruction to the command list"""
    def add(self, *instructions: list[Instruction]):
        for instruction in instructions:
            self.instructions.append(instruction)
        return self

    """Get the current ready-to-execute text from the command"""
    def get_text(self) -> str:
        text = ''
        for instruction in self.instructions:
            text += instruction.get_text() + '\n'
        return text

    """Extend this command with another command"""
    def extend(self, *commands: list['Command']):
        for command in commands:
            # Copy over each instruction
            for instruction in command.instructions:
                self.instructions.append(instruction)
        return self

    """Run this command, no questions asked"""
    def run(self):
        run(self.get_text())

    """Print the command"""
    def print(self):
        for instruction in self.instructions:
            print(instruction.get_text())
            
    # """Print the command for debugging purposes"""
    # def debug(self):
    #     for instruction in self.instructions:
    #         instruction.print()
            
    """If other is a Command, extend this command with it, otherwise add it as an Instruction"""
    def __add__(self, other: 'Command'):
        if isinstance(other, Command):
            return self.extend(other)
        elif isinstance(other, Instruction):
            return self.add(other)