# SOURCES
# https://www.youtube.com/watch?v=6gNpSuE01qE&t=135s
# uses BUILDOZER to build apk
# requires Linux
import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
import random

kivy.require('2.1.0')


class MyRoot(BoxLayout):

    def __init__(self):
        super(MyRoot, self).__init__()

    def generate_number(self):
        self.random_label.text = str(random.randint(0, 1000))


class ImgSuite(App):

    def build(self):
        return MyRoot()


neuralRandom = ImgSuite()
neuralRandom.run()
