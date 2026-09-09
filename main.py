import curses



def main(stdscr):
    stdscr.clear()
    
    curses.curs_set(0)
    stdscr.nodelay(True) 
    stdscr.timeout(50)
    
    running = True
    screen_height, screen_width = stdscr.getmaxyx() 
    x_pos = screen_width // 2
    y_pos = screen_height // 2 
    
    ship = '^'
    
    while running: 
      key = stdscr.getch() 
      if key == 27: 
        running = False
      if key == 119 and y_pos > 0:
        y_pos -= 1
      elif key == ord('s') and y_pos < screen_height - 2:
              y_pos += 1 
      
      if key == ord('d') and x_pos < screen_width - 1:
        x_pos += 1
      elif key == ord('a') and x_pos > 0:
        x_pos -= 1
      
      stdscr.clear()  
      stdscr.addstr(y_pos, x_pos, ship) 
        
      
      
      stdscr.refresh() 
    
  
  
curses.wrapper(main) 
