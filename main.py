

__version__ = "2.02"


import kivy
from kivymd.uix.floatlayout import *
from kivy.uix.anchorlayout import *
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine
from kivymd.toast import toast as Toast2
from kivymd.app import *
from kivymd.uix.pickers import *
from kivymd.uix.label import *
from kivy.uix.image import *
from kivy.uix.label import *
from bs4 import BeautifulSoup
from kivy.uix.screenmanager import *
from kivy.lang import Builder
from kivymd.uix.button import *
from kivymd.uix.screen import *
from kivymd.uix.textfield import *
from kivy.core.audio import *
from kivymd.uix.list import *
from kivy.uix.scrollview import *
from kivymd.uix.button import MDFlatButton
from kivymd.uix.card import MDCard
from kivy.uix.modalview import ModalView
from kivymd.uix.datatables import MDDataTable
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.tab import *
import requests
import os
from kivy.clock import Clock
from kivy.utils import platform
from kivy.core.window import Window
from kivymd.uix.snackbar import Snackbar
import time
import settings
from kivymd.uix.behaviors import *
from kivy.metrics import dp
from kivymd.uix.fitimage import FitImage
from kivy import Logger
from kivy.factory import Factory
from kivy.properties import OptionProperty
from kivy.utils import get_color_from_hex
from kivy.uix.scatter import *
from kivymd.color_definitions import *
from kivymd.uix.behaviors import *
from kivymd.uix.button import MDIconButton
from kivymd.uix.circularlayout import MDCircularLayout
from kivymd.uix.dialog import BaseDialog
from kivymd.uix.label import *
from kivymd.uix.sliverappbar import *
from kivymd_extensions.akivymd.uix.loaders import *
from functools import partial

if platform == "android":
	from kivmob import KivMob
class MyMDCard(MDCard,FakeRectangularElevationBehavior):
	pass


try:
	from dataDb import Teachers
except Exception:
	Teachers=[]
	passls
	

screen_manager = ScreenManager()

class GLOBALs(Screen):
    pass


class CLASSs(Screen):
    pass


class SManager(ScreenManager):
    pass

class HeadItem(AnchorLayout):
	pass
class Tab(MDFloatLayout, MDTabsBase):
    pass

