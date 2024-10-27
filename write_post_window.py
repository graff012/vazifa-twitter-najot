from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QLabel, QPushButton, QMessageBox
from PyQt5.QtCore import Qt

from database import executive_sql_get


class WritePostWindow(QWidget):
    def __init__(self, user_data, post_window):
        self.post_window = post_window
        self.user_data = user_data
        super().__init__()
        self.resize(600, 750)
        self.setWindowTitle("Upload Posts")

        main_layout = QVBoxLayout()

        title_label = QLabel("Upload Post")
        title_label.setStyleSheet("""
            font-size: 32px;
            font-weight: bold;
            padding: 10px;
        """)
        title_label.setAlignment(Qt.AlignCenter)


        self.post_text = QTextEdit()
        self.post_text.setPlaceholderText("Write your post here")

        post_btn = QPushButton("Post")
        post_btn.clicked.connect(self.write_post)

        main_layout.addWidget(title_label)
        main_layout.addWidget(self.post_text)
        main_layout.addWidget(post_btn)

        self.setStyleSheet("""
            QTextEdit {
                border: 2px solid black;
                font-size: 23px;
            }
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

        self.setLayout(main_layout)

    def write_post(self):
        text = self.post_text.toPlainText()
        executive_sql_get("insert into posts(text, user_id) values (%s, %s)", (text, self.user_data[0]))
        QMessageBox.information(self, "Information", "Post uploaded")
        self.hide()
        self.post_window.resize(600, 750)
        self.post_window.show()