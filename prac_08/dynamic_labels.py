from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    """ Create Labels from a list of names """

    def __init__(self, **kwargs):
        """ Constructing main app """
        super().__init__(**kwargs)
        self.names = ["David", "Helen", "Haruko", "Yukari"]

    def build(self):
        """ Building the Kivy app from the kv file """
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """ Putting the names into the app """
        for name in self.names:
            temp_button = Label(text=name)
            self.root.ids.label_box.add_widget(temp_button)

DynamicLabelsApp().run()