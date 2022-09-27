# SOURCES
# https://www.youtube.com/watch?v=6gNpSuE01qE&t=135s
# uses BUILDOZER to build apk, requires Linux
# https://stackoverflow.com/questions/51913956/kivy-user-touch-and-drag-for-cropping-function

import time
import shutil
import os
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
import kivy
from kivy.uix.screenmanager import Screen
from kivy.uix.filechooser import FileChooserListView

from kivymd import images_path
from kivymd.uix.screen import MDScreen
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivy.core.window import Window
from sympy import content
from kivy.core.image import Image as CoreImage
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics import Point
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from PIL import Image
import modules.adaptiveThresholding as adThresh
import modules.histogramEqualization as histEq
from ImgSwtImage import ImgSwtImage
from Project import Project

kivy.require('2.1.0')


class MyRoot(MDScreen):

    image = ImgSwtImage()
    project = Project()
    
    
    def __init__(self):
        super(MyRoot, self).__init__()
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True,
        )
        # Initializes the image which is temporary data
        self.image = ImgSwtImage()
        # Initializes the project data for use and later saving
        self.project = Project()

    

    def file_manager_open(self):
        self.file_manager.show('/')  # output manager to the screen
        self.manager_open = True

    def equalizeImage(self):
        newPath = self.project.getNewPath(self.image)
        histEq.histogram_Equalization(
            self.image.path,newPath, 0, self.image.imageHeight, 0, self.image.imageWidth)
        self.image.loadImage(newPath, self, self.project)

    def thresholdImage(self):
        newPath = self.project.getNewPath(self.image)
        adThresh.adaptive_Thresholding(self.image.path, newPath, "Gaussian")
        self.image.loadImage(newPath, self, self.project)


    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''

        self.exit_manager()
        self.image.path = path
        newPath = self.project.getNewPath(self.image)
        shutil.copy(path,newPath)
        self.image.loadImage(newPath,self,self.project)
        toast(self.image.path)

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
