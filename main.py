#!/usr/bin/env python

"""pubgbot.py: Nasty PUBG farm bot."""

__author__      = "fdukeshik, h.takatoshi"
__copyright__   = "Copyright 2017, team601"

from ctypes import *
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
import json
import webbrowser
import psutil
import win32gui
import win32con

m = PyMouse()
k = PyKeyboard()
gdi32 = windll.gdi32
user32 = windll.user32
hdc = user32.GetDC(None)

def opengame():
	webbrowser.open('steam://rungameid/578080')

def activegamewindow():
	hwnd = win32gui.FindWindow(None,"PLAYERUNKNOWN'S BATTLEGROUNDS ")
	if hwnd is not None:
		win32gui.SetForegroundWindow(hwnd)

def killgame():
	gamepid = findgame()
	if gamepid is not None:
		try:
			psutil.Process(gamepid).terminate()
		except psutil.NoSuchProcess:
			pass

def findgame():
	for _ in psutil.pids():
		try:
			name = psutil.Process(_).name()
		except psutil.NoSuchProcess:
			continue
		if name == "TslGame.exe":
			return _
	return None

def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

# BATTLEGROUNDS Crash Reporter
def crashwindow():
	top_windows = []
	win32gui.EnumWindows(windowEnumerationHandler, top_windows)
	for i in top_windows:
		if "BATTLEGROUNDS Crash Reporter" in i[1]:
			win32gui.PostMessage(i[0],win32con.WM_CLOSE,0,0)
			return True
	return False

	

def getc(hori,vert):
	return hex(gdi32.GetPixel(hdc,hori,vert))
	
def mclick(hori,vert,times, delay): #Click certain pixel 1 time
	m.click(hori,vert,times) 
	time.sleep(delay)
	
def mmove(hori,vert,times):
	m.move(hori,vert)
	time.sleep(times) 
	
def mpress(str,times):
	k.press_key(str) 
	time.sleep(times)
	k.release_key(str)

def color(clr, x, y):
	return clr == getc(x,y)
# getc(100,300)            Get color of certain pixel
# k.type_string('H')       Press certain key on keyboard
# k.press_key('H')         Keep pressing a key
# k.release_key('H')      Release a key
# m.move(200, 200)     Move mouse to certain pixel
# m.position()              Get pixel of mouse
# int(time.time())         Get current timestamp

confs = ""
with open('config.json', 'r') as f:
	confs = f.read()
conf = json.loads(confs)
print(conf)
print("Now script successfully started! Open your game")
server1 = conf['model1']//10
server2 = conf['model2']//10
server3 = conf['model3']//10
server4 = conf['model4']//10
server5 = conf['model5']//10

mode1 = conf['model1']%10
mode2 = conf['model2']%10
mode3 = conf['model3']%10
mode4 = conf['model4']%10
mode5 = conf['model5']%10

server = 4
mode = 3
s = int(time.time())
t = s
ingame = 0
stayseconds = conf['waittime']
theround = 0
lobbytime = 0

