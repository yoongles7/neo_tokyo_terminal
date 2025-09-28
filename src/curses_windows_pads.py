import curses
from curses import wrapper
import time

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_WHITE)
    BLACK_AND_RED = curses.color_pair(1)
    GREEN_AND_WHITE = curses.color_pair(2)
    
    counter_win = curses.newwin(2, 20, 10, 20)
    stdscr.addstr("Hello World :)")
    stdscr.refresh()
    
    for i in range(100):
        counter_win.clear()
        color = BLACK_AND_RED
        
        if i % 2 == 0:
            color = GREEN_AND_WHITE
        
        counter_win.addstr(f"Count: {i}", color)
        counter_win.refresh()
        time.sleep(0.1)
    stdscr.getch()

wrapper(main)