import os, sys
parentPath = os.path.abspath("..")
if parentPath not in sys.path:
	sys.path.insert(0, parentPath)

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GObject, Gdk
from PIL import Image
import cairo

class Label(Gtk.EventBox):

	def __init__(self, bgColor='#ffffff', fgColor='#000000', fontSize=10, font="", decoratePos="DOWN", decoreateImg=""):
		super().__init__()
		self.type = "LABEL"
		self.fontSize = fontSize
		txt  = '<span font="%s"></span>' % (str(self.fontSize))
		self.label = Gtk.Label(txt)
		
		self.decoratePos = decoratePos
		self.bgColor = bgColor
		self.fgColor = fgColor

		if bgColor != "":
			self.label.modify_bg(0, Gdk.color_parse(bgColor))
		if fgColor != "":
			self.label.modify_fg(0, Gdk.color_parse(fgColor))
		if font != "":
			self.label.modify_font(pango.FontDescription(font))
		
		
		self.imageDecorate = Gtk.Image()
		if decoreateImg != "":
			self.imageDecorate.set_from_file(decoreateImg)

		self.vbox = Gtk.VBox()
		if bgColor != "":
			self.vbox.modify_bg(Gtk.StateType.NORMAL, Gdk.color_parse(bgColor))
		
		self.vbox.set_border_width(0)
		if decoreateImg != "" and decoratePos == "UP":
			self.vbox.pack_start(self.imageDecorate, expand=False, fill=False, padding=0)
		self.vbox.pack_start(self.label, expand=True, fill=False, padding=0)
		if decoreateImg != "" and decoratePos == "DOWN":
			self.vbox.pack_start(self.imageDecorate, expand=False, fill=False, padding=0)
		self.add(self.vbox)

	def Update(self):
		pass

	def onClick(self, widget, event = None):
		pass

	def onScroll(self, widget, event):
		pass

