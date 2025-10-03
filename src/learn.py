import curses
from curses import wrapper

def main(stdscr):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    RED_AND_BLACK = curses.color_pair(1)
    
    x, y = 0, 0
    while True:
        key = stdscr.getkey()
            
        if key == "a":
            x -= 1
        elif key == "w":
            y -= 1
        elif key == "s":
            y += 1
        elif key == "d":
            x += 1
        elif key == "q":
            break
            
        stdscr.clear()
        stdscr.addstr(y, x, "@@@@@@@@@@@@@", RED_AND_BLACK | curses.A_BOLD)
        stdscr.refresh()

wrapper(main)