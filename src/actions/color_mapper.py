from src.types.colors import Colors


def color_mapper(color_name: str) -> Colors:
    # mapping name to the corresponding type
    color_name = color_name.lower()
    for color in Colors:
        if color_name == color.name.lower()[: len(color_name)]:
            return color
    return None
