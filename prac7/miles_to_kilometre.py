from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    output_message = StringProperty()

    def build(self):
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('miles_to_kilometre.kv')
        return self.root

    def handle_calculate(self, text):
        value = self.validate_value(text)
        # result = value * MILES_TO_KM
        # self.root.ids.output_label.text = str(result)
        self.update(value)

    def handle_increment(self, text, change):
        value = self.validate_value(text) + change
        self.root.ids.input_miles.text = str(value)
        # self.handle_calculate()

    def update(self, value):
        self.output_message = str(value * MILES_TO_KM)

    @staticmethod
    def validate_value(text):
        try:
            value = float(text)
            return value
        except ValueError:
            return 0.0


MilesConverterApp().run()
