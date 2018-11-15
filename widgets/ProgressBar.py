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

class ProgressBar(Label):

	def __init__(self, bgColor='#ffffff', fgColor='#000000', 
			l="─", e="⊙", m="─", size=10, minVal=0, maxVal=100, step=10, 
			fontSize=10, font="", decoratePos="DOWN", decoreateImg=""):
		#─⊙─
		super().__init__(bgColor, fgColor, 
			fontSize=fontSize, font=font, decoratePos=decoratePos, decoreateImg=decoreateImg)
		self.minVal, self.maxVal = minVal, maxVal
		self.step = step
		self.l, self.e, self.m = l, e, m
		self.size = size
		self.percent = 0
		self.newPercent = 50
		self.set_events(Gdk.EventMask.SCROLL_MASK|Gdk.EventMask.BUTTON_PRESS_MASK)
		self.connect('button-press-event', self.__onClick)
		self.connect('scroll-event', self.__onScroll)

	def Update(self):
		if self.newPercent != self.percent:
			bar = ""
			while len(bar) < self.size/100.0*self.newPercent:
				bar += self.l
			bar = bar[0:len(bar)-1] + self.e
			while len(bar) < self.size:
				bar += self.m
			txt = '<span font="%s">%s</span>' % (str(self.fontSize), bar)
			self.label.set_markup(txt)
			self.percent = self.newPercent

	def __onClick(self, widget, event = None):
		if event.button == 1:
			print("l")
			self.createMenu(event)
		elif event.button == 2:
			print("m")
		elif event.button == 3:
			print("r")
			Notify.init("Test")
			Notify.Notification.new("Notification", "Hello!", "/home/daniil/mopag-master/widgets/icons/awesome-icon.png").show()
			Notify.uninit()

	def createMenu(self, event):
		self.menu = Gtk.Menu()

		about = Gtk.MenuItem()
		about.set_label("About")
		quit = Gtk.MenuItem()
		quit.set_label("Quit")

		quit.connect("activate", Gtk.main_quit)

		self.menu.append(about)
		self.menu.append(quit)

		self.menu.show_all()

		self.menu.popup(None, None, None, None, event.button, event.time)

	def __onScroll(self, widget, event):
		direction = event.direction
		if direction == Gdk.ScrollDirection.DOWN:
			self.newPercent -= self.step
			if self.newPercent < self.minVal:
				self.newPercent = self.minVal
		elif direction == Gdk.ScrollDirection.UP:
			self.newPercent += self.step
			if self.newPercent > self.maxVal:
				self.newPercent = self.maxVal









