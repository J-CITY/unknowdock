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


gi.require_version('Notify', '0.7')
from gi.repository import Notify


import time
import threading
import subprocess
from widgets.ProgressBar import ProgressBar

class VolumeBar(ProgressBar):

	def __init__(self, bgColor='#ffffff', fgColor='#000000', 
			l="─", e="⊙", m="─", size=10, minVal=0, maxVal=100, step=10, 
			delay=1, fontSize=10, font="", decoratePos="DOWN", decoreateImg=""):
		#─⊙─
		super().__init__(bgColor, fgColor, 
			l, e, m, size, minVal, maxVal, step, 
			fontSize=fontSize, font=font,
			decoratePos=decoratePos, decoreateImg=decoreateImg)
		self.delay= delay
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
			self.newPercent = int(output)
			time.sleep(self.delay)

	def Update(self):
		if self.newPercent != self.percent:
			cmd = "pactl -- set-sink-volume 0 " + str(self.newPercent) + "%"
			_ = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)
		super().Update()
		return True