if platform != "android":
	Window.size = (Window.size[0]//2, Window.size[1])
y = Window.size[0]

def check_intr():
	try:
		requests.get("https://google.com",timeout=1)
	except Exception as e:
		loaderS(str(e))
		return False
	return True


class Tab(MDFloatLayout, MDTabsBase):
	pass


def loaderS(string):
	if string:
		print(f"[SRAPS-App] {string}")
	else:
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

def returnR(): 
	import random 
	a = [1,2,3]
	if random.choice(a) == 1:
		return True
	else:
		return False

def loadAD():
	if platform=="android":
		ads = KivMob("ca-app-pub-1400437871441093~9758605790")
		ads.new_interstitial("ca-app-pub-1400437871441093/3864750867")
		if returnR() == True:
			loaderS("Add Called")
			ads.request_interstitial()
		else:
			pass
	else:
		pass

def threadRun(func,args):
	Clock.schedule_once(partial(func,args))

def get_version():
	url = "https://raw.githubusercontent.com/T-Dynamos/SRAPS-App/main/.srapsapp.versionfile"
	url_Get = requests.get(url)
	if __version__ == url_Get.text:
		return "updated",url_Get.text
	else:
		return "available",url_Get.text

def genAvtar():
	import random
	no = str(random.randint(10,99))
	url = f"https://avatars.githubusercontent.com/u/6912{no}51?v=4"
	return url

def return_Sycn(url):
	import random
	try:
		path = f'assets/tmp-{random.random()}.{(url.split("."))[-1]}'
		r = requests.get(url, allow_redirects=True)
		open(path ,'wb').write(r.content)
		return path
	except Exception:
		return "assets/no-internet.png"

def showShort(words):
	  if len(words.split(" ")) >= 10:
	  	return words[:-(len(words.split(" "))-10)]+" ..."
	  else:
	  	return words


def update_data(*largs):
	o = screen_manager.get_screen("Mscreen").ids
	DataBase, links = getDb()
	o.news.text = str(DataBase["News"])		
	o.NI.source = str(DataBase["SliderImages"])
	add_part(links)
	for i in (requests.get("http://srapsapp.herokuapp.com/getGlobalNotification?pass=sraps").text).split("\n"):
		inf = i.replace("\n","")
		if inf != "":
			o.global_noti.add_widget(Builder.load_string(f"""
HeadItem:
	title:"{str(inf.split("`")[0])}"
	content:"{str(inf.split("`")[-1])}"
	avatar:'assets/logo.png'
	"""))
def Toast1(string,*largs):
	Toast2(string)

def Toast(string,*largs):
	loaderS(string)
	if platform=="android":
		Toast2(string,gravity=80)
	else:
		threadRun(Toast1,string)		

def update_menu():

	
	modal = Builder.load_string("""
#: import _thread _thread
ModalView:
	id:model
	background_color:[0,0,0,0]
	size_hint:(0.7, 0.5)
	overlay_color:(0, 0, 0, 0.6)
	
	MyMDCard:

		radius:"30dp"
		elevation:18
		orientation:"vertical"
		MDRelativeLayout:
			AnchorLayout:
				anchor_x:"left"
				anchor_y:"top"
				MDIconButton:
					on_press:model.dismiss()
					icon:"close"
			AnchorLayout:
				id:upd1		
				Image:
					id:upd
					source:"assets/update.png"
					size:(0.9,0.9)
					halign:"center"
					size_hint:None,None
					size:"70dp","70dp"
					anim_delay:0.05
		MDLabel:
			id:ud2
			text:"Currently Installed Version "+app.__version__
			font_name:"assets/Lato-Italic.ttf"
			font_size:"15sp"
			halign:"center"
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
				line_width:"1dp"
				on_press:upd.source = "assets/search.png";ud2.text = "Checking ...";_thread.start_new_thread(app.update_a,(upd1,ud2,upd,ud3))
		
	""")
	modal.open()	
def show_message():
		dialog=Snackbar(text="No internet!",
		snackbar_x="10dp",

		radius=[dp(10),dp(10),dp(10),dp(10)],
		snackbar_y="75dp",
		size_hint_x=.95)
		a = lambda self : (Toast("Updating data"),threadRun(update_data,()),dialog.dismiss())
		b = lambda self : Toast("Internet not connected")
		show_message_true = lambda self:show_message()
		c = lambda self : (dialog.dismiss(),Clock.schedule_once(show_message_true,5))
		d = lambda *largs : a(True) if check_intr() is True else b(True)
		e = lambda self:threadRun(d,())
		dialog.buttons = [
		MDFlatButton(text="RETRY",
			font_name="assets/Poppins-Regular.ttf",
			theme_text_color="Custom",
			text_color=[1,1,1,1],
			on_press = e), 
		MDFlatButton (text="CANCEL",
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
	radius:"30dp"
	elevation:18
	ScrollView:
		MDGridLayout:
			cols:1
			adaptive_height:True
			orientation:"lr-tb"
			spacing:app.y//5
			size_hint_y:None
			MDLabel:
			MDLabel:
				halign:"center"
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
"""
	modal = ModalView(
        background_color=[0,0,0,0],
        size_hint=(0.8, 0.8),
        overlay_color=(0, 0, 0, 0.7),
	)

	modal.add_widget(Builder.load_string(a))
	modal.open()
Builder.load_string(
    """
<Tab@MDFloatLayout+MDTabsBase+CommonElevationBehavior>
    md_bg_color: app.theme_cls.bg_normal


<ColorSelector>
    canvas:
        Color:
            rgba: root.rgb_hex(root.color_name)
        Ellipse:
            size: self.size
            pos: self.pos


<AccentColorSelector@ColorSelector>
    on_release: app.accent(root.color_name)

<PrimaryColorSelector@ColorSelector>
    on_release: app.primary(root.color_name)

<MDThemePicker>
    size_hint: None, None
    size: "284dp", "400dp"
	MyMDCard:
		radius:"40dp"
        MDTabs:
            tab_hint_x: True
            on_tab_switch: root.on_tab_switch(*args)

			Tab:
                id: theme_tab
                title: "Theme"
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
                title: "Accent"
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
	radius:"20dp"
	size:(0.85,0.85)
	elevation:50
	orientation:"vertical"
	ScrollView:

		MDGridLayout:
			cols:1
			adaptive_height:True
			spacing:app.spacing*3
			id : boxi
			orientation :"lr-tb"
			padding:10
			MyMDCard:
				radius:"20dp"
				size_hint:None,None
				size:"300dp","300dp"
				id:oo
				FitImage:
					source:"assets/time.jpg"
					allow_stretch:True
					keep_ratio :True
					radius:"20dp"
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
        overlay_color=(0, 0, 0, 0.7),
	)

	modal.add_widget(Builder.load_string(a))
	modal.open()	
	
	
def about_menu():
	pass

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
        overlay_color=(0, 0, 0, 0.7),
	)

	modal.add_widget(Builder.load_string(a))
	modal.open()		
def load_img(img):
	size = '{"center_x":0.5,"center_y":0.1}'
	
	
	a = f"""
MyMDCard:
	id:f
	raidus:"30dp"
	orientation:"vertical"
	RelativeLayout:
		id:fu
		Scatter:
			pos_hint_x:0.5
			pos_hiny_y:0.7
			AsyncImage:
				halign:"center"
				source:"{img}"
				size_hint:None,None
				size:(f.width,fu.height)
				keep_ratio:True
				allow_stretch:True
		BoxLayout:
			pos_hint:{size}
			size_hint:None,None			
			size:(f.width-dp(10),"30dp")
			orientation:"horizontal"

			AnchorLayout:
				id:ohm
				MDRaisedButton:
					size_hint:None,None
					size:(ohm.width-dp(8),ohm.height)
  		  		text: "Save to Gallery"
    				font_size: "18sp"
   		 		font_name: "assets/Poppins-Regular.ttf"
			BoxLayout:
			
				AnchorLayout:
					MDIconButton:
						icon:"share-variant-outline"   
				AnchorLayout:
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
	card = MyMDCard(elevation=18,radius=[30,30,30,30],size=(0.83,0.7))
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
        overlay_color=(0, 0, 0, 0.7),
	)

	modal.add_widget(card)

	modal.open()	
def show_teachers():
	f = MDDataTable(
	use_pagination=True,
	column_data=[

	("No.", dp(20)),

	("Name", dp(20)),

	("Designation", dp(20)),

	("Qualification", dp(20))],
	row_data = Teachers) 


	modal = ModalView(
        background_color=[0,0,0,0],
        size_hint=(None,None),
        size=(1,1),
        overlay_color=(0, 0, 0, 0.7),
	)

	modal.add_widget(f)

	modal.open()
def getStdInfo(soup_text) -> list:
    try:
        soup = BeautifulSoup(soup_text, 'html.parser')
    except Exception as e:
        return "Connection Error"

    stdinfo = []

    for i in  soup.find_all("li"):
    	ok = (str(i.get_text()).split("\n"))[0]
    	if ok.startswith("Admission No") or ok.startswith("St") or ok.startswith("Cl") or ok.startswith("Fa") or ok.startswith("Mo"):
            stdinfo.append(str(ok.split(":   ")[-1]).replace("<\\/label><\\/li>\r","").replace("<\\/span>",""))
    stdinfo.pop(0)
    return stdinfo


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

class SRAPS_APP_STUDENT(MDApp):
	av = lambda self:genAvtar()
	threadRun = lambda self,func,args:threadRun(func, args)
	show_ad = lambda self:loadAD()
	dday = get_part_of_day(datetime.now().hour)
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
	wid = lambda self:loaderS("Function called")
	Teachers = Teachers
	spacing = Window.size[1]//20
	time = get_part_of_day(datetime.now().hour)
	screen_manager = screen_manager
	NI="assets/no-internet.png"
	News="No Internet"
	time = lambda self:show_timings()
	fees = lambda self:show_fees()
	adim = lambda self:show_adim()
	x= Window.size[1]
	title="SRAPS App"
	def colorHex(self, color):
		return get_color_from_hex(color)
	def myc(self):
		if screen_manager.get_screen("Mscreen").ids.hy3.icon == "chevron-right":
			screen_manager.get_screen("Mscreen").ids.hy3.icon = "chevron-down"
			screen_manager.get_screen("Mscreen").ids.a890.line_color = self.theme_cls.accent_color
			screen_manager.get_screen("Mscreen").ids.a890.icon_color = self.theme_cls.accent_color
			screen_manager.get_screen("Mscreen").ids.a890.text_color = self.theme_cls.accent_color
		
			screen_manager.get_screen("Mscreen").ids.a891.line_color = self.theme_cls.accent_color
			screen_manager.get_screen("Mscreen").ids.a891.icon_color = self.theme_cls.accent_color
			screen_manager.get_screen("Mscreen").ids.a891.text_color = self.theme_cls.accent_color						
		else:
			screen_manager.get_screen("Mscreen").ids.hy3.icon = "chevron-right"

			screen_manager.get_screen("Mscreen").ids.a890.line_color = 0,0,0,0
			screen_manager.get_screen("Mscreen").ids.a890.icon_color = 0,0,0,0
			screen_manager.get_screen("Mscreen").ids.a890.text_color = 0,0,0,0		
			screen_manager.get_screen("Mscreen").ids.a891.line_color = 0,0,0,0
			screen_manager.get_screen("Mscreen").ids.a891.icon_color = 0,0,0,0
			screen_manager.get_screen("Mscreen").ids.a891.text_color = 0,0,0,0				
	def build(self):
		self.theme_cls.material_style = "M3"
		self.theme_cls.primary_palette = settings.getSettings()["primary"]
		self.theme_cls.accent_palette = settings.getSettings()["accent"]		
		if settings.getSettings()["update"] == True:
			self.theme_cls.theme_style = 'Dark'
		else:
			self.theme_cls.theme_style = 'Light'
		screen_manager.add_widget(Builder.load_file('screens/student.kv'))
		screen_manager.current = "Mscreen"
		return screen_manager
	def kl(self,*args):
		screen_manager.get_screen("Mscreen").ids.test.avatar = genAvtar()
		screen_manager.get_screen("Mscreen").ids.test1.avatar = genAvtar()
		screen_manager.get_screen("Mscreen").ids.test2.avatar = genAvtar()
		screen_manager.get_screen("Mscreen").ids.test3.avatar = genAvtar()
		screen_manager.get_screen("Mscreen").ids.test4.avatar = genAvtar()
		screen_manager.get_screen("Mscreen").ids.test5.avatar = genAvtar()
	def start(self,*largs):
		show_message() if check_intr() == False else update_data()
	def on_start(self):
		threadRun(self.start,())
	def accent(self,color):
		self.theme_cls.accent_palette = color 
		settings.writeSettings("accent",f"{color}.{self.theme_cls.primary_palette}")
	def primary(self,color):
		self.theme_cls.primary_palette = color 
		settings.writeSettings("primary",f"{color}.{self.theme_cls.accent_palette}")
	def show_theme_picker(self):
	 	  theme_picker()
			
	def theme(self):		
		if screen_manager.get_screen("Mscreen").ids.hi.active == False:
			self.settings.writeSettings("update","False")
			self.theme_cls.theme_style = "Light"
			screen_manager.get_screen("Mscreen").ids.rimg.source = "assets/shadow-white.png" 
		else:
			self.settings.writeSettings("update","True")
			self.theme_cls.theme_style = "Dark"
			screen_manager.get_screen("Mscreen").ids.rimg.source = "assets/shadow-black.png" 
	def update_a(self,a,b,c,d):
		b.text = "Checking ..."
		url = "https://raw.githubusercontent.com/T-Dynamos/SRAPS-App/main/.srapsapp.versionfile"
		try:
			ur = requests.get(url)
		except Exception as e:
			Toast("Unexpected Error : "+str(e))
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
				c.source = "assets/update.png"
			except Exception as e:
				loaderS(str(e))
				Toast("Unexpected Error"+str(e))
				d.text = "Error"
				b.text = "Unexpected Error"

#########################################

class SRAPS_APP_TEACHER(MDApp):
	__version__ = __version__
	python_version = python_version()
	y = y
	about_menu = lambda self: about_menu()
	update_menu=lambda self:update_menu()
	settings = settings
	logs = settings.getSettings()["logs"]
	show_theme_picker = lambda self:theme_picker()

	update = settings.getSettings()["update"]	
	def build(self):
		self.theme_cls.material_style = "M3"
		screen_manager.add_widget(Builder.load_file("screens/teacher.kv"))
		return screen_manager
	def myc(self):	
		if screen_manager.get_screen("Tscreen").ids.hy3.icon == "chevron-right":
			screen_manager.get_screen("Tscreen").ids.hy3.icon = "chevron-down"
			screen_manager.get_screen("Tscreen").ids.a890.line_color = self.theme_cls.accent_color
			screen_manager.get_screen("Tscreen").ids.a890.icon_color = self.theme_cls.accent_color
			screen_manager.get_screen("Tscreen").ids.a890.text_color = self.theme_cls.accent_color
		
			screen_manager.get_screen("Tscreen").ids.a891.line_color = self.theme_cls.accent_color
			screen_manager.get_screen("Tscreen").ids.a891.icon_color = self.theme_cls.accent_color
			screen_manager.get_screen("Tscreen").ids.a891.text_color = self.theme_cls.accent_color						
		else:
			screen_manager.get_screen("Tscreen").ids.hy3.icon = "chevron-right"

			screen_manager.get_screen("Tscreen").ids.a890.line_color = 0,0,0,0
			screen_manager.get_screen("Tscreen").ids.a890.icon_color = 0,0,0,0
			screen_manager.get_screen("Tscreen").ids.a890.text_color = 0,0,0,0		
			screen_manager.get_screen("Tscreen").ids.a891.line_color = 0,0,0,0
			screen_manager.get_screen("Tscreen").ids.a891.icon_color = 0,0,0,0
			screen_manager.get_screen("Tscreen").ids.a891.text_color = 0,0,0,0
	def update_a(self,a,b,c,d):
		b.text = "Checking ..."
		url = "https://raw.githubusercontent.com/T-Dynamos/SRAPS-App/main/.srapsapp.versionfile"
		try:
			ur = requests.get(url)
		except Exception as e:
			Toast("Unexpected Error : "+str(e))
			return None
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
				c.source = "assets/update.png"
			except Exception as e:
				loaderS(str(e))
				Toast("Unexpected Error"+str(e))
				d.text = "Error"
				b.text = "Unexpected Error"
	def theme(self):
		if screen_manager.get_screen("Tscreen").ids.hi.active == False:
			self.settings.writeSettings("update","False")
			self.theme_cls.theme_style = "Light"
			screen_manager.get_screen("Tscreen").ids.rimg.source = "assets/shadow-white.png" 
		else:
			self.settings.writeSettings("update","True")
			self.theme_cls.theme_style = "Dark"
			screen_manager.get_screen("Tscreen").ids.rimg.source = "assets/shadow-black.png" 
	def accent(self,color):
		self.theme_cls.accent_palette = color 
		settings.writeSettings("accent",f"{color}.{self.theme_cls.primary_palette}")
	def primary(self,color):
		self.theme_cls.primary_palette = color 
		settings.writeSettings("primary",f"{color}.{self.theme_cls.accent_palette}")


class SRAPS_APP_STARTUP(MDApp):
	y=y
	x=Window.size[1]
	screen_manager=screen_manager
	Toast =lambda self ,string:Toast(string)
	number = ""
	controler = requests.session()
	def build(self):

		self.title="SRAPS App"
		self.theme_cls.material_style = "M3"
		screen_manager.add_widget(Builder.load_string(open("screens/startup.kv").read().split("~~~")[0]))
		screen_manager.add_widget(Builder.load_string(open("screens/startup.kv").read().split("~~~")[-2]))
		screen_manager.add_widget(Builder.load_string(open("screens/startup.kv").read().split("~~~")[-1]))		
		screen_manager.current = "Sscreen"
		return screen_manager
	def on_save(self, instance, value, date_range):
		screen_manager.get_screen("Sscreen2").ids.ran.text = "Selected DOB : "+str(value)

	def show_date_picker(self):
		date_dialog = MDDatePicker()
		date_dialog.bind(on_save=self.on_save,on_ok_button_pressed=self.on_save)
		date_dialog.open()

	def sAdim(self,*largs):
		self.admno = str(self.admno[-1])
		self.dob = str(self.dob)
		import time
		time.sleep(3)
		try:
			head = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
"Accept":"/","X-Requested-With":"XMLHttpRequest"}
			req = self.controler.post("http://www.shriramashramps.org/feecontroller.php",data=f"admno={self.admno}&action=send_otp&stddob={self.dob}",headers=head)

		except Exception as e:
			print(e)
			return self.modal.dismiss();Toast("No Internet !")
		if "OTP" in req.text:
			Toast("Otp send successfully")
			self.number = (req.text.split("<\\/h5>")[0]).split("On ")[-1]

			self.modal.dismiss()
			threadRun(self.verify_otp,(self.admno))
		else:
			Toast("Student not found !")
			self.modal.dismiss()
	def get_creds(self,otp):
		def est():
			a  = self.controler.post("http://www.shriramashramps.org/feecontroller.php",data=f"otp={otp}&action=verify_otp",headers={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Accept":"/","X-Requested-With":"XMLHttpRequest"})
			if '"type":"error"' in (a.text):
				Toast("Invaild OTP ")
			else:
				Toast(str(getStdInfo(open(a.text.replace("\\","")))))
				self.modal.dismiss()
		import _thread
		_thread.start_new_thread(est,())
	def verify_otp(self,admno,*largs):

	
		modal = Builder.load_string("""
#: import _thread _thread
ModalView:
	id:model
	background_color:[0,0,0,0]
	size_hint:None,None
	size:app.y-dp(30),"400dp"
	overlay_color:(0, 0, 0, 0.6)
	
	MyMDCard:

		radius:"30dp"
		elevation:18
		orientation:"vertical"
		MDRelativeLayout:
			AnchorLayout:
				anchor_x:"left"
				anchor_y:"top"
				MDIconButton:
					on_press:model.dismiss()
					icon:"close"
			AnchorLayout:
				id:upd1		
				Image:
					id:upd
					source:"assets/otp.png"
					size:(0.9,0.9)
					halign:"center"
					size_hint:None,None
					size:"70dp","70dp"
					anim_delay:0.05
		MDLabel:
			id:ud2
			text:"Please enter the OTP sent on "+app.number
			font_name:"assets/Lato-Italic.ttf"
			font_size:"15sp"
			halign:"center"
		MDBoxLayout:
			pos_hint:{"center_x":0.5,"center_y":0.7}
			size_hint:None,None
			size:dp(200),"50dp"
			MDTextField:
				id:otp
				hint_text:"Enter the OTP"	
				mode: "rectangle"
				max_text_length:6
				font_name:"assets/Poppins-Regular.ttf"
				font_name_hint_text:"assets/Poppins-Regular.ttf"			
		AnchorLayout:
			orientation:"vertical"
			anchor_x:'center'
			anchor_y:'center'
			MDFlatButton:
				id:ud3
				text:"Verify"
				font_name:"assets/Poppins-Regular.ttf"
				font_size:"15sp"
				halign:"center"
				line_width:"1dp"
				size_hint:None,None
				size:dp(150),"50dp"
				md_bg_color:app.theme_cls.primary_light
				line_color:app.theme_cls.primary_light
				on_press:app.get_creds(otp.text)
				
		""")
		modal.open()
		self.modal = modal
	def get_admno(self):			
		modal = Builder.load_string("""
ModalView:
	id:model
	background_color:[0,0,0,0]
	size_hint:None,None
	size:app.y,app.x
	overlay_color:(0, 0, 0, 0)
	MDBoxLayout:
		md_bg_color:0,0,0,0.7
		size_hint:None,None
		size:app.y,app.x
		
		RelativeLayout:
			MDLabel:
				pos_hint:{"center_x":0.5,"center_y":0.76}
				text:"Locating "+app.screen_manager.get_screen("Sscreen2").ids.admno.text
				font_name:"assets/Poppins-Regular.ttf"
				font_size:"25sp"
				halign:"center"
				theme_text_color:"Custom"
				text_color:app.theme_cls.primary_light
			MDSpinner:

				id:ok4
				pos_hint:{"center_x":0.5,"center_y":0.38}
				size_hint: None, None
				size: dp(40), dp(40)
				pos_hint: {'center_x': .5, 'center_y': .5}
				palette:[app.theme_cls.primary_light,app.theme_cls.accent_light,app.theme_cls.primary_light,app.theme_cls.accent_light]

	""")
		threadRun(modal.open,())
		self.admno =  str(screen_manager.get_screen("Sscreen2").ids.admno.text),
		self.dob = str((screen_manager.get_screen("Sscreen2").ids.ran.text).split(": ")[-1])
		self.modal = modal
		import _thread	
		_thread.start_new_thread(self.sAdim,
			())
		
SRAPS_APP_STARTUP().run()
