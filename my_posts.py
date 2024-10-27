from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel, QSpacerItem, QSizePolicy
from datetime import datetime
from PyQt5.QtCore import Qt



class MyPostsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Posts")
        self.resize(600, 750)

        main_layout = QVBoxLayout()

        title_lable = QLabel("My Posts")
        title_lable.setAlignment(Qt.AlignCenter)
        title_lable.setStyleSheet("""
            font-size: 32px;
            font-weight: bold;
            padding: 10px;
        """)

        main_layout.addWidget(title_lable)

        self.posts = [
            (1, "graff012", "post text", datetime.now()),
            (1, "graff012", "post text", datetime.now()),
            (1, "graff012", "post text", datetime.now())
        ]

        for post in self.posts:
            post_layout = QVBoxLayout()
            post_label = QLabel(f"{post[1]}\n{post[2]}\n{post[3].strftime('%X')}")
            post_label.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)  # Center the post vertically
            post_label.setStyleSheet("""
                        border: 2px solid #0b111c;
                        font-size: 24px;
                        border-radius: 7px;
                        padding: 10px;
                        margin: 7px;
                        background-color: #ffffff;
                    """)
            post_layout.addWidget(post_label)
            main_layout.addLayout(post_layout)

        main_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Expanding))

        self.setStyleSheet("""
            QWidget {
                background-color: #cfcbc0;
            }
        """)

        self.setLayout(main_layout)



