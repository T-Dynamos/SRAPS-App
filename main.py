

__version__ = "2.0"


import kivy
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.anchorlayout import *
from kivymd.uix.dialog import MDDialog
from kivymd.app import *
from kivymd.uix.label import *
from kivy.uix.image import *
from kivy.uix.label import *
from kivy.uix.screenmanager import *
from kivy.lang import Builder
from kivy.core.text import LabelBase 
from kivymd.uix.button import *
from kivymd.uix.screen import *
from kivymd.uix.textfield import *
from kivy.core.audio import *
from kivymd.uix.list import *
from kivymd.toast import toast as Toast1
from kivy.uix.scrollview import *
from kivymd.uix.button import MDFlatButton
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.card import MDCard
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.dialog import MDDialog
from kivy.utils import get_color_from_hex
from kivy.animation import Animation
from kivy.uix.modalview import ModalView
from kivy.uix.carousel import Carousel
import kivymd_extensions.akivymd
from kivymd.uix.expansionpanel import *
from kivymd.uix.datatables import MDDataTable
from kivy.uix.anchorlayout import AnchorLayout
import requests
import webbrowser
import os
import subprocess
import sys
import threading
from pathlib import Path
from kivy.clock import Clock
from functools import partial
from kivymd.icon_definitions import md_icons
from kivy.utils import platform
from kivy.core.window import Window
from kivymd.uix.snackbar import Snackbar
import time
import _thread
from colorpicker import MDColorPicker
from kivymd.uix.dialog import MDDialog
from functools import partial
import settings
from android.runnable import run_on_ui_thread
from jnius import autoclass

try:
	from dataDb import Teachers
except Exception:
	Teachers=[]
	pass



