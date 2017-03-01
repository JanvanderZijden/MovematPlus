import pyautogui, time, pygame, os, curses   

#os.system("GoProVRPlayer /home/movematplus/Videos/360°\ walk\ -\ «Trift»\ suspension\ bridge\ -\ Swiss\ Alps.mp4")
time.sleep(3)

(x,y) = pyautogui.size()
distance = 10

pyautogui.moveTo(x/2,y/2)

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,10,"Hit 'q' to quit")
stdscr.refresh()

key = ''
while key != ord('q'):
    key = stdscr.getch()
    stdscr.addch(20,25,key)
    stdscr.refresh()
    if key == curses.KEY_LEFT: 
        pyautogui.dragRel(-distance, 0, duration=0.1) #move left
    elif key == curses.KEY_RIGHT: 
        pyautogui.dragRel(distance, 0, duration=0.1) #move right

curses.endwin()

#pyautogui.dragRel(-distance, 0, duration=0.1) #move left
#pyautogui.dragRel(distance, 0, duration=0.1) #move right
