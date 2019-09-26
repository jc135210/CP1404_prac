from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.properties import StringProperty


class DynamicWidgetsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.list_of_names = ["Adam", "Lochlan", "Matthew", "nicholas"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_name.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create buttons from dictionary entries and add them to the GUI."""
        for name in self.list_of_names:
            temp_label = Label(text=name)
            self.root.ids.entries_box.add_widget(temp_label)


DynamicWidgetsApp().run()
