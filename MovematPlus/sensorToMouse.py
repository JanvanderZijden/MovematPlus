#!/usr/bin/python3
import pyautogui, time, os, sys, threading, serial, re

distance = 20
x,y = pyautogui.size()

#time.sleep(5)
#os.system("unclutter -idle 0.0 -root")   #weet Xander wat dit doet?

#def play360Movie():
#	os.system("GoProVRPlayer -t /home/movematplus/Videos/360°\ walk\ -\ «Trift»\ suspension\ bridge\ -\ Swiss\ Alps.mp4")
#threading.Thread(target = play360Movie).start()

#time.sleep(7)

def readArduino():
	global arduinoInt
	ser = serial.Serial('/dev/ttyACM0', 9600, timeout = None)
	while True:
		try:
			arduinoBytes = ser.readline()
		except:
			break
		arduinoString = arduinoBytes.decode("utf-8")
		arduinoString = re.sub("[^0-9]", "", arduinoString)
#		print(arduinoString)
		if(arduinoString == ""):
			arduinoString = 50
			print("error")
		arduinoInt = int(arduinoString)
		time.sleep(0.02)
	arduinoInt = int(101)

threading.Thread(target = readArduino).start()

time.sleep(10)

pyautogui.moveTo(x/2,5)
pyautogui.mouseDown(button='left')
#pyautogui.moveTo(x/2,y/2)

while True:
	print(arduinoInt)
	if arduinoInt == 101:
		sys.exit("USB Unplugged")

	if arduinoInt < 45:
		pyautogui.moveRel(-distance, 0, duration=0.05) #move left
	elif arduinoInt > 55:
		pyautogui.moveRel(distance, 0, duration=0.05) #move right
	else:
		pyautogui.moveRel(0, 0, duration=0.1) #dont move
	
	xMouse, yMouse = pyautogui.position()
	if xMouse > x - 25 or xMouse < 25:
		pyautogui.mouseUp(button='left')
		pyautogui.moveTo(x/2,5)
		pyautogui.mouseDown(button='left')
