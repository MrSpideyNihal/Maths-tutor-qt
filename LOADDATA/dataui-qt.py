import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt

class QnAEditor(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QnA Editor")
        self.setGeometry(100, 100, 400, 230)
        self.setStyleSheet("background-color: #f0f0f0;")

        self.label = QLabel("Enter Question and Answer:", self)
        self.label.move(20, 20)
        self.label.setStyleSheet("font-size: 16px;")

        self.question_label = QLabel("Question:", self)
        self.question_label.move(20, 50)
        self.question_label.setStyleSheet("font-size: 14px; color: #333;")

        self.question_entry = QLineEdit(self)
        self.question_entry.setGeometry(100, 50, 250, 20)

        self.answer_label = QLabel("Answer:", self)
        self.answer_label.move(20, 80)
        self.answer_label.setStyleSheet("font-size: 14px; color: #333;")

        self.answer_entry = QLineEdit(self)
        self.answer_entry.setGeometry(100, 80, 250, 20)

        self.format_label = QLabel("Answer Format: result", self)
        self.format_label.setGeometry(20, 110, 350, 20)
        self.format_label.setStyleSheet("font-size: 12px; color: #888;")

        self.save_button = QPushButton("Save", self)
        self.save_button.setGeometry(150, 150, 100, 30)
        self.save_button.setStyleSheet("background-color: #4CAF50; color: white; border-radius: 5px;")
        self.save_button.clicked.connect(self.save_data)

    def save_data(self):
        question = self.question_entry.text()
        answer = self.answer_entry.text()

        if not question or not answer:
            QMessageBox.critical(self, "Error", "Please enter both question and answer.")
            return

        try:
            result = int(answer)
            formatted_data = f"{question}==={result}===5===1\n"
            with open("load_data.txt", "a") as file:
                file.write(formatted_data)
            QMessageBox.information(self, "Success", "Question and answer saved successfully.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Invalid input format: {e}")

def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")  # Use Fusion style
    editor = QnAEditor()
    editor.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
