from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QLabel
from PyQt5.QtCore import Qt

class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login Window")
        login_layout = QVBoxLayout()
        login_layout.setAlignment(Qt.AlignCenter)

        self.name_input = QLineEdit()
        self.name_input.setFixedWidth(300)
        self.name_input.setPlaceholderText("Enter your name")

        self.tel_input = QLineEdit()
        self.tel_input.setFixedWidth(300)
        self.tel_input.setPlaceholderText("Enter the tel number")

        self.username_input = QLineEdit()
        self.username_input.setFixedWidth(300)
        self.username_input.setPlaceholderText("Enter username")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter the password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setFixedWidth(300)

        submit_btn = QPushButton("Submit")
        submit_btn.clicked.connect(self.create_account)

        login_layout.addWidget(self.name_input)
        login_layout.addWidget(self.tel_input)
        login_layout.addWidget(self.username_input)
        login_layout.addWidget(self.password_input)
        login_layout.addWidget(submit_btn)


        self.setStyleSheet("""
            QWidget {
                background-color: #cfcbc0;
            }
            QPushButton {
                font-size: 23px;
                font-weight: bold;
                border-radius: 7px;
                background-color: #0c170f;
                color: white;
                padding: 10px;
                margin-top: 16px;
            }
            QLineEdit {
                border: 2px solid black;
                margin-bottom: 10px;
            }      
        """)
        self.setLayout(login_layout)

    def create_account(self):
        username = self.username_input.text()
        password = self.password_input.text()
