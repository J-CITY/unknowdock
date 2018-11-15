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
from widgets.VolumeBar import VolumeBar
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
	GAP_Y = 3
	
	BG_COLOR = "#282a2e"
	
	SIZE_Y = 20  # in pixel
	SIZE_X = 60 # in percent

	ALIGNMENT = Alignment.CENTR

	BORDER_COLOR = "#4B3B51"
	BORDER_WIDTH = 13

	TRANSPARENCY = False
	TRANSPARENCY_VALUE = 1

COLOR_01="#282a2e"           # black
COLOR_02="#A54242"           # red
COLOR_03="#8C9440"           # green
COLOR_04="#de935f"           # yellow
COLOR_05="#5F819D"           # blue
COLOR_06="#85678F"           # magenta
COLOR_07="#5E8D87"           # cayn
COLOR_08="#969896"           # white



left = [
	Text(bgColor="#282a2e", fgColor="#969896", text=" User: ", decoratePos="DOWN", decoreateImg="/home/daniil/mopag-master/widgets/icons/dec.png"),
	UserName(bgColor="#282a2e", fgColor="#969896", decoratePos="DOWN", decoreateImg="/home/daniil/mopag-master/widgets/icons/dec.png"), 
	#ProgressBar()
	#Text(bgColor=COLOR_01, fgColor=COLOR_02, text=" | "),
	#Text(text="2 label")
]
centr = [
	DateTime(fmt="%Y-%m-%d %H:%M:%S", bgColor="#282a2e", fgColor="#969896"), 
	#Text(text="4 label"), 
	#Text(text="3 label")
]
right = [
	Text(bgColor="#282a2e", fgColor="#969896", text="CPU: "),
	CpuUsage(fmt='%s %% ', percpu=True, bgColor="#282a2e", fgColor="#969896", decoratePos="DOWN", decoreateImg="/home/daniil/mopag-master/widgets/icons/dec.png"), 
	Text(bgColor="#282a2e", fgColor="#969896", text="Vol: ", decoratePos="DOWN", decoreateImg="/home/daniil/mopag-master/widgets/icons/dec.png"),
	VolumeBar(bgColor="#282a2e", fgColor="#969896"),
	Text(text=" Weather: ", bgColor="#282a2e", fgColor="#969896", decoratePos="DOWN", decoreateImg="/home/daniil/mopag-master/widgets/icons/dec.png"),
	WeatherLabel(bgColor="#282a2e", fgColor="#969896", decoratePos="DOWN", decoreateImg="/home/daniil/mopag-master/widgets/icons/dec.png"),
	Text(bgColor="#282a2e", fgColor="#969896", text=" "),
]
