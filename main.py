import sys
import gi
import datetime
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gdk, GLib

css_provider = Gtk.CssProvider()
css_provider.load_from_path('style.css')
Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)



class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    # Main window structuring
        self.set_default_size(600, 250)
        self.set_title("Makerspace Dashboard")

        self.box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0) # Holds everything else
        self.box_title = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box_datetime = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box_date = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.box_time = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.box_in = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box_out = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        self.set_child(self.box_main)

        self.box_main.append(self.box_title)
        self.box_main.set_halign(Gtk.Align.CENTER)
        self.box_main.append(self.box_datetime)
        self.box_main.append(self.box_in)
        self.box_in.set_halign(Gtk.Align.CENTER)
        self.box_main.append(self.box_out)
        self.box_out.set_halign(Gtk.Align.CENTER)

    # Main title 
        title_label = Gtk.Label(label="Welcome to Bolz Makerspace!")
        title_label.set_css_classes(['title'])
        self.box_title.append(title_label)

        self.box_datetime.append(self.box_date)
        self.box_datetime.append(self.box_time)

    # Date
        current_date = datetime.datetime.now()
        self.date_label = Gtk.Label(label=current_date)
        GLib.timeout_add(1000, self.update_date)
        self.date_label.set_css_classes(['date'])
        self.date_label.set_halign(Gtk.Align.CENTER)
        self.box_date.append(self.date_label)

        self.update_date()

    # Time
        current_time = datetime.datetime.now()
        self.time_label = Gtk.Label(label=current_time)
        GLib.timeout_add(1000, self.update_time)
        self.time_label.set_css_classes(['date'])
        self.box_time.append(self.time_label)

        # Initialize time display
        self.update_time()


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

    def update_date(self):
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        self.date_label.set_label(current_date)
        return True
    # Function to update the time label
    def update_time(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.time_label.set_label(current_time)
        return True



class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

app = MyApp(application_id="com.example.GtkApplication")
app.run(sys.argv)