# tile_types.py (curses version)
import curses

class Tile:
    def __init__(self, walkable: bool, transparent: bool, char: int, color_pair: int, attributes: int = curses.A_NORMAL):
        self.walkable = walkable
        self.transparent = transparent
        self.char = char
        self.color_pair = color_pair
        self.attributes = attributes
    
    def get_char_attrs(self):
        return self.char, curses.color_pair(self.color_pair) | self.attributes

# Initialize colors (call this after curses.initscr())
def init_colors():
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)   # floor
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)  # wall

# Define tiles
floor = Tile(True, True, ord(' '), 1)
wall = Tile(False, False, ord(' '), 2)