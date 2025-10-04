import numpy as np
import curses
from typing import Tuple

class GameMap:
    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        
        # Create numpy arrays for tile properties
        self.walkable = np.full((width, height), fill_value=True, order="F")
        self.transparent = np.full((width, height), fill_value=True, order="F")
        self.tile_chars = np.full((width, height), fill_value=ord(' '), order="F")
        self.tile_color_pairs = np.full((width, height), fill_value=1, order="F")  # Default to floor color
        self.tile_attrs = np.full((width, height), fill_value=curses.A_NORMAL, order="F")
        
        # Set floor tiles
        self.tile_color_pairs[:,:] = 1  # Floor color pair
        
        # Set wall
        self.walkable[30:33, 22] = False
        self.transparent[30:33, 22] = False
        self.tile_color_pairs[30:33, 22] = 2  # Wall color pair

    def in_bounds(self, x: int, y: int) -> bool:
        """Return True if x and y are inside of the bounds of this map."""
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, stdscr) -> None:
        """Render the map using curses"""
        for x in range(self.width):
            for y in range(self.height):
                if y < curses.LINES and x < curses.COLS:
                    try:
                        ch = self.tile_chars[x, y]
                        attr = curses.color_pair(self.tile_color_pairs[x, y]) | self.tile_attrs[x, y]
                        stdscr.addch(y, x, ch, attr)
                    except curses.error:
                        pass