# SOURCES
# https://www.youtube.com/watch?v=6gNpSuE01qE&t=135s
# uses BUILDOZER to build apk
# requires Linux
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
import kivy
from kivy.uix.screenmanager import Screen
from kivy.uix.filechooser import FileChooserListView
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.modalview import ModalView
from kivymd import images_path
from kivymd.uix.card import MDCard
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivy.core.window import Window

kivy.require('2.1.0')


class MyRoot(MDBoxLayout):

    def __init__(self):
        super(MyRoot, self).__init__()
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True,
        )

    def loadImage(self, path="451442263ad6573186beb1272cfadfc6.jpg"):
        self.inputImage.source = path

    def file_manager_open(self):
        self.file_manager.show('/')  # output manager to the screen
        self.manager_open = True

    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''

        self.exit_manager()
        self.inputImage.source = path
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


class ImgSuite(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Green"
        screen = MyRoot()
        return screen  # , MyRoot()


ImgSuite().run()
