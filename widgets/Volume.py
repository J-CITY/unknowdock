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

class Volume(Label):
	def __init__(self, bgColor='#ffffff', fgColor='#000000', delay=1,
			fontSize=10, font="", decoratePos="DOWN", decoreateImg=""):
		super().__init__(bgColor, fgColor,
			fontSize=fontSize, font=font, decoratePos=decoratePos, decoreateImg=decoreateImg)
		self.set_events(Gdk.EventMask.SCROLL_MASK|Gdk.EventMask.BUTTON_PRESS_MASK)
		self.connect('button-press-event', self.__onClick)
		self.connect('scroll-event', self.__onScroll)
		self.delay = delay
		self.txt = ""
		self.newTxt = ""
		th = threading.Thread(target=self.UpdateThread)
		th.daemon = True
		th.start()
	
	def UpdateThread(self):
		while True:
			cmd = "pactl list sinks \
				| grep '^[[:space:]]Громкость:' | head -n $(( $SINK + 1 )) \
				| tail -n 1 | sed -e 's,.* \\([0-9][0-9]*\\)%.*,\\1,'"
			process = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)
			output = process.stdout.strip().decode('ascii')
			self.newTxt = '<span font="%s">%s</span>' % (str(self.fontSize), output)
			time.sleep(self.delay)


	def Update(self):
		if self.txt != self.newTxt:
			self.txt = self.newTxt
			self.label.set_markup(self.txt)
		return True

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
			# pactl -- set-sink-volume 0 +10%
			cmd = "pactl -- set-sink-volume 0 -10%"
			_ = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)
		elif direction == Gdk.ScrollDirection.UP:
			cmd = "pactl -- set-sink-volume 0 +10%"
			_ = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)