screen_manager = ScreenManager()
if platform != "android":
	Window.size = (Window.size[0]//2, Window.size[1])
y = Window.size[0]
def check_intr():
	import requests
	try:
		requests.get("https://google.com",timeout=1)
	except Exception as e:
		print(str(e))
		return False
	return True

	
def getDb():
	apiUrl = "https://raw.githubusercontent.com/T-Dynamos/SRAPS-App/main/dataDb.py"
	try:
		a = requests.get(apiUrl,timeout=2)
		open('dataDb.py', 'wb').write(a.content)
		import dataDb
		from dataDb import DataBase, links
	except Exception as e:
		return exit(str(e))
	return DataBase, links
def get_version():
	url = "https://raw.githubusercontent.com/T-Dynamos/SRAPS-App/main/.srapsapp.versionfile"
	url_Get = requests.get(url)
	if __version__ == url_Get.text:
		return "updated",url_Get.text
	else:
		return "available",url_Get.text
def return_Sycn(url):
	import random
	try:
		path = f'assets/tmp-{random.random()}.{(url.split("."))[-1]}'
		r = requests.get(url, allow_redirects=True)
		open(path ,'wb').write(r.content)
		return path
	except Exception:
		return "assets/no-internet.png"
def update_data():
	o = screen_manager.get_screen("Mscreen").ids
	DataBase, links = getDb()
	o.news.text = str(DataBase["News"])		
	o.nimg1.source = str(DataBase["SliderImages"])
	add_part(links)
def Toast(string):
	Toast1(string)
def update_menu():
	KV = """
#:import _thread _thread
MDCard:
	radius:50
	elevation:60
	orientation:"vertical"
	AnchorLayout:
		id:upd1		
		anchor_x:'center'
		anchor_y:'bottom'
		Image:
			id:upd
			source:"assets/system-update.png"
			size:(0.9,0.9)
			halign:"center"
			anim_delay:0.05
	MDLabel:
		id:ud2
		text:"Currently Installed Version "+app.__version__
		font_name:"assets/Poppins-SemiBoldItalic.ttf"
		font_size:"15sp"
		hailgn:"center"
	AnchorLayout:
		orientation:"vertical"
		anchor_x:'center'
		anchor_y:'center'
		MDRoundFlatButton:
			id:ud3
			text:"Check for Update"
			font_name:"assets/Poppins-SemiBoldItalic.ttf"
			font_size:"15sp"
			halign:"center"
			line_width:5
			on_press:upd.source = "assets/load.gif";ud2.text = "Checking ...";_thread.start_new_thread(app.update_a,(upd1,ud2,upd,ud3))
	"""

	
	modal = ModalView(
	background_color=[0,0,0,0],
	size_hint=(0.7, 0.5),

	overlay_color=(0, 0, 0, 0),

	)

	modal.add_widget(Builder.load_string(KV))
	modal.open()	
def show_message():
		dialog=Snackbar(text="No Internet!",
		snackbar_x="10dp",

		radius=[30,30,30,30],
		snackbar_y="55dp",
		size_hint_x=.95)
		a = lambda self : (Toast("Updating data"),_thread.start_new_thread(update_data,()),dialog.dismiss())
		b = lambda self : Toast("Internet not connected")
		show_message_true = lambda self:show_message()
		c = lambda self : (dialog.dismiss(),Clock.schedule_once(show_message_true,5))
		d = lambda self : a(True) if check_intr() is True else b(True)
		dialog.buttons = [
		MDFlatButton(text="Retry",
			font_name="assets/Poppins-Regular.ttf",
			theme_text_color="Custom",
			text_color=[1,1,1,1],
			on_press = d), 
		MDFlatButton (text="Cancel",
			font_name="assets/Poppins-Regular.ttf",
			theme_text_color="Custom",
			text_color=[1,1,1,1],
			on_press=c)]
		dialog.auto_dismiss=False
		dialog.open()

def add_part(links):
	if check_intr() is True:
		screen_manager.get_screen("Mscreen").ids.fu.add_widget(Builder.load_string("""
MDLabel:
	text:'Our Partners '
	font_name:'assets/Poppins-Bold.ttf'
	font_size:'20sp'
			"""))
		pass
	else:
		card = MDCard(
		radius=[20],
		padding=0,
		elevation=10,
		halign="center",
		size_hint=(None,None),
		size= (y-y//5, "200dp")
		)
		card.add_widget(FitImage(source='assets/no-internet.png'))
		screen_manager.get_screen("Mscreen").ids.fu.add_widget(card)	
	for link in links:
		card = MDCard(
		radius=[20],
		padding=10,
		halign="center",
		elevation=0,
		size_hint=(None,None),
		size= (y-y//15, "200dp")
		)
		image = AsyncImage (source=link, allow_stretch=True)
		card.add_widget(image)
		o = screen_manager.get_screen("Mscreen").ids
		o.fu.add_widget(card)
	
def show_timings():

	a = """
MDCard:
	radius:[30]
	size:(0.85,0.85)
	elevation:50
	orientation:"vertical"
	AnchorLayout:
		Image:
			size:(0.8,0.8)
			source:"assets/time.jpg"
			allow_stretch:True
			keep_ratio :False
	ScrollView:
		MDGridLayout:
			cols:1
			adaptive_height:True
			spacing:app.spacing*3
			id : boxi
			orientation :"lr-tb"
			padding:10
			MDLabel:
				text:""
				font_name:"assets/Poppins-Bold.ttf"
				font_size:"15sp"
			MDLabel:
				text:"Timings can be changed any time as the situation demands."
				font_name:"assets/Poppins-Bold.ttf"
				font_size:"15sp"
			MDLabel:
				text:"• Parents must ensure that their children reach at least 10 minutes before the gate is closed so that children are able to attend the morning assembly."
				font_name:"assets/Poppins-Regular.ttf"
			MDLabel:
				text:"• First Bell will ring 5 minutes prior to the time mentioned above."
				font_name:"assets/Poppins-Regular.ttf"
			MDLabel:
				text:"• In the morning no student will be allowed to enter the school after the second bell."
				font_name:"assets/Poppins-Regular.ttf"
			MDLabel:
				text:"• The gate will remain closed during assembly. At the time of dispersal gates will open at the time of last bell."
				font_name:"assets/Poppins-Regular.ttf"	
			MDLabel:
				text:"• For Primary Wing the gate will open only 5 minutes before dispersal time."
				font_name:"assets/Poppins-Regular.ttf"
			MDLabel:
				text:""


				
		"""
	modal = ModalView(
	background_color=[0,0,0,0],
	size_hint=(0.8, 0.8),

	overlay_color=(0, 0, 0, 0),

	)

	modal.add_widget(Builder.load_string(a))
	modal.open()	
	
	
def about_menu():
	a = """
MDCard:
	radius:30
	elevation:50
	orientation:"vertical"
	md_bg_color:app.colorHex("#FE3545")
	AnchorLayout:
		Image:
			source:"assets/td-s.png"
			allow_stretch:True
			size:(self.width,self.height)
			keep_ratio :False
	ScrollView:
		GridLayout:
			cols:1
			adaptive_height:True
			spacing:app.spacing*3
			orientation :"lr-tb"
			padding:0		
			MDLabel:
				text:"We Are Technocractic Dynamos"
				font_name:"assets/Poppins-Bold.ttf"
				theme_text_color:"Custom"
				text_color:1,1,1,1
				font_size:"20sp"
			MDLabel:
				text:"> Technocratic Dynamos , a group made of youths to empower technology. We're dedicated to providing you the very best of an overall experience in an app, with an emphasis on [easy UI], [Lag Free experience ]"
				font_name:"assets/Poppins-Bold.ttf"
				text_color:0,0,0,1
				font_size:"15sp"
				theme_text_color:"Custom"							
"""
	modal = ModalView(
	background_color=[0,0,0,0],
	size_hint=(0.8, 0.9),
	overlay_color=(0, 0, 0, 0),

	)

	modal.add_widget(Builder.load_string(a))
	modal.open()		
def show_adim():
	a = """
MDCard:
	radius:[30]
	size:(0.85,0.85)
	elevation:50
	orientation:"vertical"
	ScrollView:
		MDGridLayout:
			cols:1
			adaptive_height:True
			spacing:app.spacing*2.5
			id : boxi
			orientation :"lr-tb"
			padding:10
			MDLabel:
				text:""
				font_name:"assets/Poppins-Bold.ttf"
				font_size:"15sp"
			MDLabel:
				text:"ADMISSION & WITHDRAWAL POLICY"
				font_name:"assets/Poppins-Bold.ttf"
			MDLabel:
				text:" • Syllabus for entrance test will be given at the reception."
				font_name:"assets/Poppins-Regular.ttf"
				font_size:"15sp"
			MDLabel:
				text:""
				font_name:"assets/Poppins-Bold.ttf"
				font_size:"15sp"
			MDLabel:
				text:"•Original Birth certificate from the municipal corporation is to be produced at the time of admission, along with photocopy of aadhar card, school leaving certificate and recent passport sized photograph."
				font_name:"assets/Poppins-Regular.ttf"
				font_size:"15sp"
			MDLabel:
				text:""
				font_name:"assets/Poppins-Bold.ttf"
				font_size:"15sp"
			MDLabel:
				text:"• Students are admitted to various classes on the basis of their entrance tests/interviews depending on the availability of seats in the school"
				font_name:"assets/Poppins-Regular.ttf"
				font_size:"15sp"
			MDLabel:
				text:""
				font_name:"assets/Poppins-Bold.ttf"
				font_size:"15sp"			
			MDLabel:
				text:"• Date of birth once entered will not be altered in any instance."
				font_name:"assets/Poppins-Regular.ttf"
				font_size:"15sp"	
			MDLabel:
				text:""
				font_name:"assets/Poppins-Bold.ttf"
				font_size:"15sp"			
			MDLabel:
				text:"• The selection of the candidates will be done at the discretion of the Principal. Guardian or anybody else will not have any right to admit any child in any class."
				font_name:"assets/Poppins-Regular.ttf"
				font_size:"15sp"
			MDLabel:
				text:""
				font_name:"assets/Poppins-Bold.ttf"
				font_size:"15sp"
			MDLabel:
				text:"•  In case guardian wants to admit, then consent letter from the parents is required. If it is found that a false document is submitted, admission will be cancelled and guardian alone will be responsible for all consequences."
				font_name:"assets/Poppins-Regular.ttf"
				font_size:"15sp"
			MDLabel:
				text:""
				font_name:"assets/Poppins-Bold.ttf"
				font_size:"15sp"
			MDLabel:
				text:"• The school allows concession of Rs.100 in fee to the younger child if two real brother/sister are studying in the school. The parents have to apply in the month of April to avail this opportunity, afterwards no application will be entertained."
				font_name:"assets/Poppins-Regular.ttf"
				font_size:"15sp"
			MDLabel:
				text:""
				font_name:"assets/Poppins-Bold.ttf"
				font_size:"15sp"				
			MDLabel:
				text:"• Student can be removed or withdrawn from the school by giving one month's notice in writing."
				font_name:"assets/Poppins-Regular.ttf"
				font_size:"15sp"
			MDLabel:
				text:""
				font_name:"assets/Poppins-Bold.ttf"
				font_size:"15sp"						
	"""
	modal = ModalView(
	background_color=[0,0,0,0],
	size_hint=(0.8, 0.8),

	overlay_color=(0, 0, 0, 0),

	)

	modal.add_widget(Builder.load_string(a))
	modal.open()			
def show_fees():
	card = MDCard(elevation=50,radius=[30,30,30,30],size=(0.83,0.7))
	a = MDDataTable(
	size=(0.8,0.8),
	use_pagination=True,
	column_data=[

	("Sr.No.", dp(20)),

	("Class", dp(20)),

	("Monthly Fees", dp(20))],
	row_data = (
		["1","Newly Admit Fees","₹ 15395"],
		["2","NUR - UKG ","₹ 3080"],
		["3","I - V","₹ 3100"],
		["4","VI - VIII","₹ 3235"],
		["5","IX - X","₹ 3360"],
		["6","XI - XII Science","₹ 3545"],
		["7","XI - XII Commerce/Arts","₹ 3380"],
		)
	)
	card.add_widget(a)
	modal = ModalView(
	background_color=[0,0,0,0],
	size_hint=(0.83, 0.7),

	overlay_color=(0, 0, 0, 0),

	)

	modal.add_widget(card)

	modal.open()	
def show_teachers():
	card = MDCard(elevation=50, radius=[30],size=(1,1))
	f = MDDataTable(
	size=(0.8,0.8),
	use_pagination=True,
	column_data=[

	("No.", dp(20)),

	("Name", dp(20)),

	("Designation", dp(20)),

	("Qualification", dp(20))],
	row_data = Teachers) 

	card.add_widget(f)
	modal = ModalView(
	background_color=[0,0,0,0],
	size_hint=(0.95, 0.95),

	overlay_color=(0, 0, 0, 0),

	)

	modal.add_widget(card)

	modal.open()
def get_part_of_day(h):
    return (
        "Morning"
        if 5 <= h <= 11
        else "Afternoon"
        if 12 <= h <= 17
        else "Evening"
        if 18 <= h <= 22
        else "Night"
    )
def getUpdate():
	url = "https://raw.githubusercontent.com/T-Dynamos/SRAPS-App/main/.srapsapp.filestobeupdated"
	ur = requests.get(url)
	files = (ur.text.replace("\n","")).split(",")
	for file in files:
		os.remove(file)
		url_file = "https://raw.githubusercontent.com/T-Dynamos/SRAPS-App/main/"+file
		r = requests.get(url_file)
		open(file, 'wb').write(r.content)
	
from datetime import datetime
from platform import python_version

class SRAPS_APP(MDApp):
	about_menu = lambda self: about_menu()
	update_menu=lambda self:update_menu()
	table = lambda self: show_teachers()
	settings = settings
	logs = settings.getSettings()["logs"]
	update = settings.getSettings()["update"]
	update2 = lambda self:settings.getSettings()["update"]
	python_version = python_version()
	__version__ = __version__
	y = y
	wid = lambda self:print()
	Teachers = Teachers
	spacing = Window.size[1]//20
	time = get_part_of_day(datetime.now().hour)
	screen_manager = screen_manager
	NI="assets/no-internet.png"
	News="No Internet"
	time = lambda self:show_timings()
	fees = lambda self:show_fees()
	adim = lambda self:show_adim()
	def colorHex(self, color):
		return get_color_from_hex(color)

	def build(self):
		self.theme_cls.primary_palette = settings.getSettings()["primary"]
		self.theme_cls.accent_palette = settings.getSettings()["accent"]		

		screen_manager.add_widget(Builder.load_file('main.kv'))
		screen_manager.current = "Mscreen"
		return screen_manager
	def start(self):
		if check_intr() == True:
			update_data()
		else:
			show_message()
	def on_start(self):
		_thread.start_new_thread(self.start,())
	
	def show_theme_picker(self):

		color_picker = MDColorPicker(size_hint=(0.45, 0.85))
		color_picker.open()
  	  
	def theme(self,theme):
		if theme == "Dark":
			theme1 = self.theme_cls.primary_dark
		else:
			theme1 = self.theme_cls.primary_light
		a = screen_manager.get_screen("Mscreen").ids
		a.t1.md_bg_color=theme1
		a.t2.md_bg_color=theme1
		a.t3.md_bg_color=theme1
		a.t4.md_bg_color=theme1
	def update_b(self):
		if screen_manager.get_screen("Mscreen").ids.hi.active is True:
			self.settings.writeSettings("update","True")
			self.theme("Dark") 
		else:
			self.settings.writeSettings("update","False")
			self.theme("Light")
	def update_a(self,a,b,c,d):
		b.text = "Checking ..."
		url = "https://raw.githubusercontent.com/T-Dynamos/SRAPS-App/main/.srapsapp.versionfile"
		ur = requests.get(url)
		if float(ur.text) ==  float (__version__):
			Toast("Already up Date")
			d.text = "UP TO DATE"
			b.text = "Updated Version : "+ur.text.replace("\n","")
		else:
			Toast("Updates Available : "+ur.text.replace("\n",""))
			time.sleep(3)
			Toast("Staring Auto Update")
			b.text = "Update Available : "+ur.text.replace("\n","")
			d.text = "Updating ..."
			try:
				getUpdate()
				Toast("Done Updating")
				d.text = "UP TO DATE"
				b.text = "Updated Version : "+ur.text.replace("\n","")
			except Exception as e:
				print(str(e))
				Toast("Unexpected Error"+str(e))
				d.text = "Error"
				b.text = "Unexpected Error"

#########################################

SRAPS_APP().run()
