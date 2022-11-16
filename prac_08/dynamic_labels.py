from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.label import Label

class DynamicLabels(App):
    status_test = StringProperty

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.list_of_names = {"John Mutch", "Jill Hill", "Hoover Dam"}

    def build(self):
        self.title = "Dynamic Label Builder"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.list_of_names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)

DynamicLabels().run()