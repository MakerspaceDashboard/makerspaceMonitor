import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    # Main window structuring
        self.set_default_size(600, 250)
        self.set_title("Makerspace Dashboard")

        self.box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL) # Holds everything else
        self.box_title = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box_in = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box_out = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        self.set_child(self.box_main)

        self.box_main.append(self.box_title)
        self.box_main.append(self.box_in)  
        self.box_main.append(self.box_out)
        
    # Main title 
        title_label = Gtk.Label(label="Welcome to Bolz Makerspace!")
        self.box_title.append(title_label)

    # Buttons for check in and out
        self.button_in = Gtk.Button(label="Check In")
        self.button_in.connect('clicked', self.check_in)
        self.box_in.append(self.button_in)

        self.button_out = Gtk.Button(label="Check Out")
        self.button_out.connect('clicked', self.check_out)
        self.box_out.append(self.button_out)

    # Activate check in window on click
    def check_in(self, button):
        print("Check in stuff here")

    # Activate check out window on click
    def check_out(self, button):
        print("Check out stuff here")



class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

app = MyApp(application_id="com.example.GtkApplication")
app.run(sys.argv)