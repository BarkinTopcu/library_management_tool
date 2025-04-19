
import sys
from PySide6.QtWidgets import QApplication, QWidget,QTableWidgetItem
#     pyside6-uic form.ui -o ui_form.py
from ui_form import Ui_Widget
import mysql.connector
from datetime import datetime
class Widget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        #Main Page Variables
        self.user_type = None
        self.user_ID = None
        self.first_name = None
        self.last_name = None
        self.phone = None
        self.email = None
        self.reg = None
        self.membership = None

        #Mysql and initfunctions
        self.connection = None
        self.mysql_cursor = None
        self.mysql_connect()
        self.initfunctions()
    
    def initfunctions(self):
        #Visible / Unvisible
        self.ui.books_menu_button.hide()
        self.ui.loans_menu_button.hide()
        self.ui.staff_button.hide()
        self.ui.main_menu_widgets.setCurrentWidget(self.ui.main_menu_log_in)

        #Button connections
        self.ui.login_button.clicked.connect(self.on_login_button_click)
        self.ui.signup_button.clicked.connect(self.on_signup_button_click)
        self.ui.main_menu_back_button.clicked.connect(self.go_back_login_button)
        self.ui.go_signup_button.clicked.connect(self.go_signup_button)
        self.ui.books_menu_button.clicked.connect(self.go_books_menu)
        self.ui.loans_menu_button.clicked.connect(self.go_loans_menu)
        self.ui.main_menu_button.clicked.connect(self.go_main_menu)
        self.ui.staff_button.clicked.connect(self.go_staff_menu)

        self.ui.search_button_books.clicked.connect(self.search_books)
        self.ui.filter_button_books.clicked.connect(self.filter_books)
        self.ui.create_loan_button.clicked.connect(self.loan_create)
        self.ui.remove_loan_button.clicked.connect(self.loan_remove)
        self.ui.show_all_loans_button.clicked.connect(self.loan_table)
        self.ui.show_staff_loans.clicked.connect(self.loan_table_staff)
        self.ui.loan_edit_button.clicked.connect(self.loan_edit)
        


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
            print("Database error:", err)
    

    '''
    Generaly these below functions are for GUI configiration and connection of buttons
    '''
    def go_books_menu(self):
        self.ui.main_widget.setCurrentWidget(self.ui.books_widget)

    def go_main_menu(self):
        self.ui.main_widget.setCurrentWidget(self.ui.main_menu_widget)
    
    def go_loans_menu(self):
        self.ui.main_widget.setCurrentWidget(self.ui.loans_widget_users)

    def go_staff_menu(self):
        self.ui.main_widget.setCurrentWidget(self.ui.staff_menu_widget)


    #Button function that goes to signup of mainmenu
    def go_signup_button(self):
        self.ui.main_menu_widgets.setCurrentWidget(self.ui.main_menu_sign_up)

    #Button function that allow users to go to login page from sign up page
    def go_back_login_button(self):
        self.ui.main_menu_widgets.setCurrentWidget(self.ui.main_menu_log_in)

    

    '''
    Functionality of GUI functions
    '''
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
    
    # A function that search for books
    def search_books(self, filter_query):
        book_name = self.ui.books_title_edit.text()
        author_name = self.ui.books_author_edit.text()
        print(book_name)
        print(author_name)
        query = """
        SELECT b.title, b.book_ID, a.author_name, a.author_last_name, b.year, b.category
        FROM book b
        JOIN author a ON b.author_ID = a.author_ID
        WHERE 1=1
        """
        params = []
        # Add book name to query
        if book_name != "":
            query += " AND b.title LIKE %s"
            params.append(f"%{book_name}%")

        # Add author name to query
        if author_name != "":
            query += " AND a.author_name LIKE %s"
            params.append(f"%{author_name}%")
        
        # Add filters to query

        if filter_query != "" and filter_query != False:
            query += filter_query

        self.mysql_cursor.execute(query, params)
        books = self.mysql_cursor.fetchall()
        self.populate_table(books)
        


    # A function that update the table books
    def populate_table(self, books):
        table = self.ui.books_table
        table.setRowCount(len(books))
        table.setColumnCount(6) 
        table.setHorizontalHeaderLabels(["Title", "Book ID", "Author Name", "Last Name", "Year", "Category"])
        for row_idx, row_data in enumerate(books):
            for col_idx, cell_data in enumerate(row_data):
                table.setItem(row_idx, col_idx, QTableWidgetItem(str(cell_data)))
        table.resizeColumnsToContents()

    def filter_books(self):

        #A dictionary that used for checking the categories.
        category_dict = {
            "Romance":False,
            "Horror":False,
            "Fantasy":False,
            "Travel":False,
            "Short Story":False,
            "History":False,
            "Science Fiction":False,
            "Adventure":False
        }

        #Each category is checking
        category_dict["Romance"] = self.ui.romance_box_books.isChecked()
        category_dict["Horror"] = self.ui.horror_box_books.isChecked()
        category_dict["Fantasy"] = self.ui.fantasy_box_books.isChecked()
        category_dict["Travel"] = self.ui.tralve_box_books.isChecked()
        category_dict["Short Story"] = self.ui.short_story_box_books.isChecked()
        category_dict["History"] = self.ui.history_box_books.isChecked()
        category_dict["Science Fiction"] = self.ui.science_box_books.isChecked()
        category_dict["Adventure"] = self.ui.adventure_box_books.isChecked()



        filter_query = ""
        first_filter = 0

        #Adding selected filters to query
        for key, value in category_dict.items():
            if value == True:
                if first_filter == 0:
                    filter_query += f" AND (b.category LIKE '{key}'"
                    first_filter = 1
                else:
                    filter_query += f" OR b.category LIKE '{key}'"
        
        if first_filter == 1:
            filter_query += ")"

        #Adding date info to query
        first_date = self.ui.first_date_year.date().year()
        second_date = self.ui.second_date_year.date().year()
        filter_query += f" AND b.year >= {first_date}"
        filter_query += f" AND b.year <= {second_date}"
        
        self.search_books(filter_query)

    def loan_create(self):
        book_ID = self.ui.loans_book_ID_edit.text()
        user_ID = self.user_ID
        loan_date = datetime.now()
        status = "Waiting"
        query = """
        INSERT INTO loan (book_ID, user_ID, loan_date,status_state)
        VALUES (%s, %s, %s, %s)
        """
        values =(book_ID,user_ID,loan_date,status)
        self.mysql_cursor.execute(query, values)
        self.connection.commit()

    def loan_remove(self):
        loan_ID = self.ui.loans_loan_ID_edit.text()
        query = """
        SELECT 1 FROM loan
        WHERE %s = user_ID AND status_state = 'Waiting' AND %s = loan_ID
        """
        values =(self.user_ID,loan_ID)
        self.mysql_cursor.execute(query, values)
        result = self.mysql_cursor.fetchall()

        if result:
            query = """
            DELETE FROM loan WHERE loan_ID = %s
            """
            values =(loan_ID,)
            self.mysql_cursor.execute(query, values)
            self.connection.commit()

    def loan_table(self):
        query = """
        SELECT l.loan_ID, l.book_ID, b.title,loan_date, l.status_state FROM loan l
        LEFT JOIN book b ON b.book_ID = l.book_ID
        WHERE %s = l.user_ID 
        """
        values =(self.user_ID,)
        self.mysql_cursor.execute(query, values)
        result = self.mysql_cursor.fetchall()

        table = self.ui.user_loans_table
        
        table.setRowCount(len(result))
        table.setColumnCount(5) 
        table.setHorizontalHeaderLabels(["Loan ID", "Book ID", "Title","Loan Date", "Status"])

        column_widths = [100, 100, 220, 120, 100]

        for col_idx, width in enumerate(column_widths):
            table.setColumnWidth(col_idx, width)
            
        for row_idx, row_data in enumerate(result):
            for col_idx, cell_data in enumerate(row_data):
                table.setItem(row_idx, col_idx, QTableWidgetItem(str(cell_data)))

    def loan_edit(self):
        query = """
                UPDATE loan SET status_state =%s WHERE loan_ID = %s
"""
        loan_ID = self.ui.staff_loan_ID.text()
        status = self.ui.staff_loan_status.text()

        values =(status,loan_ID)
        self.mysql_cursor.execute(query, values)
        self.connection.commit()

    def loan_table_staff(self):
        query = """
        SELECT l.loan_ID, l.book_ID, b.title,loan_date, l.user_ID,l.status_state,l.staff_ID,l.return_date FROM loan l
        LEFT JOIN book b ON b.book_ID = l.book_ID
        """
        self.mysql_cursor.execute(query)
        result = self.mysql_cursor.fetchall()

        table = self.ui.staff_loan_table
        
        table.setRowCount(len(result))
        table.setColumnCount(8) 
        table.setHorizontalHeaderLabels(["Loan ID", "Book ID", "Title","Loan Date", "User ID","Status","Staff ID","Return Date"])

            
        for row_idx, row_data in enumerate(result):
            for col_idx, cell_data in enumerate(row_data):
                table.setItem(row_idx, col_idx, QTableWidgetItem(str(cell_data)))
        table.resizeColumnsToContents()



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
                    self.ui.staff_button.show()
                else:
                    self.user_type ="user"
                    self.user_ID, self.first_name, self.last_name, self.phone, self.email, self.reg, self.membership, *others = result
                self.ui.info_first_name_label.setText(self.first_name)
                self.ui.info_last_name_label.setText(self.last_name)
                self.ui.info_membership_label.setText(self.membership)
                self.ui.info_phone_label.setText(self.phone)
                self.ui.info_regis_date_label.setText(str(self.reg))
                self.ui.info_email_label.setText(self.email)
                self.ui.books_menu_button.show()
                self.ui.loans_menu_button.show()
            else:
                self.ui.login_button.setStyleSheet("background-color: red; color: white;")
                self.ui.login_button.setText("Login Unsuccessfull!")

        except mysql.connector.Error as err:
            print("Database Error:", err)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    
    widget.show()
    sys.exit(app.exec())
