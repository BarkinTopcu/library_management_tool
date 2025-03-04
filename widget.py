
import sys
from PySide6.QtWidgets import QApplication, QWidget
#     pyside6-uic form.ui -o ui_form.py
from ui_form import Ui_Widget
import mysql.connector

class Widget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.user_type = None
        self.ui.login_button.clicked.connect(self.on_login_button_click)


    def on_login_button_click(self):
        email = self.ui.login_email_edit.text()
        password = self.ui.login_password_edit.text()
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="admin123",
                database="library"
            )
            cursor = connection.cursor()
            checker = self.ui.staff_check_box.isChecked()
            if checker == True:
                query = "SELECT * FROM staff WHERE staff_email = %s AND staff_password = %s"
            else:
                query = "SELECT * FROM user WHERE email = %s AND user_password = %s"
            cursor.execute(query, (email, password))
            result = cursor.fetchone()

            if result:
                if checker == True:
                    self.user_type ="staff"
                else:
                    self.user_type ="user"
                self.ui.main_menu_widgets.setCurrentWidget(self.ui.main_menu_info)
            else:
                self.ui.login_button.setStyleSheet("background-color: red; color: white;")
                self.ui.login_button.setText("Giriş Başarısız!")

        except mysql.connector.Error as err:
            print("Veritabanı hatası:", err)
        finally:
            if 'cursor' in locals() and cursor is not None:
                cursor.close()
            if 'connection' in locals() and connection is not None:
                connection.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
