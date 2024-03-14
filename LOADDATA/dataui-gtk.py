import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject

class QnAEditor(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="QnA")
        self.set_default_size(400, 230)
        self.set_border_width(10)

        self.layout = Gtk.Grid()
        self.add(self.layout)

        self.label = Gtk.Label(label="Enter Question and Answer:")
        self.layout.attach(self.label, 0, 0, 2, 1)

        self.question_label = Gtk.Label(label="Question:")
        self.layout.attach(self.question_label, 0, 1, 1, 1)

        self.question_entry = Gtk.Entry()
        self.layout.attach(self.question_entry, 1, 1, 1, 1)

        self.answer_label = Gtk.Label(label="Answer:")
        self.layout.attach(self.answer_label, 0, 2, 1, 1)

        self.answer_entry = Gtk.Entry()
        self.layout.attach(self.answer_entry, 1, 2, 1, 1)

        self.format_label = Gtk.Label(label="Answer Format: result")
        self.layout.attach(self.format_label, 0, 3, 2, 1)

        self.save_button = Gtk.Button(label="Save")
        self.layout.attach(self.save_button, 0, 4, 2, 1)
        self.save_button.connect("clicked", self.save_data)

    def save_data(self, button):
        question = self.question_entry.get_text()
        answer = self.answer_entry.get_text()

        if not question or not answer:
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR, Gtk.ButtonsType.OK, "Error")
            dialog.format_secondary_text("Please enter both question and answer.")
            dialog.run()
            dialog.destroy()
            return

        try:
            result = int(answer)
            formatted_data = f"{question}==={result}===5===1\n"
            with open("loaddata.txt", "a") as file:
                file.write(formatted_data)
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Success")
            dialog.format_secondary_text("Question and answer saved successfully.")
            dialog.run()
            dialog.destroy()
        except Exception as e:
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR, Gtk.ButtonsType.OK, "Error")
            dialog.format_secondary_text(f"Invalid input format: {e}")
            dialog.run()
            dialog.destroy()

def main():
    win = QnAEditor()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()
