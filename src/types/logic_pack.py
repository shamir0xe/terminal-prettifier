from src.types.characters import Characters
from dataclasses import dataclass


@dataclass
class LogicPack:
    index: int
    char_type: Characters
    logic: bool = True

    def get(self) -> tuple:
        return self.index, self.char_type, self.logic
