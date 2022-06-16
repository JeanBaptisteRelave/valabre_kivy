from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class cApp(App):
    def build(self):
        return BoxLayout()

myApp = cApp()
myApp.run()