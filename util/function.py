func_list = []

class function:
    def __init__(self, pattern, func, alias='', arguments=0, line=False, enabled=True):
        self.pattern = pattern
        self.func = func
        self.alias = alias
        # The number of arguments this function takes
        self.arguments = arguments
        self.line = line
        self.enabled = enabled

# TODO: Maybe get rid of this entirely somehow?
def register_function(pattern, func, alias, arguments, line=False, enabled=True) -> function:
    func_list.append(
        function(
            pattern,
            func,
            alias,
            arguments,
            line,
            enabled
        ))
    return func