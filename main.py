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
import win32process
import random
import logging

import config

m = PyMouse()
k = PyKeyboard()
gdi32 = windll.gdi32
user32 = windll.user32
hdc = user32.GetDC(None)

# misc helper functions
def setTitle(titleStr):
	windll.kernel32.SetConsoleTitleW(titleStr)

def l(logStr):
	logging.info(logStr)

def initLogger():
    logging.basicConfig(
    format='[%(asctime)s] %(message)s',
    level=logging.DEBUG,
    datefmt='%Y-%m-%d %H:%M:%S')

# Process related helper functions
def activeWindowName():
	return win32gui.GetWindowText(win32gui.GetForegroundWindow())

def enum_window_callback(hwnd, pid):
    tid, current_pid = win32process.GetWindowThreadProcessId(hwnd)
    if pid == current_pid and win32gui.IsWindowVisible(hwnd):
        win32gui.SetForegroundWindow(hwnd)
        l("window activated")

def opengame():
	webbrowser.open('steam://rungameid/578080')

def activegamewindow():

	gamepid = findgame()
	if gamepid is not None:
		win32gui.EnumWindows(enum_window_callback, gamepid)
	
		

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
			l("crash window closed")
			return True
	return False

# pyinput helper functions
def getc(hori,vert):
	return hex(gdi32.GetPixel(hdc,hori,vert))

def mmove(hori,vert,delay):
	m.move(hori,vert)
	time.sleep(delay) 
	
def mclick(hori,vert,delay=2): # move, pause and click
	mmove(hori,vert,0.5)
	m.click(hori,vert,1)
	time.sleep(delay)
	
def mpress(str,times):
	k.press_key(str) 
	time.sleep(times)
	k.release_key(str)

def color(clr, x, y):
	return clr == getc(x,y)

def move_mouse(x,y):
    windll.user32.mouse_event(
        c_uint(0x0001),
        c_uint(x),
        c_uint(y),
        c_uint(0),
        c_uint(0)
    )
# getc(100,300)            Get color of certain pixel
# k.type_string('H')       Press certain key on keyboard
# k.press_key('H')         Keep pressing a key
# k.release_key('H')      Release a key
# m.move(200, 200)     Move mouse to certain pixel
# m.position()              Get pixel of mouse
# int(time.time())         Get current timestamp
# move_mouse(x,y)			move mouse in game

initLogger()

confs = ""
conf = {}
stayseconds = 240
easymode = 1
useJson = True
try:
	with open('config.json', 'r') as f:
		confs = f.read()
	conf = json.loads(confs)
except:
	useJson = False

if useJson:

	try:
	
		config.server1 = conf['model1']//10
		config.server2 = conf['model2']//10
		config.server3 = conf['model3']//10
		config.server4 = conf['model4']//10
		config.server5 = conf['model5']//10

		config.mode1 = conf['model1']%10
		config.mode2 = conf['model2']%10
		config.mode3 = conf['model3']%10
		config.mode4 = conf['model4']%10
		config.mode5 = conf['model5']%10

		stayseconds = conf['waittime']

		l("using user defined config")
		print(conf)
	
	except:
		l("error parsing config file")
		useJson = False

if not useJson:
	l("now in easymode")

setTitle("pubgfarmbot.tk - ©xulusjb,hirototakatoshi")


l("Farmbot successfully started! Open your game")
server = 4
mode = 3
s = int(time.time())
t = s
ingame = 0

theround = 0
lobbytime = 0


time.sleep(5)
lastgame = time.time()
windowActive = True

