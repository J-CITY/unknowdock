import os, sys
parentPath = os.path.abspath("..")
if parentPath not in sys.path:
	sys.path.insert(0, parentPath)

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GObject, Gdk
from PIL import Image
import cairo

class Image(Gtk.EventBox):

	def __init__(self, bgColor="#ffffff", path="v.png", decoratePos="DOWN", decoreateImg=""):
		super().__init__()
		self.type = "IMAGE"
		self.bgColor = bgColor

		self.image = Gtk.Image()
		self.image.set_from_file(path)

		self.imageDecorate = Gtk.Image()
		if decoreateImg != "":
			self.imageDecorate.set_from_file(decoreateImg)

		self.vbox = Gtk.VBox()
		if bgColor != "":
			self.vbox.modify_bg(Gtk.StateType.NORMAL, Gdk.color_parse(bgColor))
		
		self.vbox.set_border_width(0)
		if decoreateImg != "" and decoratePos == "UP":
			self.vbox.pack_start(self.imageDecorate, expand=False, fill=False, padding=0)
		self.vbox.pack_start(self.image, expand=True, fill=False, padding=0)
		if decoreateImg != "" and decoratePos == "DOWN":
			self.vbox.pack_start(self.imageDecorate, expand=False, fill=False, padding=0)
		
		self.add(self.vbox)

	def Update(self):
		pass

	def onClick(self, widget, event = None):
		pass

	def onScroll(self, widget, event):
		pass