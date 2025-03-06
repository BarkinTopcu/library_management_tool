
import sys
from PySide6.QtWidgets import QApplication, QWidget
#     pyside6-uic form.ui -o ui_form.py
from ui_form import Ui_Widget
import mysql.connector
import datetime
class Widget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.user_type = None
        self.user_ID = None
        self.first_name = None
        self.last_name = None
        self.phone = None
        self.email = None
        self.reg = None
        self.membership = None
        self.ui.login_button.clicked.connect(self.on_login_button_click)
        self.ui.signup_button.clicked.connect(self.on_signup_button_click)
        self.ui.main_menu_back_button.clicked.connect(self.go_back_login_button)
        self.ui.go_signup_button.clicked.connect(self.go_signup_button)
        self.connection = None
        self.mysql_cursor = None
        self.mysql_connect()

    #SQL connect
    def mysql_connect(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="admin123",
                database="library"
            )
            self.mysql_cursor = self.connection.cursor()
        except mysql.connector.Error as err:
            print("Veritabanı hatası:", err)
    #Button function that goes to signup of mainmenu
    def go_signup_button(self):
        self.ui.main_menu_widgets.setCurrentWidget(self.ui.main_menu_sign_up)
    #Button function that allow users to go to login page from sign up page
    def go_back_login_button(self):
        self.ui.main_menu_widgets.setCurrentWidget(self.ui.main_menu_log_in)
    #Function that sign up to user to database
    def on_signup_button_click(self):
        first_name = self.ui.signup_first_name_edit.text()
        last_name = self.ui.signup_last_name_edit.text()
        email = self.ui.signup_email_edit.text()
        password = self.ui.signup_password_edit.text()
        phone = self.ui.signup_phone_edit.text()
        registraion_date = datetime.date.today()
        membership = "Normal"
        query = """
        INSERT INTO user (first_name,last_name,email,user_password,phone_number,registration_date,membership_type)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
"""
        values = (first_name, last_name, email, password,phone,registraion_date,membership)
        self.mysql_cursor.execute(query,values)
        self.connection.commit()
    #Function that log in the user of staff to application with checking database
    def on_login_button_click(self):
        email = self.ui.login_email_edit.text()
        password = self.ui.login_password_edit.text()
        try:
            checker = self.ui.staff_check_box.isChecked()
            if checker == True:
                query = "SELECT * FROM staff WHERE staff_email = %s AND staff_password = %s"
            else:
                query = "SELECT * FROM user WHERE email = %s AND user_password = %s"
            self.mysql_cursor.execute(query, (email, password))
            result = self.mysql_cursor.fetchone()

            if result:
                self.ui.main_menu_widgets.setCurrentWidget(self.ui.main_menu_info)
                if checker == True:
                    self.user_type ="staff"
                    self.user_ID, self.first_name, self.last_name, self.email, *others = result
                else:
                    self.user_type ="user"
                    self.user_ID, self.first_name, self.last_name, self.phone, self.email, self.reg, self.membership, *others = result
                self.ui.info_first_name_label.setText(self.first_name)
                self.ui.info_last_name_label.setText(self.last_name)
                self.ui.info_membership_label.setText(self.membership)
                self.ui.info_phone_label.setText(self.phone)
                self.ui.info_regis_date_label.setText(str(self.reg))
                self.ui.info_email_label.setText(self.email)
            else:
                self.ui.login_button.setStyleSheet("background-color: red; color: white;")
                self.ui.login_button.setText("Giriş Başarısız!")

        except mysql.connector.Error as err:
            print("Veritabanı hatası:", err)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    
    widget.show()
    sys.exit(app.exec())
