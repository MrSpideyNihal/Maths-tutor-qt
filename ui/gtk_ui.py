import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GObject, GLib, Pango

class MathsTutorWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Maths-Tutor")
        self.set_border_width(10)
        self.connect("destroy", Gtk.main_quit)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        vbox.pack_start(vbox2, True, True, 0)

        self.welcome_message = "Welcome to maths tutor!\nPress enter to start "
        self.label = Gtk.Label()
        self.label.set_text(self.welcome_message)
        vbox2.modify_font(Pango.FontDescription("Sans 40"))
        font_color = "#0603f0"
        background_color = "#ffffff"
        vbox2.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse(font_color))
        vbox2.modify_bg(Gtk.StateFlags.NORMAL, Gdk.color_parse(background_color))
        vbox2.pack_start(self.label, True, True, 0)

        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        fix1 = Gtk.Fixed()
        hbox.pack_start(fix1, True, True, 0)
        self.entry = Gtk.Entry()
        self.entry.connect("activate", self.on_entry_activated)
        hbox.pack_start(self.entry, False, False, 0)
        fix2 = Gtk.Fixed()
        hbox.pack_start(fix2, True, True, 0)
        vbox2.pack_start(hbox, False, False, 0)

        self.data_directory = "/usr/share/maths-tutor"
        self.image = Gtk.Image()
        self.set_image("welcome", 3)
        vbox2.pack_start(self.image, True, True, 0)

        hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        user_guide_button = Gtk.Button(label="User-Guide")
        user_guide_button.set_size_request(1, 1)
        hbox2.pack_start(user_guide_button, True, True, 0)

        Load_Questions_button = Gtk.Button(label="Load Questions")
        Load_Questions_button.connect("clicked", self.on_Load_Questions_clicked)
        Load_Questions_button.set_size_request(1, 1)
        hbox2.pack_start(Load_Questions_button, True, True, 0)

        about_button = Gtk.Button(label="About")
        about_button.connect("clicked", self.show_about_dialog)
        about_button.set_size_request(1, 1)
        hbox2.pack_start(about_button, True, True, 0)

        Close_button = Gtk.Button(label="Quit")
        Close_button.connect("clicked", self.window_close)
        hbox2.pack_start(Close_button, True, True, 0)

        vbox.pack_start(hbox2, False, True, 0)

        self.set_default_size(500, 700)
        self.show_all()

    def on_entry_activated(self, entry):
        pass

    def set_image(self, name, rand_range):
        pass

    def on_Load_Questions_clicked(self, widget):
        pass

    def window_close(self, button):
        self.destroy()
    def show_about_dialog(self, button):
        about_dialog = Gtk.AboutDialog()
        # Set the relevant properties of the about dialog
        about_dialog.set_program_name("MATHS TUTOR GAME\n 0.1 \n\nMATHS TUTOR is a game to develop students calculation ability in maths and to judge themselves.\n Which is helpful to the students who have basic knowledge in maths. \n They  want to answer the questions they got and can lead into progress if they can answer the questions correctly.  \n\n   Copyright(C) 2022-2023 ROOPASREE A P <roopasreeap@gmail.com>\n\n   Supervised by  Zendalona(2022-2023)\n\n This program is free software you can redistribute it and or modify \nit under the terms of GNU General Public License as published by the free software foundation \n either gpl3 of the license.This program is distributed in the hope that it will be useful,\n but without any warranty without even the implied warranty of merchantability or fitness for a particular purpose.\n see the GNU General Public License for more details")
        about_dialog.set_website_label("GNU General Public License,version 0.1\n\n" "Visit MATHS TUTOR Home page")
        about_dialog.set_website("http://wwww,zendalona.com/maths-tutor")
        about_dialog.set_authors(["Roopasree A P"])
        about_dialog.set_documenters(["Roopasree A P"])
        about_dialog.set_artists(["Nalin Sathyan", "Dr.Saritha Namboodiri", "Subha I N", "Bhavya P V", "K.Sathyaseelan"])
        
        about_dialog.run()
        about_dialog.destroy()

if __name__ == "__main__":
    win = MathsTutorWindow()
    Gtk.main()
