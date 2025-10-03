#!/usr/bin/env python3
import curses
from curses import wrapper

from engine import Engine
from entity import Entity
from input_handler import EventHandler


def main(stdscr) -> None:
    # Initialize curses
    curses.curs_set(0)  # Hide cursor
    #stdscr.keypad(True) # Enable special keys
    stdscr.nodelay(0)   # wait for the input
    
    # initialize colors
    if curses.has_colors():
        curses.start_color()
        # define color pairs 
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
        
    # Get screen dimensions
    screen_height, screen_width = stdscr.getmaxyx()
    
    event_handler = EventHandler()
    
    player = Entity((screen_width // 2), (screen_height // 2), "@", curses.color_pair(1))
    npc = Entity((screen_width //2 - 5), (screen_height // 2 - 5), "@", curses.color_pair(3))
    entities = [player, npc]
    
    engine = Engine(entities, event_handler, player, stdscr)
    
    while True:
        stdscr.clear()      # clear screen
        
        # draw player
        try:
            engine.render()
        except curses.error:
            pass        # ignore drawing errors at screen edges
        
        stdscr.refresh()        # refresh screen
        
        # get input
        try:
            key = stdscr.getkey()
        except KeyboardInterrupt:
            break
        
        events = [key]
        
        if not engine.handle_events(events):
            break
        
        

if __name__ == "__main__":
    wrapper(main)