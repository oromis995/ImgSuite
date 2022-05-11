# SOURCES
# https://www.youtube.com/watch?v=6gNpSuE01qE&t=135s
# uses BUILDOZER to build apk, requires Linux
# https://stackoverflow.com/questions/51913956/kivy-user-touch-and-drag-for-cropping-function

import time
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
import kivy
from kivy.uix.screenmanager import Screen
from kivy.uix.filechooser import FileChooserListView
from kivymd.uix.button import MDRectangleFlatButton
from kivymd import images_path
from kivymd.uix.screen import MDScreen
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivy.core.window import Window
from sympy import content
from kivy.core.image import Image as CoreImage
import segmentation
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics import Point
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from PIL import Image
from ComputerVisionAlgorithms import ComputerVisionAlgorithms

kivy.require('2.1.0')


class MyRoot(MDScreen):

    path = "Intro.png"
    image = CoreImage(path)
    imageHeight = image.height
    imageWidth = image.width
    # Canvas Variables
    #rect_box = ObjectProperty(None)
    #t_x = NumericProperty(0.0)
    #t_y = NumericProperty(0.0)
    #x1 = y1 = x2 = y2 = NumericProperty(0.0)

    def __init__(self):
        super(MyRoot, self).__init__()
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True,
        )

    def loadImage(self, path):
        self.path = path
        self.imageViewer.source = path
        self.image = CoreImage(path)
        self.imageHeight = self.image.height
        self.imageWidth = self.image.width
        self.imgHeightLabel.text = ("Image Height: " + str(self.imageHeight))
        self.imgWidthLabel.text = ("Image Width: " + str(self.imageWidth))

    def file_manager_open(self):
        self.file_manager.show('/')  # output manager to the screen
        self.manager_open = True

    def equalizeImage(self):
        ComputerVisionAlgorithms.histogram_equalization(
            self.path, 100, 500, 100, 500)
        self.loadImage("equalizedImage.png")

    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''

        self.exit_manager()
        self.loadImage(path)
        toast(path)

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True

    # Canvas Functions
    # def enable_cropping(self):
    #    if(self.path != "Intro.png"):
    #        print("\nRootScreen:")
    #        print(self.ids.main_image.pos)
    #        print(self.ids.main_image.size)
    #       print("\tAbsolute size=", self.ids.main_image.norm_image_size)
    #        print("\tAbsolute pos_x=", self.ids.main_image.center_x -
    #             self.ids.main_image.norm_image_size[0] / 2.)
    #        print("\tAbsolute pos_y=", self.ids.main_image.center_y -
    #              self.ids.main_image.norm_image_size[1] / 2.)

    # def on_touch_down(self, touch):
        # checks whether on start screen
    #    if(self.path != "Intro.png"):
    #        self.x1 = touch.x
    #        self.y1 = touch.y
    #        self.t_x = touch.x
    #        self.t_y = touch.y
    #
    #        touch.grab(self)
    #        print(self.x1, self.y1)

    # def on_touch_move(self, touch):
    #    if touch.grab_current is self:
    #        # not working
    #        self.t_x = touch.x
    #        self.t_y = touch.y

    #        print(self.t_x, self.t_y)

    # def on_touch_up(self, touch):

    #    if touch.grab_current is self and self.path != "Intro.png":
    #        # final position
    #        self.x2 = touch.x
    #        self.y2 = touch.y

    #        print(self.x2, self.y2)


class ContentNavigationDrawer(MDBoxLayout):
    pass


class MyScreenManager(ScreenManager):
    pass


class ImgSuite(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Green"

        screen = MyRoot()
        screen.nav_drawer.set_state("closed")
        return screen


ImgSuite().run()
