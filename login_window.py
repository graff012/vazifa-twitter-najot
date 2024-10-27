from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QLabel, QMessageBox
from PyQt5.QtCore import Qt

from database import executive_sql_get
from post_window import PostWindow


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login Window")
        login_layout = QVBoxLayout()
        login_layout.setAlignment(Qt.AlignCenter)

        self.username_input = QLineEdit()
        self.username_input.setFixedWidth(300)
        self.username_input.setPlaceholderText("Enter username")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter the password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setFixedWidth(300)

        submit_btn = QPushButton("Submit")
        submit_btn.clicked.connect(self.enter_login)

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

    def enter_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        data = executive_sql_get("select * from users where username = %s and password = %s", (username, password))

        if data:
            self.post_window = PostWindow(data[0])
            self.post_window.resize(600 ,750)
            self.post_window.show()
            self.hide()
        else:
            QMessageBox.warning(self, "Error", "Login or password is incorrect")