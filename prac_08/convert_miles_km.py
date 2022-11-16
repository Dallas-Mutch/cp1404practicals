from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

M_TO_KM = 1.609344


class ConvertMilesKm(App):
    textfield = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self):
        result = self.get_valid_number()
        value = result * M_TO_KM
        self.root.ids.output_number.text = str(value)

    def handle_increments(self, change):
        result = self.get_valid_number() + change
        self.root.ids.input_number.text = str(result)
        self.handle_conversion()

    def get_valid_number(self):
        try:
            result = float(self.root.ids.input_number.text)
            return result
        except ValueError:
            return 0


ConvertMilesKm().run()
