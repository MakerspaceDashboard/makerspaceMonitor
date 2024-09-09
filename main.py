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
        self.set_default_size(768, 480)
        self.set_title("Makerspace Dashboard")

    # Home screen
        self.box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0) # Holds everything else
        self.box_main.set_css_classes(['mainbox'])
        self.box_title = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box_datetime = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box_date = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.box_time = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.box_in = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box_out = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

    # Staff box
        self.box_present = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box_present.set_css_classes(['staff'])
        self.box_present.set_halign(Gtk.Align.END)
        self.staff_present = Gtk.ListBox()
        self.staff_list_label = Gtk.Label(label=" Staff Present ")
        self.staff_present.set_css_classes(['staff'])
        self.staff_present.append(self.staff_list_label)
        self.box_present.append(self.staff_present)



    # Moving pages
        self.box_back = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.button_back = Gtk.Button(label="<-")
        self.button_back.connect('clicked', self.go_back)
        self.box_back.set_css_classes(['arrows'])
        self.box_back.set_halign(Gtk.Align.START)
        self.box_back.append(self.button_back)

    # Check in page
        self.box_login = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box_user = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.box_password = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.box_login.set_halign(Gtk.Align.CENTER)
        self.box_login.append(self.box_user)
        self.box_login.append(self.box_password)

    # Initialize
        self.box_main.set_css_classes(['mainbox'])
        self.set_child(self.box_main)

    # Main title
        self.box_main.append(self.box_title)
        self.box_main.set_halign(Gtk.Align.CENTER)
        self.box_main.append(self.box_present)
        self.box_main.append(self.box_datetime)
        self.box_datetime.set_halign(Gtk.Align.CENTER)
        self.box_main.append(self.box_in)
        self.box_in.set_halign(Gtk.Align.CENTER)
        self.box_main.append(self.box_out)
        self.box_out.set_halign(Gtk.Align.CENTER)
 
        title_label = Gtk.Label(label="Welcome to Bolz Makerspace!")
        title_label.set_css_classes(['welcome'])
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

        self.update_time()


    # Buttons for check in and out
        self.button_in = Gtk.Button(label="Check In")
        self.button_in.connect('clicked', self.check_in)
        self.box_in.set_css_classes(['check'])
        self.box_in.append(self.button_in)

        self.button_out = Gtk.Button(label="Check Out")
        self.button_out.connect('clicked', self.check_out)
        self.box_out.set_css_classes(['check'])
        self.box_out.append(self.button_out)

    # User and password boxes for next page
        user_label = Gtk.Label(label="Username:")
        self.username = Gtk.Entry()
        self.box_user.append(user_label)
        self.box_user.append(self.username)

        pass_label = Gtk.Label(label="Password:")
        self.password = Gtk.Entry()
        self.password.set_visibility(False)
        self.box_password.append(pass_label)
        self.box_password.append(self.password)

        self.box_login.append(self.box_back)

    # Activate check in window on click
    def check_in(self, button):
        print("Check in stuff here")
        self.set_child(self.box_login)

    def go_back(self, button): 
        print("Back to main")
        self.set_child(self.box_main)

    # Activate check out window on click
    def check_out(self, button):
        print("Check out stuff here")
        # Work needed here

    # Update date label
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