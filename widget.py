# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.main_menu_button.clicked.connect(self.on_main_menu_button_click)

        self.button_clicked = True

    def on_main_menu_button_click(self):
        if self.button_clicked:
            self.ui.main_menu_button.setText('Clicked!')
            self.ui.main_menu_button.setStyleSheet("background-color: green; color: white;")
            self.button_clicked = False
        else:
            self.ui.main_menu_button.setText('Back!')
            self.ui.main_menu_button.setStyleSheet("background-color: white; color: black;")
            self.button_clicked = True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
