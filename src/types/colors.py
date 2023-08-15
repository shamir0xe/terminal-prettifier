from enum import Enum


class Colors(Enum):
    BLACK = "\033[1;30;40m"
    RED = "\033[1;31;40m"
    GREEN = "\033[1;32;40m"
    YELLOW = "\033[1;33;40m"
    BLUE = "\033[1;34;40m"
    MAGENTA = "\033[1;35;40m"
    CYAN = "\033[1;36;40m"
    WHITE = "\033[1;37;40m"
    RESET = "\033[0m"
