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
from widgets.Desktop import Desktop, Desktops, Mode
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
	
	BG_COLOR = "#260b59"
	
	SIZE_Y = 18  # in pixel
	SIZE_X = 100 # in percent

	ALIGNMENT = Alignment.CENTR

	BORDER_COLOR = "#260b59"
	BORDER_WIDTH = 0

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
	Desktops(text=["一", "二", "三", "四"],
		bgColor='#260b59', fgColor='#e90cb2', 
		bgColorActive='#b70b41', fgColorActive='#505050'),
	#Text(bgColor="#4B3B51", fgColor="#ffffff", text=" | "),
	#UserName(bgColor="#4B3B51", fgColor="#ffffff"), 
	#Mode(bgColor="#4B3B51", fgColor="#ffffff"),
	#ProgressBar()
	#Text(bgColor=COLOR_01, fgColor=COLOR_02, text=" | "),
	#Text(text="2 label")
]
centr = [
	#Text(text="4 label"), 
	#Text(text="3 label")
]
right = [
	#Image(bgColor="#ffffff", 
	#	path="/home/daniil/unknowdock/widgets/icons/arr5.png"),
	#Image(bgColor="#CB755B", 
	#	path="/home/daniil/unknowdock/widgets/icons/cpu.png"),
	Text(bgColor="#260b59", fgColor="#e90cb2", text=" CPU: "),
	CpuUsage(fmt='%s %% ', percpu=True, bgColor="#260b59", fgColor="#e90cb2"), 
	#Image(path="/home/daniil/unknowdock/widgets/icons/arr4.png"),
	#VolumeImage(), 
	Text(bgColor="#260b59", fgColor="#b70b41", text=" | "),
	#Volume(bgColor="#92B0A0", fgColor="#ffffff"),
	#Text(text=" % ", bgColor="#92B0A0", fgColor="#ffffff"),
	#Image(path="/home/daniil/unknowdock/widgets/icons/arr3.png"),
	#Text(bgColor="#4B3B51", fgColor="#ffffff", text=" | "),
	#WeatherLabel(bgColor="#C0C0A2", fgColor="#ffffff"),
	#Text(bgColor="#4B3B51", fgColor="#ffffff", text=" | "),
	#Image(path="/home/daniil/unknowdock/widgets/icons/arr2.png"),
	DateTime(fmt="%Y-%m-%d %H:%M:%S", bgColor="#260b59", fgColor="#e90cb2"), 
	Text(bgColor="#260b59", fgColor="#ffffff", text=" "),
]
