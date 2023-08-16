import random
from typing import List
from src.types.colors import Colors


def color_mapper(color_name: str) -> Colors:
    # mapping name to the corresponding type
    color_name = color_name.lower()
    for color in Colors:
        if color_name == color.name.lower()[: len(color_name)]:
            return color
    return None


def string_color_mapper(color_name: str, length: int) -> List[Colors]:
    # mapping array of colors, to the given {color_name}
    # {color_name} can be either
    #   1) the name of the color or,
    #   2) the string of the first characters of corresponding color names
    colors = []
    color = color_mapper(color_name)
    if not color is None:
        # it's the first type
        colors = [color]
    else:
        # it's the second type
        for char in color_name:
            char = char.lower()
            found = False
            for original_color in Colors:
                if original_color is Colors.RESET:
                    continue
                if original_color.name.lower()[0] == char:
                    colors.append(original_color)
                    found = True
                    break
            if not found:
                colors.append(Colors.BLACK)

    # expanding the array to reach {length}
    cur_length = len(colors)
    base_length = cur_length
    while cur_length < length:
        colors.append(colors[cur_length % base_length])
        cur_length += 1
    return colors
    
