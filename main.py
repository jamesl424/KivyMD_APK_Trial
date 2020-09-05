# Kivy Imports
from kivy import Config
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.graphics.vertex_instructions import RoundedRectangle
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen, RiseInTransition, FallOutTransition

########################################################################################################################

# KivyMD Imports


from kivymd.app import MDApp
from kivymd.font_definitions import theme_font_styles
from kivymd.theming import ThemeManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDTextButton, MDFlatButton
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivymd.uix.expansionpanel import MDExpansionPanel
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.list import OneLineAvatarIconListItem, OneLineIconListItem
from kivymd.uix.screen import MDScreen
from kivymd.uix.tab import MDTabsBase

########################################################################################################################

class HomeScreen(MDScreen):
    pass

class PlantsScreen(MDScreen):
    pass

class TasksScreen(MDScreen):
    pass

class WikiScreen(MDScreen):
    pass

########################################################################################################################

class KivyMDTrial(MDApp) :
    dialog = None

    def build(self) :

        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "400"
        self.theme_cls.accent_pallette = "Yellow"
        self.theme_cls.accent_hue = "600"



        return Builder.load_file('.kv files/main.kv')

KivyMDTrial().run()