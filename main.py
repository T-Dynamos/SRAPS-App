import kivy
from kivy.lang import Builder
from kivymd.app import *
from kivy.core.window import Window
from kivy.clock import Clock
import  webbrowser

code = """
RelativeLayout:
	AnchorLayout:
		anchor_y:"top"
		MDBoxLayout:
			size_hint:None,None
			size:app.y,"50dp"
			md_bg_color:app.theme_cls.primary_color
			MDLabel:
				text:"OpenURL"
				style:"H1"
				halign:"center"
	MDLabel:
		text:"This app open a link in default browser in every 10 secod."
		style:"H2"
		halign:"center"		
	MDLabel:
		pos_hint:{"center_x":0.5,"center_y":0.08}
		text:"© 2022 Amjad Ali"
		style:"H2"
		halign:"center"					

"""


class OpenUrl(MDApp):
	y=Window.size[1]
	def build(self):
		return Builder.load_string(code)
	def on_start(self):
		def ok(sefl):
			webbrowser.open("https://www.something.com/ijq2dcvp?key=7c1cc91e5b652aa50431cd8439173")
		Clock.schedule_interval(ok,300)

OpenUrl().run()