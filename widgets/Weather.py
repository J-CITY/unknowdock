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
class WeatherLabel(Label):

	def __init__(self, bgColor='#ffffff', fgColor='#000000', fmt="%s", city="vladivostok", delay=5,
		fontSize=10, font="", decoratePos="DOWN", decoreateImg=""):
		super().__init__(bgColor, fgColor, fontSize=fontSize, font=font,
			decoratePos=decoratePos, decoreateImg=decoreateImg)
		self.weather = Weather()
		self.city = city
		#location = self.weather.lookup_by_location(self.city)
		#condition = location.condition
		#self.text = condition.text + " " + condition.temp + " °C "
		self.text = ""
		self.newText = ""
		self.SetText()
		self.delay = delay
		th = threading.Thread(target=self.UpdateThread)
		th.daemon = True
		th.start()

	def SetText(self):
		self.label.set_markup(self.text)

	def UpdateThread(self):
		while True:
			location = self.weather.lookup_by_location(self.city)
			condition = location.condition
			self.newText = condition.text + " " + condition.temp + " °C "
			time.sleep(self.delay)

	def Update(self):
		if self.text != self.newText:
			self.text = self.newText
			self.SetText()
		return True