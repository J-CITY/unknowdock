import os, sys
parentPath = os.path.abspath("..")
if parentPath not in sys.path:
	sys.path.insert(0, parentPath)

from widgets.Label import Label
from widgets.Image import Image

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GObject, Gdk
import datetime

import psutil


from weather import Weather, Unit
gi.require_version('Notify', '0.7')
from gi.repository import Notify


import time
import threading

import subprocess
import json
import traceback


class Mode(Label):
	def __init__(self, pwmi="", pdi="", bgColor='#ffffff', fgColor='#000000', 
		delay=1, fontSize=10, font="", decoratePos="DOWN", decoreateImg="", text=""):
		super().__init__(bgColor, fgColor,
			fontSize=fontSize, font=font, decoratePos=decoratePos, decoreateImg=decoreateImg)
		
		self.type = "MODE"
		self.set_events(Gdk.EventMask.SCROLL_MASK|Gdk.EventMask.BUTTON_PRESS_MASK)
		self.connect('button-press-event', self.__onClick)
		self.connect('scroll-event', self.__onScroll)
		self.delay = delay
		self.txt = ""
		self.newTxt = text
		self.id = 0
		self.json = ""

		self.pwmi = pwmi
		self.pdi = pdi
		th = threading.Thread(target=self.UpdateThread)
		th.daemon = True
		th.start()
	
	def UpdateThread(self):
		while True:
			#print(self.json)
			if self.json != "":
				try:
					parsedString = json.loads(self.json)
					curM = ""
					for m in parsedString["monitors"]:
						if m["cur"] == True:
							curM = m
							break
					curD = ""
					for d in curM["desktops"]:
						if d["cur"] == True:
							curD = d
							break

					if curD["mode"] == 0:
						self.newTxt = "VSL"
					elif curD["mode"] == 1:
						self.newTxt = "VSR"
					elif curD["mode"] == 2:
						self.newTxt = "HSU"
					elif curD["mode"] == 3:
						self.newTxt = "HSD"
					elif curD["mode"] == 4:
						self.newTxt = "MON"
					elif curD["mode"] == 5:
						self.newTxt = "GRD"
					elif curD["mode"] == 6:
						self.newTxt = "FLT"
					elif curD["mode"] == 7:
						self.newTxt = "FIB"
				except:
					traceback.print_exc()
			time.sleep(self.delay)


	def Update(self):
		if self.pwmi == "":
				return
		with open(self.pwmi, 'r') as f:
			data = f.read()
			self.json = data

		if self.txt != self.newTxt:
			self.txt = self.newTxt
			self.label.set_text(self.txt)
		return True

	def __onClick(self, widget, event = None):
		if event.button == 1:
			print("l")
			if self.pdi == "":
				return
			f = open(self.pdi, "w")
			self.id += 1
			if self.id > 7:
				self.id = 0
			f.write("mode:"+str(self.id))
		elif event.button == 2:
			print("m")
		elif event.button == 3:
			print("r")

	def __onScroll(self, widget, event):
		direction = event.direction
		if direction == Gdk.ScrollDirection.DOWN:
			pass
		elif direction == Gdk.ScrollDirection.UP:
			pass

class Desktop(Label):
	def __init__(self, pwmi="", pdi="", bgColor='#ffffff', fgColor='#000000', 
		bgColorActive='#000000', fgColorActive='#ffffff',
		delay=1, fontSize=10, font="", decoratePos="DOWN", decoreateImg="", text="", id=0):
		super().__init__(bgColor, fgColor,
			fontSize=fontSize, font=font, decoratePos=decoratePos, decoreateImg=decoreateImg)
		self.type = "DESK"
		self.set_events(Gdk.EventMask.SCROLL_MASK|Gdk.EventMask.BUTTON_PRESS_MASK)
		self.connect('button-press-event', self.__onClick)
		self.connect('scroll-event', self.__onScroll)
		self.delay = delay
		self.txt = ""
		self.newTxt = text
		self.id = id
		self.json = ""

		self.pwmi = pwmi
		self.pdi = pdi

		self.bgColorActive = bgColorActive
		self.fgColorActive = fgColorActive

		self.isCur = False
		self.newIsCur = False

		th = threading.Thread(target=self.UpdateThread)
		th.daemon = True
		th.start()
	
	def UpdateThread(self):
		while True:
			#print(self.json)
			if self.json != "":
				try:
					parsedString = json.loads(self.json)
					curM = ""
					for m in parsedString["monitors"]:
						#print(m)
						if m["cur"] == True:
							curM = m
							break
					if curM["desktops"][self.id]["cur"] == True:
						self.newIsCur = True
					else:
						self.newIsCur = False
				except:
					traceback.print_exc()
			time.sleep(self.delay)


	def Update(self):
		if self.txt != self.newTxt:
			self.txt = self.newTxt
			self.label.set_text(self.txt)
		if self.newIsCur != self.isCur:
			self.isCur = self.newIsCur
			if self.isCur == True:
				if self.bgColorActive != "":
					self.label.modify_bg(0, Gdk.color_parse(self.bgColorActive))
				if self.fgColorActive != "":
					self.label.modify_fg(0, Gdk.color_parse(self.fgColorActive))
			else:
				if self.bgColor != "":
					self.label.modify_bg(0, Gdk.color_parse(self.bgColor))
				if self.fgColor != "":
					self.label.modify_fg(0, Gdk.color_parse(self.fgColor))
		return True

	def __onClick(self, widget, event = None):
		if event.button == 1:
			print("l")
			if self.pdi == "":
				return
			f = open(self.pdi, "w")
			f.write("desktop:"+str(self.id))
		elif event.button == 2:
			print("m")
		elif event.button == 3:
			print("r")

	def __onScroll(self, widget, event):
		direction = event.direction
		if direction == Gdk.ScrollDirection.DOWN:
			pass
		elif direction == Gdk.ScrollDirection.UP:
			pass

class Desktops:
	def __init__(self, pwmi="", pdi="", deskSize=4,
		bgColor='#ffffff', fgColor='#000000', 
		bgColorActive='#000000', fgColorActive='#ffffff',
		delay=1, fontSize=10, font="", decoratePos="DOWN", decoreateImg="", text=[]):
		self.desktops = []
		self.type = "DESK"
		self.pwmi = pwmi
		self.pdi = pdi

		if text == []:
			for i in range(deskSize):
				text.append(str(i))

		for d in range(deskSize):
			self.desktops.append(Desktop(pwmi, pdi, bgColor, fgColor, 
				bgColorActive, fgColorActive, delay, fontSize, font, decoratePos, decoreateImg, text[d], d))
		
		self.delay = delay
		self.json = 0
		th = threading.Thread(target=self.UpdateThread)
		th.daemon = True
		th.start()

	def UpdateThread(self):
		while True:
			if self.pwmi == "":
				return
			with open(self.pwmi, 'r') as f:
				data = f.read()
				#print(data)
				for d in self.desktops:
					d.json = data
			time.sleep(self.delay)

	def Update(self):
		for w in self.desktops:
			w.Update()
		return True