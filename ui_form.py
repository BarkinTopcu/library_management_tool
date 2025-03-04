# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1073, 681)
        Widget.setStyleSheet(u"background:black;")
        self.horizontalLayout = QHBoxLayout(Widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.menu_widget = QWidget(Widget)
        self.menu_widget.setObjectName(u"menu_widget")
        self.menu_widget.setMinimumSize(QSize(135, 200))
        self.menu_widget.setMaximumSize(QSize(999999, 16777215))
        self.menu_widget.setStyleSheet(u"background: rgb(71, 153, 174);")
        self.verticalLayout = QVBoxLayout(self.menu_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main_menu_button = QPushButton(self.menu_widget)
        self.main_menu_button.setObjectName(u"main_menu_button")
        self.main_menu_button.setStyleSheet(u"background: white;")

        self.verticalLayout.addWidget(self.main_menu_button)

        self.books_menu_button = QPushButton(self.menu_widget)
        self.books_menu_button.setObjectName(u"books_menu_button")
        self.books_menu_button.setStyleSheet(u"background: white;")

        self.verticalLayout.addWidget(self.books_menu_button)

        self.loans_menu_button = QPushButton(self.menu_widget)
        self.loans_menu_button.setObjectName(u"loans_menu_button")
        self.loans_menu_button.setStyleSheet(u"background: white;")

        self.verticalLayout.addWidget(self.loans_menu_button)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.menu_widget)

        self.stackedWidget = QStackedWidget(Widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background:black;")
        self.loans_widget_users = QWidget()
        self.loans_widget_users.setObjectName(u"loans_widget_users")
        self.verticalLayout_6 = QVBoxLayout(self.loans_widget_users)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.loans_widget_users)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 125))
        self.frame.setStyleSheet(u"background:white;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 0, 221, 121))
        self.groupBox.setStyleSheet(u"background:white;")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 35, 49, 16))
        self.loans_book_ID_edit = QLineEdit(self.groupBox)
        self.loans_book_ID_edit.setObjectName(u"loans_book_ID_edit")
        self.loans_book_ID_edit.setGeometry(QRect(80, 30, 113, 22))
        self.create_loan_button = QPushButton(self.groupBox)
        self.create_loan_button.setObjectName(u"create_loan_button")
        self.create_loan_button.setGeometry(QRect(80, 70, 75, 24))
        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(240, 0, 221, 121))
        self.groupBox_2.setStyleSheet(u"background:white;")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 35, 49, 16))
        self.loans_loan_ID_edit = QLineEdit(self.groupBox_2)
        self.loans_loan_ID_edit.setObjectName(u"loans_loan_ID_edit")
        self.loans_loan_ID_edit.setGeometry(QRect(80, 30, 113, 22))
        self.remove_loan_button = QPushButton(self.groupBox_2)
        self.remove_loan_button.setObjectName(u"remove_loan_button")
        self.remove_loan_button.setGeometry(QRect(80, 70, 75, 24))
        self.groupBox_3 = QGroupBox(self.frame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(470, 0, 221, 121))
        self.groupBox_3.setStyleSheet(u"background:white;")
        self.show_all_loans_button = QPushButton(self.groupBox_3)
        self.show_all_loans_button.setObjectName(u"show_all_loans_button")
        self.show_all_loans_button.setGeometry(QRect(50, 50, 121, 24))

        self.verticalLayout_6.addWidget(self.frame)

        self.widget = QWidget(self.loans_widget_users)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.user_loans_table = QTableWidget(self.widget)
        self.user_loans_table.setObjectName(u"user_loans_table")
        self.user_loans_table.setStyleSheet(u"background:#FFEEE4;")

        self.horizontalLayout_4.addWidget(self.user_loans_table)


        self.verticalLayout_6.addWidget(self.widget)

        self.stackedWidget.addWidget(self.loans_widget_users)
        self.main_menu_widget = QWidget()
        self.main_menu_widget.setObjectName(u"main_menu_widget")
        self.main_menu_widget.setStyleSheet(u"background:gray;")
        self.verticalLayout_7 = QVBoxLayout(self.main_menu_widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_2 = QWidget(self.main_menu_widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background:#58C9B9;")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_2 = QSpacerItem(254, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 53, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(254, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 54, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 2, 1, 1, 1)

        self.main_menu_widgets = QStackedWidget(self.widget_2)
        self.main_menu_widgets.setObjectName(u"main_menu_widgets")
        self.main_menu_widgets.setMinimumSize(QSize(350, 400))
        self.main_menu_widgets.setStyleSheet(u"background:#FFEEE4;")
        self.main_menu_info = QWidget()
        self.main_menu_info.setObjectName(u"main_menu_info")
        self.widget_3 = QWidget(self.main_menu_info)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(10, 10, 331, 381))
        self.widget_3.setStyleSheet(u"background:white;")
        self.label_10 = QLabel(self.widget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(40, 60, 121, 41))
        font = QFont()
        font.setFamilies([u"Microsoft Sans Serif"])
        font.setPointSize(12)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_11 = QLabel(self.widget_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(40, 100, 121, 41))
        self.label_11.setFont(font)
        self.label_12 = QLabel(self.widget_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(40, 140, 141, 41))
        self.label_12.setFont(font)
        self.label_13 = QLabel(self.widget_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(40, 180, 201, 41))
        self.label_13.setFont(font)
        self.label_14 = QLabel(self.widget_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(130, 10, 71, 51))
        font1 = QFont()
        font1.setFamilies([u"Microsoft Sans Serif"])
        font1.setPointSize(30)
        font1.setBold(True)
        self.label_14.setFont(font1)
        self.label_15 = QLabel(self.widget_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(40, 220, 201, 41))
        self.label_15.setFont(font)
        self.label_16 = QLabel(self.widget_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(40, 250, 201, 41))
        self.label_16.setFont(font)
        self.info_first_name_label = QLabel(self.widget_3)
        self.info_first_name_label.setObjectName(u"info_first_name_label")
        self.info_first_name_label.setGeometry(QRect(150, 73, 121, 16))
        self.info_last_name_label = QLabel(self.widget_3)
        self.info_last_name_label.setObjectName(u"info_last_name_label")
        self.info_last_name_label.setGeometry(QRect(150, 113, 121, 16))
        self.info_membership_label = QLabel(self.widget_3)
        self.info_membership_label.setObjectName(u"info_membership_label")
        self.info_membership_label.setGeometry(QRect(160, 153, 121, 16))
        self.info_regis_date_label = QLabel(self.widget_3)
        self.info_regis_date_label.setObjectName(u"info_regis_date_label")
        self.info_regis_date_label.setGeometry(QRect(200, 193, 121, 16))
        self.info_phone_label = QLabel(self.widget_3)
        self.info_phone_label.setObjectName(u"info_phone_label")
        self.info_phone_label.setGeometry(QRect(110, 233, 121, 16))
        self.info_email_label = QLabel(self.widget_3)
        self.info_email_label.setObjectName(u"info_email_label")
        self.info_email_label.setGeometry(QRect(110, 263, 121, 16))
        self.main_menu_widgets.addWidget(self.main_menu_info)
        self.main_menu_log_in = QWidget()
        self.main_menu_log_in.setObjectName(u"main_menu_log_in")
        self.label_7 = QLabel(self.main_menu_log_in)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(120, 60, 121, 51))
        self.label_7.setFont(font1)
        self.login_email_edit = QLineEdit(self.main_menu_log_in)
        self.login_email_edit.setObjectName(u"login_email_edit")
        self.login_email_edit.setGeometry(QRect(100, 140, 151, 41))
        font2 = QFont()
        font2.setItalic(False)
        self.login_email_edit.setFont(font2)
        self.login_email_edit.setStyleSheet(u"background-color:white;\n"
"border:none;\n"
"border-bottom:2px solid black;\n"
"color:rgb(164, 202, 222);\n"
"padding-bottom:7px;\n"
"")
        self.login_password_edit = QLineEdit(self.main_menu_log_in)
        self.login_password_edit.setObjectName(u"login_password_edit")
        self.login_password_edit.setGeometry(QRect(100, 210, 151, 41))
        self.login_password_edit.setStyleSheet(u"background-color:white;\n"
"border:none;\n"
"border-bottom:2px solid black;\n"
"color:rgb(164, 202, 222);\n"
"padding-bottom:7px;\n"
"")
        self.login_password_edit.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton(self.main_menu_log_in)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(140, 280, 75, 24))
        self.label_8 = QLabel(self.main_menu_log_in)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(50, 140, 41, 41))
        self.label_8.setStyleSheet(u"")
        self.go_signup_button = QPushButton(self.main_menu_log_in)
        self.go_signup_button.setObjectName(u"go_signup_button")
        self.go_signup_button.setGeometry(QRect(140, 320, 75, 24))
        self.staff_check_box = QCheckBox(self.main_menu_log_in)
        self.staff_check_box.setObjectName(u"staff_check_box")
        self.staff_check_box.setGeometry(QRect(150, 260, 51, 20))
        self.main_menu_widgets.addWidget(self.main_menu_log_in)
        self.main_menu_sign_up = QWidget()
        self.main_menu_sign_up.setObjectName(u"main_menu_sign_up")
        self.label_9 = QLabel(self.main_menu_sign_up)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(100, 10, 151, 51))
        self.label_9.setFont(font1)
        self.signup_first_name_edit = QLineEdit(self.main_menu_sign_up)
        self.signup_first_name_edit.setObjectName(u"signup_first_name_edit")
        self.signup_first_name_edit.setGeometry(QRect(30, 70, 121, 41))
        self.signup_first_name_edit.setFont(font2)
        self.signup_first_name_edit.setStyleSheet(u"background-color:white;\n"
"border:none;\n"
"border-bottom:2px solid black;\n"
"color:rgb(164, 202, 222);\n"
"padding-bottom:7px;\n"
"")
        self.signup_password_edit = QLineEdit(self.main_menu_sign_up)
        self.signup_password_edit.setObjectName(u"signup_password_edit")
        self.signup_password_edit.setGeometry(QRect(30, 190, 151, 41))
        self.signup_password_edit.setStyleSheet(u"background-color:white;\n"
"border:none;\n"
"border-bottom:2px solid black;\n"
"color:rgb(164, 202, 222);\n"
"padding-bottom:7px;\n"
"")
        self.signup_password_edit.setEchoMode(QLineEdit.Password)
        self.signup_button = QPushButton(self.main_menu_sign_up)
        self.signup_button.setObjectName(u"signup_button")
        self.signup_button.setGeometry(QRect(140, 320, 75, 24))
        self.signup_email_edit = QLineEdit(self.main_menu_sign_up)
        self.signup_email_edit.setObjectName(u"signup_email_edit")
        self.signup_email_edit.setGeometry(QRect(30, 130, 291, 41))
        self.signup_email_edit.setFont(font2)
        self.signup_email_edit.setStyleSheet(u"background-color:white;\n"
"border:none;\n"
"border-bottom:2px solid black;\n"
"color:rgb(164, 202, 222);\n"
"padding-bottom:7px;\n"
"")
        self.main_menu_back_button = QPushButton(self.main_menu_sign_up)
        self.main_menu_back_button.setObjectName(u"main_menu_back_button")
        self.main_menu_back_button.setGeometry(QRect(140, 350, 75, 24))
        self.signup_last_name_edit = QLineEdit(self.main_menu_sign_up)
        self.signup_last_name_edit.setObjectName(u"signup_last_name_edit")
        self.signup_last_name_edit.setGeometry(QRect(200, 70, 121, 41))
        self.signup_last_name_edit.setFont(font2)
        self.signup_last_name_edit.setStyleSheet(u"background-color:white;\n"
"border:none;\n"
"border-bottom:2px solid black;\n"
"color:rgb(164, 202, 222);\n"
"padding-bottom:7px;\n"
"")
        self.signup_phone_edit = QLineEdit(self.main_menu_sign_up)
        self.signup_phone_edit.setObjectName(u"signup_phone_edit")
        self.signup_phone_edit.setGeometry(QRect(30, 250, 121, 41))
        self.signup_phone_edit.setFont(font2)
        self.signup_phone_edit.setStyleSheet(u"background-color:white;\n"
"border:none;\n"
"border-bottom:2px solid black;\n"
"color:rgb(164, 202, 222);\n"
"padding-bottom:7px;\n"
"")
        self.main_menu_widgets.addWidget(self.main_menu_sign_up)

        self.gridLayout.addWidget(self.main_menu_widgets, 1, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.widget_2)

        self.stackedWidget.addWidget(self.main_menu_widget)
        self.books_widget = QWidget()
        self.books_widget.setObjectName(u"books_widget")
        self.books_widget.setStyleSheet(u"background: black;")
        self.verticalLayout_2 = QVBoxLayout(self.books_widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.header_books = QWidget(self.books_widget)
        self.header_books.setObjectName(u"header_books")
        self.header_books.setMinimumSize(QSize(0, 50))
        self.header_books.setStyleSheet(u"background:#58C9B9;")
        self.books_title_edit = QLineEdit(self.header_books)
        self.books_title_edit.setObjectName(u"books_title_edit")
        self.books_title_edit.setGeometry(QRect(100, 10, 113, 22))
        self.books_title_edit.setStyleSheet(u"background:white;")
        self.label_title_books = QLabel(self.header_books)
        self.label_title_books.setObjectName(u"label_title_books")
        self.label_title_books.setGeometry(QRect(30, 13, 71, 16))
        self.search_button_books = QPushButton(self.header_books)
        self.search_button_books.setObjectName(u"search_button_books")
        self.search_button_books.setGeometry(QRect(790, 10, 75, 24))
        self.search_button_books.setStyleSheet(u"background:white;")
        self.books_author_edit = QLineEdit(self.header_books)
        self.books_author_edit.setObjectName(u"books_author_edit")
        self.books_author_edit.setGeometry(QRect(330, 10, 113, 22))
        self.books_author_edit.setStyleSheet(u"background:white;")
        self.label_author_books = QLabel(self.header_books)
        self.label_author_books.setObjectName(u"label_author_books")
        self.label_author_books.setGeometry(QRect(250, 13, 81, 16))

        self.verticalLayout_2.addWidget(self.header_books)

        self.widget_books_search = QWidget(self.books_widget)
        self.widget_books_search.setObjectName(u"widget_books_search")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_books_search)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 1, 0, 0)
        self.widget_books_filter = QWidget(self.widget_books_search)
        self.widget_books_filter.setObjectName(u"widget_books_filter")
        self.widget_books_filter.setMinimumSize(QSize(160, 0))
        self.widget_books_filter.setStyleSheet(u"background:#58C9B9;")
        self.verticalLayout_3 = QVBoxLayout(self.widget_books_filter)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.category_filter_books = QFrame(self.widget_books_filter)
        self.category_filter_books.setObjectName(u"category_filter_books")
        self.category_filter_books.setMinimumSize(QSize(0, 300))
        self.category_filter_books.setStyleSheet(u"background:white;")
        self.category_filter_books.setFrameShape(QFrame.StyledPanel)
        self.category_filter_books.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.category_filter_books)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.category_label_books = QLabel(self.category_filter_books)
        self.category_label_books.setObjectName(u"category_label_books")
        font3 = QFont()
        font3.setPointSize(14)
        self.category_label_books.setFont(font3)
        self.category_label_books.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.category_label_books)

        self.checkBox_all_books = QCheckBox(self.category_filter_books)
        self.checkBox_all_books.setObjectName(u"checkBox_all_books")

        self.verticalLayout_4.addWidget(self.checkBox_all_books)

        self.romance_box_books = QCheckBox(self.category_filter_books)
        self.romance_box_books.setObjectName(u"romance_box_books")

        self.verticalLayout_4.addWidget(self.romance_box_books)

        self.horror_box_books = QCheckBox(self.category_filter_books)
        self.horror_box_books.setObjectName(u"horror_box_books")

        self.verticalLayout_4.addWidget(self.horror_box_books)

        self.fantasy_box_books = QCheckBox(self.category_filter_books)
        self.fantasy_box_books.setObjectName(u"fantasy_box_books")

        self.verticalLayout_4.addWidget(self.fantasy_box_books)

        self.tralve_box_books = QCheckBox(self.category_filter_books)
        self.tralve_box_books.setObjectName(u"tralve_box_books")

        self.verticalLayout_4.addWidget(self.tralve_box_books)

        self.short_story_box_books = QCheckBox(self.category_filter_books)
        self.short_story_box_books.setObjectName(u"short_story_box_books")

        self.verticalLayout_4.addWidget(self.short_story_box_books)

        self.history_box_books = QCheckBox(self.category_filter_books)
        self.history_box_books.setObjectName(u"history_box_books")

        self.verticalLayout_4.addWidget(self.history_box_books)

        self.science_box_books = QCheckBox(self.category_filter_books)
        self.science_box_books.setObjectName(u"science_box_books")

        self.verticalLayout_4.addWidget(self.science_box_books)

        self.adventure_box_books = QCheckBox(self.category_filter_books)
        self.adventure_box_books.setObjectName(u"adventure_box_books")

        self.verticalLayout_4.addWidget(self.adventure_box_books)


        self.verticalLayout_3.addWidget(self.category_filter_books)

        self.year_filter_books = QFrame(self.widget_books_filter)
        self.year_filter_books.setObjectName(u"year_filter_books")
        self.year_filter_books.setStyleSheet(u"background:white;")
        self.year_filter_books.setFrameShape(QFrame.StyledPanel)
        self.year_filter_books.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.year_filter_books)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.year_filter_books)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 20))
        font4 = QFont()
        font4.setPointSize(16)
        self.label_4.setFont(font4)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)

        self.label = QLabel(self.year_filter_books)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label)

        self.first_date_year = QDateEdit(self.year_filter_books)
        self.first_date_year.setObjectName(u"first_date_year")

        self.verticalLayout_5.addWidget(self.first_date_year)

        self.second_date_year = QDateEdit(self.year_filter_books)
        self.second_date_year.setObjectName(u"second_date_year")

        self.verticalLayout_5.addWidget(self.second_date_year)


        self.verticalLayout_3.addWidget(self.year_filter_books)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.filter_button_books = QPushButton(self.widget_books_filter)
        self.filter_button_books.setObjectName(u"filter_button_books")
        self.filter_button_books.setStyleSheet(u"background:white;")

        self.verticalLayout_3.addWidget(self.filter_button_books)


        self.horizontalLayout_3.addWidget(self.widget_books_filter)

        self.books_table = QTableWidget(self.widget_books_search)
        self.books_table.setObjectName(u"books_table")
        self.books_table.setStyleSheet(u"background:#FFEEE4;")

        self.horizontalLayout_3.addWidget(self.books_table)


        self.verticalLayout_2.addWidget(self.widget_books_search)

        self.stackedWidget.addWidget(self.books_widget)

        self.horizontalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Widget)

        self.stackedWidget.setCurrentIndex(1)
        self.main_menu_widgets.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.main_menu_button.setText(QCoreApplication.translate("Widget", u"Main Menu", None))
        self.books_menu_button.setText(QCoreApplication.translate("Widget", u"Books", None))
        self.loans_menu_button.setText(QCoreApplication.translate("Widget", u"Loans", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"Loan Create", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Book ID:", None))
        self.create_loan_button.setText(QCoreApplication.translate("Widget", u"Create", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"Loan Remove", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"Loan ID:", None))
        self.remove_loan_button.setText(QCoreApplication.translate("Widget", u"Remove", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Widget", u"Loans", None))
        self.show_all_loans_button.setText(QCoreApplication.translate("Widget", u"Show All Loans", None))
        self.label_10.setText(QCoreApplication.translate("Widget", u"First Name:", None))
        self.label_11.setText(QCoreApplication.translate("Widget", u"Last Name:", None))
        self.label_12.setText(QCoreApplication.translate("Widget", u"Membership:", None))
        self.label_13.setText(QCoreApplication.translate("Widget", u"Registration Date:", None))
        self.label_14.setText(QCoreApplication.translate("Widget", u"Info", None))
        self.label_15.setText(QCoreApplication.translate("Widget", u"Phone:", None))
        self.label_16.setText(QCoreApplication.translate("Widget", u"Email:", None))
        self.info_first_name_label.setText(QCoreApplication.translate("Widget", u"Name", None))
        self.info_last_name_label.setText(QCoreApplication.translate("Widget", u"Name", None))
        self.info_membership_label.setText(QCoreApplication.translate("Widget", u"Name", None))
        self.info_regis_date_label.setText(QCoreApplication.translate("Widget", u"Name", None))
        self.info_phone_label.setText(QCoreApplication.translate("Widget", u"Name", None))
        self.info_email_label.setText(QCoreApplication.translate("Widget", u"Name", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"Log In", None))
        self.login_email_edit.setText(QCoreApplication.translate("Widget", u"Email", None))
        self.login_password_edit.setText(QCoreApplication.translate("Widget", u"Password", None))
        self.login_button.setText(QCoreApplication.translate("Widget", u"Log In", None))
        self.label_8.setText("")
        self.go_signup_button.setText(QCoreApplication.translate("Widget", u"Sign Up", None))
        self.staff_check_box.setText(QCoreApplication.translate("Widget", u"Staff", None))
        self.label_9.setText(QCoreApplication.translate("Widget", u"Sign Up", None))
        self.signup_first_name_edit.setText(QCoreApplication.translate("Widget", u"First Name", None))
        self.signup_password_edit.setText(QCoreApplication.translate("Widget", u"Password", None))
        self.signup_button.setText(QCoreApplication.translate("Widget", u"Sign Up", None))
        self.signup_email_edit.setText(QCoreApplication.translate("Widget", u"Email", None))
        self.main_menu_back_button.setText(QCoreApplication.translate("Widget", u"Back", None))
        self.signup_last_name_edit.setText(QCoreApplication.translate("Widget", u"Last Name", None))
        self.signup_phone_edit.setText(QCoreApplication.translate("Widget", u"Phone Number", None))
        self.label_title_books.setText(QCoreApplication.translate("Widget", u"Book Name:", None))
        self.search_button_books.setText(QCoreApplication.translate("Widget", u"Search", None))
        self.books_author_edit.setText("")
        self.label_author_books.setText(QCoreApplication.translate("Widget", u"Author Name:", None))
        self.category_label_books.setText(QCoreApplication.translate("Widget", u"Category", None))
        self.checkBox_all_books.setText(QCoreApplication.translate("Widget", u"All", None))
        self.romance_box_books.setText(QCoreApplication.translate("Widget", u"Romance", None))
        self.horror_box_books.setText(QCoreApplication.translate("Widget", u"Horror", None))
        self.fantasy_box_books.setText(QCoreApplication.translate("Widget", u"Fantasy", None))
        self.tralve_box_books.setText(QCoreApplication.translate("Widget", u"Travel", None))
        self.short_story_box_books.setText(QCoreApplication.translate("Widget", u"Short Story", None))
        self.history_box_books.setText(QCoreApplication.translate("Widget", u"History", None))
        self.science_box_books.setText(QCoreApplication.translate("Widget", u"Science Fiction", None))
        self.adventure_box_books.setText(QCoreApplication.translate("Widget", u"Adventure", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Year", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Between", None))
        self.filter_button_books.setText(QCoreApplication.translate("Widget", u"Filter", None))
    # retranslateUi

