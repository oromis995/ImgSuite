# SOURCES
# https://www.youtube.com/watch?v=6gNpSuE01qE&t=135s
# uses BUILDOZER to build apk
# requires Linux
import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.image import Image

kivy.require('2.1.0')


class MyRoot(BoxLayout):

    def __init__(self):
        super(MyRoot, self).__init__()

    def loadImage(self):
        self.inputImage.source = "https://zunews.com/wp-content/uploads/2021/04/Screen-Shot-2021-04-01-at-1.48.27-PM.png"


class ImgSuite(App):

    def build(self):
        return MyRoot()


neuralRandom = ImgSuite()
neuralRandom.run()
