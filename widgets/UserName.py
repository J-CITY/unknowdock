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

class UserName(Label):

	def __init__(self, bgColor='#ffffff', fgColor='#000000',
			fontSize=10, font="", decoratePos="DOWN", decoreateImg=""):
		super().__init__(bgColor, fgColor, fontSize=fontSize, font=font,
			decoratePos=decoratePos, decoreateImg=decoreateImg)
		self.text = psutil.users()[0].name
		self.SetText()
	
	def SetText(self):
		txt = '<span font="%s">%s</span>' % (str(self.fontSize), self.text)
		self.label.set_markup(txt)