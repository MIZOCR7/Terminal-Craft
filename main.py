import curses



def main(stdscr):
  
  running = True
  while running:
    
    stdscr.addstr(0, 0, "Let's Go")
    stdscr.refresh()
    stdscr.getch()
    
    
  
  
curses.wrapper(main) 
