from enum import Enum


class Colors(Enum):
    BLACK = "\033[1;30;30m"
    RED = "\033[1;31;31m"
    GREEN = "\033[1;32;32m"
    YELLOW = "\033[1;33;33m"
    BLUE = "\033[1;34;34m"
    MAGENTA = "\033[1;35;35m"
    CYAN = "\033[1;36;36m"
    WHITE = "\033[1;37;37m"
    RESET = "\033[0m"
