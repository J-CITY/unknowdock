#!/usr/bin/env python3
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GObject, Gdk
import datetime

#import gobject
import threading
import cairo


from config import *


class DockWindow(Gtk.Window):

	def __init__(self, left=[], centr=[], right=[]):
		Gtk.Window.__init__(self, title="UnknownDock", decorated=True, name="DockWindow")
		
		#GObject.threads_init()

		self.config = Config()

		s = Gdk.Screen.get_default()
		'''
		style_provider = Gtk.CssProvider() 
		
		css = """
			#DockWindow {
			background: """+self.config.BORDER_COLOR+""";
		}"""
		style_provider.load_from_data(css.encode()) 

		Gtk.StyleContext.add_provider_for_screen(s, 
			style_provider, 
			Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
		'''
		
		self.width = s.get_width()
		self.height = s.get_height()

		self.box = Gtk.HBox(spacing=1)
		self.set_border_width(self.config.BORDER_WIDTH)
		self.add(self.box)

		_w = self.width - 2*self.config.GAP_X
		_w = int(_w/100*self.config.SIZE_X)
		posX = self.config.GAP_X
		if self.config.ALIGNMENT == Alignment.RIGHT:
			posX = self.width - self.config.GAP_X - _w
		elif self.config.ALIGNMENT == Alignment.CENTR:
			posX = self.width/2 - int(_w/2)
		posY = self.config.GAP_Y if self.config.POSITION == Position.TOP else self.height-self.config.GAP_Y-self.config.SIZE_Y


		self.wiggetsLeft = []
		self.wiggetsCentr = []
		self.wiggetsRight = []
		self.layoutLeft = Gtk.HBox()
		self.layoutCentr = Gtk.HBox()
		self.layoutRight = Gtk.HBox()
		
		if not self.config.TRANSPARENCY:
			self.layoutLeft.modify_bg(0, Gdk.color_parse(self.config.BG_COLOR))##54ff00
			self.layoutCentr.modify_bg(0, Gdk.color_parse(self.config.BG_COLOR))#ff4800
			self.layoutRight.modify_bg(0, Gdk.color_parse(self.config.BG_COLOR))#0099ff

		self.ralign = Gtk.Alignment()
		self.ralign.xalign = 1
		self.ralign.add(self.layoutRight)

		self.calign = Gtk.Alignment()
		self.calign.xalign = 0.5
		self.calign.add(self.layoutCentr)

		self.lalign = Gtk.Alignment()
		self.lalign.xalign = 0
		self.lalign.add(self.layoutLeft)

		self.box.pack_start(self.lalign, True, True, 0)
		self.box.pack_start(self.calign, True, True, 0)
		self.box.pack_end(self.ralign, False, True, 0)
		
		self.wLeft = left
		self.wRight = right
		self.wCentr = centr
		for w in left:
			self.layoutLeft.pack_start(w, expand=False, fill=False, padding=0)
			
		for w in right:
			self.layoutRight.pack_start(w, expand=False, fill=False, padding=0)
			
		for w in centr:
			self.layoutCentr.pack_start(w, expand=False, fill=False, padding=0)
		
		t = threading.Thread(target=self.Update)
		t.start()

		self.connect("destroy", Gtk.main_quit)
		disp = Gdk.Display.get_default()
		assert disp.supports_input_shapes()
		rect = disp.get_primary_monitor().get_geometry()

		self.set_type_hint(Gdk.WindowTypeHint.NOTIFICATION)
		#self.set_decorated(False)
		self.set_app_paintable(True)
		self.set_keep_above(True)
		self.set_accept_focus(False)
		self.set_visual(disp.get_default_screen().get_rgba_visual())
		self.set_default_size(rect.width, rect.height)
		self.realize()
		self.get_window().set_child_input_shapes()
		self.get_window().set_override_redirect(True)
		self.move(posX, posY)
		self.set_default_size(_w, self.config.SIZE_Y)
		
		self.visual = s.get_rgba_visual()
		if self.visual != None and s.is_composited():
			print("yay")
			self.set_visual(self.visual)
		self.connect("draw", self.area_draw)

		self.show_all()

	def area_draw(self, widget, cr):
		color = self.config.BG_COLOR[1:]
		rgb = tuple(int(color[i:i+2], 16) for i in (0, 2 ,4))
		transparency = self.config.TRANSPARENCY_VALUE if self.config.TRANSPARENCY else 1
		cr.set_source_rgba(rgb[0]/255.0, rgb[1]/255.0, rgb[2]/255.0, transparency)
		cr.set_operator(cairo.OPERATOR_SOURCE)
		cr.paint()
		cr.set_operator(cairo.OPERATOR_OVER)


	def Update(self):
		while True:
			for w in left:
				GObject.timeout_add(50, w.Update)
				#w.Update()
			for w in right:
				GObject.timeout_add(50, w.Update)
				#w.Update()
			for w in centr:
				GObject.timeout_add(50, w.Update)
				#w.Update()
			#GObject.timeout_add(200, None)
			#GObject.threads_init()
		


	def on_button_clicked(self, widget):
		print("Hello World")


win = DockWindow(left, centr, right)
Gtk.main()

