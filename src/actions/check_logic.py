from typing import List, Callable
from src.types.logic_pack import LogicPack

@staticmethod
def check_logic(word: str, fn: Callable, *args: List[LogicPack]) -> bool:
    # returning whether conditions provided by {args} are
    # met in the string {word}
    # {fn} is get_character_type function
    result = True
    for logic_pack in args:
        index, char_type, logic = logic_pack.get()
        if not in_range(word, index):
            result &= logic == False
            continue
        result &= (fn(word[index]) is char_type) == logic
    return result

@staticmethod
def in_range(word: str, idx: int) -> bool:
    return 0 <= idx < len(word)