time.sleep(5)
lastgame = time.time()
while True:
	
	if ((theround % 5) == 0):
		server = server1
		mode = mode1
	elif ((theround % 5) == 1):
		server = server2
		mode = mode2
	elif ((theround % 5) == 2):
		server = server3
		mode = mode3
	elif ((theround % 5) == 3):
		server = server4
		mode = mode4
	elif ((theround % 5) == 4):
		server = server5
		mode = mode5
	
	didsomething = False

	if crashwindow():
		print("game crashed")
		opengame()
		lastgame = time.time()
		didsomething = True
		time.sleep(25)
		activegamewindow()

	if findgame() is None:
		opengame()
		print("launch game")
		lastgame = time.time()
		didsomething = True
		time.sleep(25)
		activegamewindow()

	
		
	# ok1
	if(color("0xffffff",954,623) and color("0xffffff",979,615) and color("0xffffff",980,635)):
		print("on ok 1")	
		mmove(954,623,0.5)	
		mclick(954,623,1,2)
		time.sleep(5)
		didsomething = True
	
	
	#in the lobby
	if ( not color("0xcdff",285,974) and color("0xffffff", 1839,1022 ) and color("0xffffff",1843,1036) and color("0xffffff",1834,1036) ):
		print("in the lobby")
		nowtime = int(time.time())
		if ((nowtime - lobbytime) > 50):
			lobbytime = nowtime
		else: # repeatly match failed
			mmove(1837,1029,0.5)
			mclick(1837,1029,1,2)
			time.sleep(2)
			mmove(947,605,0.5)
			mclick(947,605,1,2)
			time.sleep(5)
		
		time.sleep(2)
		mmove(1759,1035,0.5)
		mclick(1759,1035,1,2) # click bottom
		if (server == 1): #NA server
			mmove(845,422,0.5)
			mclick(845,422,1,2)
		elif (server == 2):#EU server
			mmove(847,462 ,0.5)
			mclick(847,462 ,1,2) 
		elif (server == 3):#KR/JP server
			mmove(847,505 ,0.5)
			mclick(847,505,1,2) 
		elif (server == 4):#asia server
			mmove(853,567,0.5)
			mclick(853,567,1,2) 
		elif (server == 5):#OC server
			mmove(844,597,0.5)
			mclick(844,597,1,2) 
		elif (server == 6):#SA server
			mmove(847,645,0.5)
			mclick(847,645,1,2) 
		elif( server == 7):#SEA server
			mmove(842,692,0.5)
			mclick(842,692,1,2) 
		
		mclick(957,758,1,2) #esc
		if (mode == 3):#squad
			mmove(155,790,0.5)
			mclick(155,790,1,2)
		elif (mode == 2): #duo
			mmove(152,718 ,0.5)
			mclick(152,718,1,2)
		elif (mode == 1): #solo
			mmove(182,680 ,0.5)
			mclick(182,680,1,2)			
		mmove(158,1009,0.5)
		mclick(158,1009,1,2) 
		time.sleep(15)
			
	#on the plane
	if ( ingame == 0 ) and ( color("0xf2f3f2",960,20) and  color("0xf2f3f2",961,21) and  color("0xf2f3f2",963,23)):
		print("on the plane")
		ingame = 1
		s = int(time.time())
		lastgame = time.time()
		if(stayseconds > 15):
			time.sleep(25)
			k.press_key('F')
			time.sleep(0.2)
			k.release_key('F') 
			time.sleep(5)
			k.press_key('F')
			time.sleep(0.2)
			k.release_key('F')
			theround = theround +1 
			
	
	#on time exit
	t = int(time.time())
	if (ingame == 1) and ((t-s)>stayseconds):
		didsomething = True
		print("on time exit")
		mpress(k.escape_key,0.5)
		mmove(840,602,0.5)
		mclick(840,602,1,2)
		mmove(848,583,0.5)
		mclick(848,583,1,2)
		ingame = 0
		time.sleep(10)
	#cancel continue
	if( color("0xffffff", 816,482) and color("0xffffff",931,501) and  color("0xffffff",932,553)):
		didsomething = True
		print("cancel continue")
		mmove(1024,619,0.5)	
		mclick(1024,619,1,2)
		time.sleep(5)
	
	# reconnect1
	if( color("0xffffff",902,596) and  color("0xffffff",911,602) and  color("0xffffff",917,606)):
		didsomething = True
		print("on death exit")	
		mmove(957,608,0.5)	
		mclick(957,608,1,2)

		time.sleep(5)		
	
	# on death exit
	if( color("0xffffff",1703,960) and  color("0xffffff",1648,954) and  color("0xffffff",1671,954)):
		didsomething = True
		print("on death exit")	
		mmove(1629,942,0.5)	
		mclick(1629,942,1,2)
		mmove(834,577,0.5)
		mclick(834,577,1,2)
		ingame = 0
		time.sleep(10)		
		
		
	#reconnect2
	if( color("0xffffff",902,633) and  color("0xffffff",910,642) and  color("0xffffff",937,627)):
		didsomething = True
		print("on reconnect 2")	
		mmove(910,642,0.5)	
		mclick(910,642,1,2)
		time.sleep(5)
	
	if time.time() - lastgame > 300 + stayseconds:
		killgame()
		print("game killed")
