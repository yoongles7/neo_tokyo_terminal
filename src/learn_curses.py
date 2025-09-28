import curses
from curses import wrapper

def main(stdscr):
    # Basic setup
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()
    
    # Display welcome message
    stdscr.addstr(5, 10, "Welcome to Neo-Tokyo Terminal!")
    stdscr.addstr(7, 10, "Press any key to continue...")
    stdscr.refresh()
    
    # Wait for input
    stdscr.getch()
    
    # Clear and show new message
    stdscr.clear()
    stdscr.addstr(2, 5, "Cyberpunk ASCII MMO - Day 1 Progress")
    stdscr.addstr(4, 5, "This is your game window!")
    stdscr.addstr(6, 5, "Press 'q' to quit")
    stdscr.refresh()
    
    # Main loop
    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break

if __name__ == "__main__":
    curses.wrapper(main)