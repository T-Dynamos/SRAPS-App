

__version__ = "2.0"


import kivy
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import *
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
from kivymd.uix.card import *
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
from kivymd.uix.tab import *
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
from kivymd.uix.dialog import MDDialog
from functools import partial
import settings
from android.runnable import run_on_ui_thread
from jnius import autoclass
from kivymd.uix.behaviors import *
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivymd.uix.fitimage import FitImage
from kivy import Logger
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.event import EventDispatcher
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.behaviors import ButtonBehavior, FocusBehavior
from kivy.graphics.transformation import Matrix
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.utils import get_color_from_hex
from kivy.vector import Vector
from kivy.uix.scatter import *
from kivymd.color_definitions import colors, palette
from kivymd.theming import ThemableBehavior
from kivymd.toast import toast
from kivymd.uix.behaviors import (
    CircularRippleBehavior,
    FakeRectangularElevationBehavior,
    SpecificBackgroundColorBehavior,
)
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.circularlayout import MDCircularLayout
from kivymd.uix.dialog import BaseDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.tooltip import MDTooltip
from kivy.uix.relativelayout import RelativeLayout 
class MyMDCard(MDCard,FakeRectangularElevationBehavior):
	pass

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
class Tab(MDFloatLayout, MDTabsBase):
	pass
	
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
MyMDCard:
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
		font_name:"assets/Lato-Italic.ttf"
		font_size:"15sp"
		hailgn:"center"
	AnchorLayout:
		orientation:"vertical"
		anchor_x:'center'
		anchor_y:'center'
		MDRoundFlatButton:
			id:ud3
			text:"Check for Update"
			font_name:"assets/Lato-Italic.ttf"
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
		snackbar_y="75dp",
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
		card = MyMDCard(
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
		card = MyMDCard(
		radius=[20],
		padding=10,
		halign="center",
		elevation=0,
		size_hint=(None,None),
		size= (y-y//8, "200dp"),
		md_bg_color=[0,0,0,1],
		)
		image = AsyncImage (source=link, allow_stretch=True,keep_ratio=False, width="200dp")
		a = AnchorLayout ()
		card.add_widget(image)
		a.add_widget(card)
		o = screen_manager.get_screen("Mscreen").ids
		for i in range(1,6):
			o.fu.add_widget(MDLabel ())	
		o.fu.add_widget(a)
def booklist():
	a = """
MyMDCard:
	id:hi
	radius:30
	elevation:60
	ScrollView:
		GridLayout:
			cols:1
			adaptive_height:True
			orientation:"lr-tb"
			spacing:app.y//5
			size_hint_y:None
			MDLabel:
			MDLabel:
				text:"Choose Class"
				font_name:"assets/Poppins-Bold.ttf"
				font_size:"25sp"
			AnchorLayout:
				MDRectangleFlatButton:
    				text: "NUR"
    				font_name:"assets/Lato-Italic.ttf"
   				 theme_text_color: "Custom"
   				 line_width:3
   				 size:(hi.width-hi.width//10,"50dp")
   				 on_press:app.load_img("https://i.postimg.cc/5yXynH8w/0003.jpg")
			AnchorLayout:
				MDRectangleFlatButton:
    				text: "UKG"
    				font_name:"assets/Lato-Italic.ttf"
   				 theme_text_color: "Custom"
   				 line_width:3
   				 size:(hi.width-hi.width//10,"50dp")
			AnchorLayout:
				MDRectangleFlatButton:
    				text: "LKG"
    				font_name:"assets/Lato-Italic.ttf"
   				 theme_text_color: "Custom"
   				 line_width:3
   				 size:(hi.width-hi.width//10,"50dp")   				 
			AnchorLayout:
				MDRectangleFlatButton:
    				text: "1st"
    				font_name:"assets/Lato-Italic.ttf"
   				 theme_text_color: "Custom"
   				 line_width:3
   				 size:(hi.width-hi.width//10,"50dp")
			AnchorLayout:
				MDRectangleFlatButton:
    				text: "2nd"
    				font_name:"assets/Lato-Italic.ttf"
   				 theme_text_color: "Custom"
   				 line_width:3
   				 size:(hi.width-hi.width//10,"50dp")

			AnchorLayout:
				MDRectangleFlatButton:
    				text: "3rd"
    				font_name:"assets/Lato-Italic.ttf"
   				 theme_text_color: "Custom"
   				 line_width:3
   				 size:(hi.width-hi.width//10,"50dp")

			AnchorLayout:
				MDRectangleFlatButton:
    				text: "4th"
    				font_name:"assets/Lato-Italic.ttf"
   				 theme_text_color: "Custom"
   				 line_width:3
   				 size:(hi.width-hi.width//10,"50dp")
			AnchorLayout:
				MDRectangleFlatButton:
    				text: "5th"
    				font_name:"assets/Lato-Italic.ttf"
   				 theme_text_color: "Custom"
   				 line_width:3
   				 size:(hi.width-hi.width//10,"50dp")
			AnchorLayout:
				MDRectangleFlatButton:
    				text: "6th"
    				font_name:"assets/Lato-Italic.ttf"
   				 theme_text_color: "Custom"
   				 line_width:3
   				 size:(hi.width-hi.width//10,"50dp")
			AnchorLayout:
				MDRectangleFlatButton:
    				text: "7th"
    				font_name:"assets/Lato-Italic.ttf"
   				 theme_text_color: "Custom"
   				 line_width:3
   				 size:(hi.width-hi.width//10,"50dp")
			AnchorLayout:
				MDRectangleFlatButton:
    				text: "8th"
    				font_name:"assets/Lato-Italic.ttf"
   				 theme_text_color: "Custom"
   				 line_width:3
   				 size:(hi.width-hi.width//10,"50dp")
			AnchorLayout:
				MDRectangleFlatButton:
    				text: "9th"
    				font_name:"assets/Lato-Italic.ttf"
   				 theme_text_color: "Custom"
   				 line_width:3
   				 size:(hi.width-hi.width//10,"50dp")
			AnchorLayout:
				MDRectangleFlatButton:
    				text: "10th"
    				font_name:"assets/Lato-Italic.ttf"
   				 theme_text_color: "Custom"
   				 line_width:3
   				 size:(hi.width-hi.width//10,"50dp")
			AnchorLayout:
				MDRectangleFlatButton:
    				text: "+1"
    				font_name:"assets/Lato-Italic.ttf"
   				 theme_text_color: "Custom"
   				 line_width:3
   				 size:(hi.width-hi.width//10,"50dp")
			AnchorLayout:
				MDRectangleFlatButton:
    				text: "+2"
    				font_name:"assets/Lato-Italic.ttf"
   				 theme_text_color: "Custom"
   				 line_width:3
   				 size:(hi.width-hi.width//10,"50dp")
			MDLabel:
			MDLabel:
			MDLabel:
"""
	modal = ModalView(
	background_color=[0,0,0,0],
	size_hint=(0.8, 0.8),

	overlay_color=(0, 0, 0, 0),

	)

	modal.add_widget(Builder.load_string(a))
	modal.open()	
Builder.load_string(
    """
<Tab@MDFloatLayout+MDTabsBase>
    md_bg_color: app.theme_cls.bg_normal


<ColorSelector>
    canvas:
        Color:
            rgba: root.rgb_hex(root.color_name)
        Ellipse:
            size: self.size
            pos: self.pos


<AccentColorSelector@ColorSelector>
    on_release: app.theme_cls.accent_palette = root.color_name; app.settings.writeSettings("accent",root.color_name)


<PrimaryColorSelector@ColorSelector>
    on_release: app.theme_cls.primary_palette = root.color_name; app.settings.writeSettings("primary",root.color_name)


<MDThemePicker>
    size_hint: None, None
    size: "284dp", "400dp"

    MyMDCard:
        radius:50
        orientation: "vertical"

		MDToolbar:
		    title:"Change Theme"
		    font_name:"assets/Poppins-Bold.ttf"
		    
		    
        MDTabs:
            on_tab_switch: root.on_tab_switch(*args)

            Tab:
                id: theme_tab
                text: "Theme"
                font_name:"assets/Lato-Italic.ttf"

                MDGridLayout:
                    id: primary_box
                    adaptive_size: True
                    spacing: "8dp"
                    padding: "12dp"
                    pos_hint: {"center_x": .5, "top": 1}
                    cols: 5
                    rows: 4

                MDFlatButton:
                    text: "CLOSE"
                    pos: root.width - self.width - 10, 10
                    on_release: root.dismiss()

            Tab:
                text: "Accent"
                font_name:"assets/Lato-Italic.ttf"

                MDGridLayout:
                    id: accent_box
                    adaptive_size: True
                    spacing: "8dp"
                    padding: "12dp"
                    pos_hint: {"center_x": .5, "top": 1}
                    cols: 5
                    rows: 4

                MDFlatButton:
                    text: "CLOSE"
                    pos: root.width - self.width - 10, 10
                    on_release: root.dismiss()

"""
)


class ColorSelector(MDIconButton):
    color_name = OptionProperty("Indigo", options=palette)

    def rgb_hex(self, col):
        return get_color_from_hex(colors[col][self.theme_cls.accent_hue])


class MDThemePicker(
    BaseDialog
):
    def on_open(self):
        self.on_tab_switch(None, self.ids.theme_tab, None, None)

    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        if instance_tab.text == "Theme":
            if not self.ids.primary_box.children:
                for name_palette in palette:
                    self.ids.primary_box.add_widget(
                        Factory.PrimaryColorSelector(color_name=name_palette)
                    )
        if instance_tab.text == "Accent":
            if not self.ids.accent_box.children:
                for name_palette in palette:
                    self.ids.accent_box.add_widget(
                        Factory.AccentColorSelector(color_name=name_palette)
                    )

def theme_picker():
	c = MDThemePicker()
	c.open()
def show_timings():

	a = """
MyMDCard:
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
			radius:30
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
MyMDCard:
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
			radius:30
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
MyMDCard:
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
def load_img(img):
	a = f"""
MyMDCard:
	id:f
	raidus:30
	elevation:60
	orientation:"vertical"
	MDLabel:
	MDLabel:
	AnchorLayout:
		id:fu
		anchor_x:"center"
		anchor_y:"bottom"
		Scatter:
			id:ok			
			do_rotation:False
			do_scale:True
			AsyncImage:
				halign:"center"
				source:"{img}"
				size:(fu.width,fu.height*3.3)
				keep_ratio:False
				allow_stretch:True
	BoxLayout:
		size:(f.width-f.width//15,"50dp")
		orientation:"horizontal"
		padding:50
		MDRaisedButton:
  		  text: "Save to Gallery"
    		font_size: "18sp"
   		 font_name: "assets/Poppins-Regular.ttf"
		MDIconButton:
			icon:"share-variant-outline"   
		MDIconButton:
			icon:"whatsapp"		 	
"""	
	modal = ModalView(
	background_color=[0,0,0,0],
	size_hint=(0.83, 0.7),

	overlay_color=(0, 0, 0, 0),

	)

	modal.add_widget(Builder.load_string(a))

	modal.open()	
def show_fees():
	card = MyMDCard(elevation=50,radius=[30,30,30,30],size=(0.83,0.7))
	a = MDDataTable(
	size=(0.8,0.8),
	use_pagination=True,
	column_data=[

	("Sr.No.", dp(20)),

	("Class", dp(20)),

	("Monthly Fees", dp(20))
	],
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
	card = MyMDCard(elevation=50, radius=[30],size=(1,1))
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
		os.remove(os.getcwd()+"/"+file)
		url_file = "https://raw.githubusercontent.com/T-Dynamos/SRAPS-App/main/"+file
		r = requests.get(url_file)
		open(file, 'wb').write(r.content)
	
from datetime import datetime
from platform import python_version

class SRAPS_APP(MDApp):
	load_img = lambda self,img:load_img(img)
	booklist = lambda self:booklist()
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
		self.theme_cls.material_style = "M3"
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
	 	  theme_picker()
  	  
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
