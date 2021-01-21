import random
import enum
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, '..')))

from TerminalPrettifier.libs.PythonLibrary.buffer_io import (StandardInputReader)
from TerminalPrettifier.libs.PythonLibrary.utils import (debug_text)
from TerminalPrettifier.src.prettifier_config import *
from TerminalPrettifier.src.prettifier_stream import *

# class Log:
#     def __init__(self, filename=".prettifier_log"):
#         self.filename = filename

#     def add_log(self, string):
#         append_to_file(self.filename, string + '\n')


def main():
    # log_writer = Log()
    input_reader = StandardInputReader(log_writer=None)
    config = PrettifierConfig()
    stream = PrettifierStream(input_reader, config)
    stream.stream()


if __name__ == '__main__':
    main()
