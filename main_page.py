from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from login_window import LoginWindow
from register_window import RegisterWindow

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Twitter")
        self.resize(700, 850)

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)

        title_label = QLabel("Welcome to TWITTER")
        title_label.setStyleSheet("""
            font-size: 50px;
            font-weight: bold;
            margin-bottom: 30px;
        """)

        enter_btn = QPushButton("Login")
        enter_btn.clicked.connect(self.enter_login)

        register_btn = QPushButton("Create an account")
        register_btn.clicked.connect(self.create_account)

        self.setStyleSheet("""
            QWidget {
                background-color: #cfcbc0;
            }
            QPushButton {
                font-size: 26px;
                font-weight: bold;
                padding: 6px 20px;
                border-radius: 12px;
                background-color: #0c170f;
                color: white;
                margin: 6px;
            }      
        """)

        main_layout.addWidget(title_label)
        main_layout.addWidget(enter_btn)
        main_layout.addWidget(register_btn)

        self.setLayout(main_layout)

    def enter_login(self):
        self.login_window = LoginWindow()
        self.login_window.resize(600, 750)
        self.login_window.show()
        self.hide()

    def create_account(self):
        self.create_account = RegisterWindow()
        self.create_account.resize(600, 750)
        self.create_account.show()
        self.hide()