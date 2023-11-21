class Instruction:
    """Get the current ready-to-execute text from the instruction"""
    def get_text(self) -> str:
        return self.text

    """All subclasses must call this after receiving arguments"""
    def clean(self, text) -> str:
        return text.replace('"', '\'\'')

    """Print the instruction for debugging purposes"""
    def print(self):
        print(self.get_text())
