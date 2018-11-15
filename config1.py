from widgets.DateTime import DateTime
from widgets.UserName import UserName
from widgets.Volume import Volume
from widgets.VolumeImage import VolumeImage
from widgets.CpuUsage import *
from widgets.Weather import *
from widgets.ProgressBar import *
from widgets.Text import *
from widgets.Image import Image
from widgets.Label import Label
from enum import Enum

class Position(Enum):
	TOP = 1
	BOTTOM = 2

class Alignment(Enum):
	LEFT = 1
	CENTR = 2
	RIGHT = 3

class Config:
	POSITION = Position.TOP

	GAP_X = 10
	GAP_Y = 0
	
	BG_COLOR = "#4B3B51"
	
	SIZE_Y = 20  # in pixel
	SIZE_X = 100 # in percent

	ALIGNMENT = Alignment.CENTR

	BORDER_COLOR = "#4B3B51"
	BORDER_WIDTH = 0

	TRANSPARENCY = True
	TRANSPARENCY_VALUE = 0.4

COLOR_01="#282a2e"           # black
COLOR_02="#A54242"           # red
COLOR_03="#8C9440"           # green
COLOR_04="#de935f"           # yellow
COLOR_05="#5F819D"           # blue
COLOR_06="#85678F"           # magenta
COLOR_07="#5E8D87"           # cayn
COLOR_08="#969896"           # white



left = [
	Text(bgColor="", fgColor="#000000", text=" User: "),
	UserName(bgColor="", fgColor="#000000"), 
	#ProgressBar()
	#Text(bgColor=COLOR_01, fgColor=COLOR_02, text=" | "),
	#Text(text="2 label")
]
centr = [
	DateTime(fmt="%Y-%m-%d %H:%M:%S", bgColor="", fgColor="#000000"), 
	#Text(text="4 label"), 
	#Text(text="3 label")
]
right = [
	Text(bgColor="", fgColor="#000000", text="CPU: "),
	CpuUsage(fmt='%s %% ', percpu=True, bgColor="", fgColor="#000000"), 
	Text(bgColor="", fgColor="#000000", text="Vol: "),
	Volume(bgColor="", fgColor="#000000"),
	Text(text=" % ", bgColor="", fgColor="#000000"),
	Text(text="Weather: ", bgColor="", fgColor="#000000"),
	WeatherLabel(bgColor="", fgColor="#000000"),
	Text(bgColor="", fgColor="#000000", text=" "),
]
