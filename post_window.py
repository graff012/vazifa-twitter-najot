from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel, QSpacerItem, QSizePolicy, QScrollArea
from PyQt5.QtCore import Qt
from database import executive_sql_get
from my_posts import MyPostsWindow
from write_post_window import WritePostWindow

class PostWindow(QWidget):
    def __init__(self, user_data):
        super().__init__()
        self.user_data = user_data
        self.setWindowTitle("Posts")
        self.resize(600, 750)

        main_layout = QVBoxLayout()

        # Scroll area for posts
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)

        try:
            self.posts = executive_sql_get(
                "SELECT p.id, u.username, p.text, p.created_date FROM posts p JOIN users u ON p.user_id = u.id"
            )
            if not self.posts:
                no_posts_label = QLabel("No posts available.")
                no_posts_label.setAlignment(Qt.AlignCenter)
                scroll_layout.addWidget(no_posts_label)

        except Exception as e:
            error_label = QLabel(f"Error fetching posts: {e}")
            scroll_layout.addWidget(error_label)

        else:
            for post in self.posts:
                post_label = QLabel(f"{post[1]}\n{post[2]}\n{post[3].strftime('%X')}\n")
                post_label.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
                scroll_layout.addWidget(post_label)

        # Add the scrollable widget to the scroll area
        scroll_area.setWidget(scroll_widget)
        main_layout.addWidget(scroll_area)

        # Buttons
        write_post_btn = QPushButton("Upload")
        write_post_btn.clicked.connect(self.enter_write_posts)

        my_posts_btn = QPushButton("My posts")
        my_posts_btn.clicked.connect(self.enter_my_posts)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(write_post_btn)
        btn_layout.addWidget(my_posts_btn)

        main_layout.addLayout(btn_layout)
        main_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Expanding))

        self.setStyleSheet("""
            QWidget {
                background-color: #cfcbc0;
            }
            QPushButton {
                font-size: 22px;
                font-weight: bold;
                padding: 6px 15px;
                border-radius: 7px;
                background-color: #0c170f;
                color: white;
                margin: 6px;
            }
            QLabel {
                border: 2px solid #0b111c;
                font-size: 18px;
                border-radius: 7px;
                padding-left: 8px;
                padding-top: 12px;
                margin: 7px;
            }
        """)

        self.setLayout(main_layout)
        print(self.posts)

    def enter_my_posts(self):
        self.my_posts = MyPostsWindow()
        self.my_posts.resize(600, 750)
        self.my_posts.show()
        self.hide()

    def enter_write_posts(self):
        self.write_post = WritePostWindow(self.user_data, self)
        self.write_post.resize(600, 750)
        self.write_post.show()
        self.hide()