# main event loop
while True:
	
	# when game is not there, start it

	if crashwindow():
		l("game crashed")
		opengame()
		lastgame = time.time()
		time.sleep(25)
		#activegamewindow()

	if findgame() is None:
		opengame()
		l("launch game")
		lastgame = time.time()
		time.sleep(25)
		#activegamewindow()

	# else, do nothing when game is there but not activated

	wName = activeWindowName()
	gName = "PLAYERUNKNOWN'S BATTLEGROUNDS"
	if not gName in wName:
		lastgame = time.time()
		if windowActive:
			setTitle("pubgfarmbot.tk - idle")
			windowActive = False
		time.sleep(5)
		continue
	else:
		if not windowActive:
			windowActive = True
			setTitle("pubgfarmbot.tk - ©xulusjb,hirototakatoshi")	

	# ok1
	if(color("0xffffff",954,623) and color("0xffffff",979,615) and color("0xffffff",980,635)):
		l("on ok 1")	
		mclick(954,623)	
		time.sleep(5)
	
	
	#in the lobby
	if ( not color("0xcdff",285,974) and color("0xffffff", 1839,1022 ) and color("0xffffff",1843,1036) and color("0xffffff",1834,1036) ):
		l("in the lobby")
		nowtime = int(time.time())
		if ((nowtime - lobbytime) > 50):
			lobbytime = nowtime
		else: # repeatly matching failed
			mclick(1837,1029)
			time.sleep(2)
			mclick(947,605)
			time.sleep(5)
			l("restart lobby")
		
		time.sleep(2)
		# server and mode selection when using json
		if useJson:
			if ((theround % 5) == 0):
				server = config.server1
				mode = config.mode1
			elif ((theround % 5) == 1):
				server = config.server2
				mode = config.mode2
			elif ((theround % 5) == 2):
				server = config.server3
				mode = config.mode3
			elif ((theround % 5) == 3):
				server = config.server4
				mode = config.mode4
			elif ((theround % 5) == 4):
				server = config.server5
				mode = config.mode5

			mclick(1759,1035) # click bottom
			if (server == 1): #NA server
				mclick(815,448)
			elif (server == 2):#EU server
				mclick(847,496)
			elif (server == 3):#KR/JP server -- unavailable
				mclick(847,505)
			elif (server == 4):#asia server
				mclick(853,536)
			elif (server == 5):#OC server
				mclick(844,584)
			elif (server == 6):#SA server
				mclick(847,622)
			elif( server == 7):#SEA server
				mclick(842,671)
		
			mclick(935,736) #esc


		if (mode == 3):#squad
			mclick(155,790)
		elif (mode == 2): #duo
			mclick(152,718)
		elif (mode == 1): #solo
			mclick(182,680)		
		mclick(158,1009) 
		time.sleep(15)
			
	#on the plane
	if ( ingame == 0 ) and ( color("0xf2f2f2",1071,624) and  color("0xf2f3f2",961,21) and  color("0xf2f3f2",963,23)):
		l("on the plane")
		ingame = 1
		s = int(time.time())
		lastgame = time.time()
		if(stayseconds > 15):
			mmove(960,1080,0.1)
			time.sleep(8 + random.random() * 3)  # adjusted this value to keep distance from the map centre
			k.press_key('F')
			time.sleep(0.2)
			k.release_key('F') 
			time.sleep(1)  # double press F key to make sure player jumps
			k.press_key('F')
			time.sleep(0.2)
			k.release_key('F')
			timestamp = time.time()
			while time.time() - timestamp < 3:
				time.sleep(0.01)
				move_mouse(0,30)
			k.press_key('W')
			time.sleep(40)
			k.release_key('W')
			time.sleep(5)
			k.press_key('=')
			time.sleep(0.1)
			k.release_key('=')
			nowstate = 0
			nextstate = 0
			theround = theround +1 
			
	
	
	t = int(time.time())
	if (ingame == 1):
		#on time exit
		if ((t-s)>stayseconds):
			l("on time exit")
			mpress(k.escape_key,0.5)
			mclick(840,602)
			mclick(848,583)
			ingame = 0
			time.sleep(10)
		else:
			if random.random() < 0.2:
				mpress(' ', 0.05)
			timestamp = time.time()
			direction = random.choice([30,-30])
			while time.time() - timestamp < 0.4:
				move_mouse(direction,0)
				time.sleep(0.01)
			time.sleep(1)



	#cancel continue
	if( color("0xffffff", 816,482) and color("0xffffff",931,501) and  color("0xffffff",932,553)):
		l("cancel continue")
		mclick(1024,619)
		time.sleep(5)
	
	# reconnect1
	if( color("0xffffff",902,596) and  color("0xffffff",911,602) and  color("0xffffff",917,606)):
		l("on death exit")	
		mclick(957,608)
		time.sleep(5)		
	
	# on death exit
	if( color("0xffffff",1703,960) and  color("0xffffff",1648,954) and  color("0xffffff",1671,954)):
		l("on death exit")	
		mclick(1629,942)
		mclick(834,577)
		ingame = 0
		time.sleep(10)		
		
		
	#reconnect2
	if( color("0xffffff",902,633) and  color("0xffffff",910,642) and  color("0xffffff",937,627)):
		l("on reconnect 2")	
		mclick(910,642)
		time.sleep(5)
	
	if time.time() - lastgame > 300 + stayseconds:
		killgame()
		l("game killed")
		time.sleep(20)
