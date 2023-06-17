from util.logs import log_wrapper as log

prefixes = []

def load():
    with open("prefixes.txt", "r") as file:
        log("Opened prefixes.txt")
        lines = file.readlines()
        for line in lines:
            prefixes.append(line.strip())
            log("Found prefix: " + line.strip())

blacklist = [
    "*DEAD* ",
    "*ALIVE* ",
    "*SPEC* ",
    "(Counter-Terrorist)",
    "(Terrorist)"
]

def clean(name: str) -> str:
    for prefix in prefixes:
        print("Replacing prefix " + f'[{prefix}]')
        name = name.replace(f'[{prefix}] ', '')

    for item in blacklist:
        name = name.replace(item, '')
        
    return name.strip().replace("`", "&#96;")
