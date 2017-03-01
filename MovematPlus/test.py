#!/usr/bin/python3
import pyautogui, time, os, sys, threading, serial, re

distance = 20
(x,y) = pyautogui.size()
pyautogui.moveTo(x/2,y-15)

time.sleep(5)
os.system("unclutter -idle 0.0 -root")

def play360Movie():
	os.system("GoProVRPlayer -t /home/movematplus/Videos/360°\ walk\ -\ «Trift»\ suspension\ bridge\ -\ Swiss\ Alps.mp4")
threading.Thread(target = play360Movie).start()

time.sleep(7)

def readArduino():
	global arduinoInt
	ser = serial.Serial('/dev/ttyACM0', 9600, timeout = None)
	while True:
		arduinoBytes = ser.readline()
#		print(arduinoBytes)
		arduinoString = arduinoBytes.decode("utf-8")
		arduinoString = re.sub("[^0-9]", "", arduinoString)
#		print(arduinoString)
		if(arduinoString == ""):
			arduinoString = 20
			print("error")
		arduinoInt = int(arduinoString)
		time.sleep(0.02)

threading.Thread(target = readArduino).start()

pyautogui.mouseDown(button='left')
pyautogui.moveTo(x/2,y/2)

while True:
	print(arduinoInt)

	if arduinoInt < 45:
		pyautogui.moveRel(-distance, 0, duration=0.05) #move left
	elif arduinoInt > 55:
		pyautogui.moveRel(distance, 0, duration=0.05) #move right
	else:
		pyautogui.moveRel(0, 0, duration=0.1) #dont move


#finished = False

#while True:
#	for line in open("/dev/ttyACM0", 'r'):
#		item = line.rstrip()
#		print(item)
#	print("the end")
#	time.sleep(1)
	


#def thread1():
#	global key
#	lock = threading.Lock()
#	pygame.init()
#	finished = False

#	while not finished:
#		for event in pygame.event.get():
#			print(event)
#			if event.type == pygame.QUIT:
#				finished = True
#			if event.type == pygame.KEYDOWN:
#				print(event.key)
#				key = event.key
			




#time.sleep(10)

#while True:
#	time.sleep(1)
#	print(key)
#	if key == ord('a'): 
#		pyautogui.dragRel(-distance, 0, duration=0.1) #move left
#	elif key == ord('d'): 
#		pyautogui.dragRel(distance, 0, duration=0.1) #move right
#	elif key == ord('q'):
#		break





#os.system("GoProVRPlayer /home/movematplus/Videos/360°\ walk\ -\ «Trift»\ suspension\ bridge\ -\ Swiss\ Alps.mp4")
#time.sleep(3)

#(x,y) = pyautogui.size()
#distance = 10

#pyautogui.moveTo(x/2,y/2)

#stdscr = curses.initscr()
#curses.cbreak()
#stdscr.keypad(1)

#stdscr.addstr(0,10,"Hit 'q' to quit")
#stdscr.refresh()

#key = ''
#while key != ord('q'):
#    key = stdscr.getch()
#    stdscr.addch(20,25,key)
#    stdscr.refresh()
#    if key == curses.KEY_LEFT: 
#        pyautogui.dragRel(-distance, 0, duration=0.1) #move left
#    elif key == curses.KEY_RIGHT: 
#        pyautogui.dragRel(distance, 0, duration=0.1) #move right

#curses.endwin()

#pyautogui.dragRel(-distance, 0, duration=0.1) #move left
#pyautogui.dragRel(distance, 0, duration=0.1) #move right


