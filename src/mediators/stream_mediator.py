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
            if word == '':
                continue
            if self.ta.check_edits(word):
                self.raw_print(word)
                continue
            self.print_word(word, self.ta.color_string(word))
