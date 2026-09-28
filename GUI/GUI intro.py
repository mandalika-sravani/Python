# PyQt6 Introduction
# PyQt6 Labels

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first GUI")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("GUI/channel-7.jpeg"))

        # Added Labels

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 25))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: #004e69;"
                            "background-color: #88cf95;"
                            "font-weight : bold;"
                            "text-decoration: underline;")

        label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()