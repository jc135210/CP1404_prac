from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    def build(self):
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('miles_to_kilometre.kv')
        return self.root

    def handle_calculate(self):
        value = float(self.root.ids.input_miles.text)
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        value = float(self.root.ids.input_miles.text) + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()


MilesConverterApp().run()