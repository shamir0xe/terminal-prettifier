from libs.pylib.config.config import Config
from libs.pylib.buffer_io.buffer_reader import BufferReader
from src.types.colors import Colors
from src.types.logic_pack import LogicPack
from src.types.characters import Characters
from src.actions.check_logic import check_logic
from src.actions.color_mapper import color_mapper


EDITS_ARR = ["\033[F", "\033[A"]


class TextActions:
    def __init__(self) -> None:
        self.escapes = [*Config.read("basics.escapes"), chr(10), chr(32)]
        self.dots = Config.read("basics.dots")
        self.separators = Config.read("basics.separators")
        self.parentheses = Config.read("basics.parentheses")
        self.operators = Config.read("basics.operators")
        self.edits = EDITS_ARR
        self.switcher = Config.read("user.switcher")

    def check_escape(self, reader: BufferReader) -> bool:
        # check whether a char is an escape
        return self.__is_escape(reader.next_char(True))

    def check_edits(self, word: str) -> bool:
        # check if the words is {backspace} or etc
        return word in self.edits

    def __is_digit(self, char: str) -> bool:
        return ord("0") <= ord(char) <= ord("9")

    def __is_alphabet(self, char: str) -> bool:
        return ord("a") <= ord(char.lower()) <= ord("z")

    def __is_separator(self, char: str) -> bool:
        return char in self.separators

    def __is_operator(self, char: str) -> bool:
        return char in self.operators

    def __is_dot(self, char: str) -> bool:
        return char in self.dots

    def __is_escape(self, char: str) -> bool:
        return char in self.escapes

    def __is_parentheses(self, char: str) -> bool:
        return char in self.parentheses

    def get_character_type(self, char: str) -> Characters:
        # print(f'char: {char}')
        if self.__is_digit(char):
            return Characters.DIGIT
        elif self.__is_alphabet(char):
            return Characters.ALPHABET
        elif self.__is_dot(char):
            return Characters.DOT
        elif self.__is_escape(char):
            return Characters.ESCAPE
        elif self.__is_separator(char):
            return Characters.SEPARATOR
        elif self.__is_operator(char):
            return Characters.OPERATOR
        elif self.__is_parentheses(char):
            return Characters.PARENTHESES
        return Characters.ESCAPE

    def __index_bounderies(self, word: str, idx: int, char_type: Characters) -> tuple:
        first, last = idx, idx
        while last < len(word) and self.get_character_type(word[last]) is char_type:
            last += 1
        while first >= 0 and self.get_character_type(word[first]) is char_type:
            first -= 1
        return first, last

    def range_type(self, word: str, idx: int) -> Characters:
        char_type = self.get_character_type(word[idx])
        if char_type is Characters.DIGIT:
            first_idx, last_idx = self.__index_bounderies(word, idx, Characters.DIGIT)
            if not check_logic(
                word,
                lambda char: self.get_character_type(char),
                LogicPack(first_idx, Characters.ALPHABET, False),
                LogicPack(last_idx, Characters.ALPHABET, False),
            ):
                char_type = Characters.ALPHABET
        return char_type

    def character_switcher(self, char_type: Characters) -> Colors:
        return color_mapper(self.switcher[char_type.value])

    def color_string(self, word: str) -> list:
        colors = list(map(lambda _: Colors.RESET, word))
        # changing base character colors
        for idx, _ in enumerate(word):
            colors[idx] = self.character_switcher(self.range_type(word, idx))
        return colors
