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
import time
import threading



class CpuUsage(Label):

	def __init__(self, bgColor='#ffffff', fgColor='#000000', fmt='%s', percpu=True, delay=1,
			fontSize=10, font="", decoratePos="DOWN", decoreateImg=""):
		super().__init__(bgColor, fgColor, fontSize=fontSize, font=font, decoratePos=decoratePos, decoreateImg=decoreateImg)
		self.percpu = percpu
		self.fmt =fmt
		self.text=self.newText=""
		self.delay = delay
		th = threading.Thread(target=self.UpdateThread)
		th.daemon = True
		th.start()
	
	def UpdateThread(self):
		while True:
			self.data = psutil.cpu_percent(interval=1, percpu=self.percpu)
			res = ""
			if self.percpu:
				for core in self.data:
					res += self.fmt % (core)
			else:
				res += self.fmt % (self.data)
			self.newText = res
			time.sleep(self.delay)
	def Update(self):
		if self.text != self.newText:
			self.text = self.newText
			self.SetText()
		return True
	def SetText(self):
		txt = '<span font="%s">%s</span>' % (str(self.fontSize), self.text)
		self.label.set_markup(txt)
