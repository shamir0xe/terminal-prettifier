from __future__ import annotations
from functools import reduce
from typing import List
from libs.pylib.buffer_io.buffer import Buffer
from libs.pylib.buffer_io.buffer_reader import BufferReader
from src.actions.text_actions import TextActions
from src.types.colors import Colors


class StreamMediator:
    def __init__(self, reader: BufferReader) -> None:
        self.reader = reader

    @staticmethod
    def set_buffer(buffer: Buffer) -> StreamMediator:
        return StreamMediator(reader=BufferReader(buffer))

    def read_config(self) -> StreamMediator:
        # reading config and initialize ta with it
        # TODO
        self.ta = TextActions()
        return self

    def print_word(self, word: str, colors_arr: List[Colors]) -> None:
        # print("\033[1;37;40m \033[2;37:40m TextColour BlackBackground          TextColour GreyBackground                WhiteText ColouredBackground\033[0;37;40m\n")
        # print("\033[1;30;40m Dark Gray      \033[0m 1;30;40m            \033[0;30;47m Black      \033[0m 0;30;47m               \033[0;37;41m Black      \033[0m 0;37;41m")
        # print("\033[1;31;40m Bright Red     \033[0m 1;31;40m            \033[0;31;47m Red        \033[0m 0;31;47m               \033[0;37;42m Black      \033[0m 0;37;42m")
        # print("\033[1;32;40m Bright Green   \033[0m 1;32;40m            \033[0;32;47m Green      \033[0m 0;32;47m               \033[0;37;43m Black      \033[0m 0;37;43m")
        # print("\033[1;33;40m Yellow         \033[0m 1;33;40m            \033[0;33;47m Brown      \033[0m 0;33;47m               \033[0;37;44m Black      \033[0m 0;37;44m")
        # print("\033[1;34;40m Bright Blue    \033[0m 1;34;40m            \033[0;34;47m Blue       \033[0m 0;34;47m               \033[0;37;45m Black      \033[0m 0;37;45m")
        # print("\033[1;35;40m Bright Magenta \033[0m 1;35;40m            \033[0;35;47m Magenta    \033[0m 0;35;47m               \033[0;37;46m Black      \033[0m 0;37;46m")
        # print("\033[1;36;40m Bright Cyan    \033[0m 1;36;40m            \033[0;36;47m Cyan       \033[0m 0;36;47m               \033[0;37;47m Black      \033[0m 0;37;47m")
        # print("\033[1;37;40m White          \033[0m 1;37;40m            \033[0;37;40m Light Grey \033[0m 0;37;40m               \033[0;37;48m Black      \033[0m 0;37;48m")
        new_word = reduce(
            lambda a, b: a + b,
            map(
                lambda char, color: f"{color.value}{char}{Colors.RESET.value}",
                list(word),
                colors_arr,
            ),
        )
        print(new_word, end="", flush=True)

    def raw_print(self, word: str) -> None:
        print(word, end="", flush=True)

    def stream(self) -> None:
        while not self.reader.eof:
            while self.ta.check_escape(self.reader):
                self.raw_print(self.reader.next_char())
            word = self.reader.next_string()
            if self.ta.check_edits(word):
                self.raw_print(word)
                continue
            self.print_word(word, self.ta.color_string(word))
