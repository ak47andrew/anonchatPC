from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.properties import NumericProperty

class LoadingSpinner(Widget):
    angle = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_animation()

    def start_animation(self):
        anim = Animation(angle=360, duration=1) + Animation(angle=0, duration=0)
        anim.repeat = True
        anim.start(self)