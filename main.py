import os
os.environ["KIVY_GL_BACKEND"] = "sdl2"
os.environ["SDL_VIDEO_MINIMIZE_ON_FOCUS_LOSS"] = "0"

from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

class TestApp(App):
    def build(self):
        Window.clearcolor = (0.1, 0.5, 0.1, 1)
        return Label(text="Mali GPU Fix Works!", font_size="40sp")

TestApp().run()
