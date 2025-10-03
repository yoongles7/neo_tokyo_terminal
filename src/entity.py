from typing import Optional

class Entity:
    """A generic object ot represent playerd, enemies, items, etc.
    """
    def __init__(self, x: int, y: int, char: str, color: int):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        
    def move(self, dx: int, dy: int) -> None:
        # Move the entityt by a given amount
        self.x += dx
        self.y += dy