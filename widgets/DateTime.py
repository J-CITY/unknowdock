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


#from weather import Weather, Unit
gi.require_version('Notify', '0.7')
from gi.repository import Notify


import time
import threading

class DateTime(Label):

	def __init__(self, bgColor='#ffffff', fgColor='#000000', fmt="", delay=0.5,
			fontSize=10, font="", decoratePos="DOWN", decoreateImg=""):
		super().__init__(bgColor, fgColor, fontSize=fontSize, font=font,
			decoratePos=decoratePos, decoreateImg=decoreateImg)
		self.fmt = fmt
		self.delay = delay
		self.set_events(Gdk.EventMask.SCROLL_MASK|Gdk.EventMask.BUTTON_PRESS_MASK)
		self.connect('button-press-event', self.__onClick)
		self.connect('scroll-event', self.__onScroll)
		self.txt, self.newTxt = "", ""

		th = threading.Thread(target=self.UpdateThread)
		th.daemon = True
		th.start()
	
	def UpdateThread(self):
		while True:
			nowdt = datetime.datetime.now()
			self.newTxt = '<span font="%s">%s</span>' % (str(self.fontSize), nowdt.strftime(self.fmt))
			time.sleep(self.delay)

	def Update(self):
		if self.txt != self.newTxt:
			self.txt = self.newTxt
			self.label.set_markup(self.txt)
		return True
		#return GObject.SOURCE_CONTINUE

	def __onClick(self, widget, event = None):
		if event.button == 1:
			print("l")
		elif event.button == 2:
			print("m")
		elif event.button == 3:
			print("r")

	def __onScroll(self, widget, event):
		direction = event.direction
		if direction == Gdk.ScrollDirection.DOWN:
			print("-")
		elif direction == Gdk.ScrollDirection.UP:
			print("+")


















