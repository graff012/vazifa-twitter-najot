from PyQt5.QtWidgets import QApplication, QMessageBox
from database import load_db, load_data
from main_page import MainWindow

def initialize_database():
    try:
        load_db()
        load_data()
    except Exception as e:
        print(f"Error initializing database: {e}")

        QMessageBox.critical(None, "Database Error", "Failed to initialize the database.")

if __name__ == "__main__":
    app = QApplication([])

    initialize_database()

    main = MainWindow()
    main.show()

    app.exec_()
