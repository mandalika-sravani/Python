# PyQt6 Text Edits

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Line Edits GUI")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("GUI/channel-7.jpeg"))
        self.line = QLineEdit(self)
        self.button = QPushButton("Submit", self)
        self.initUI()

    def initUI(self):
        self.line.setGeometry(10, 10, 200, 40)
        self.button.setGeometry(210, 10, 200, 40)
        self.line.setStyleSheet("font-size : 25px;" 
                                "font-family : Arial;"
                                "color : #175719;")
        self.button.setStyleSheet("font-size : 35px;" 
                                "font-family : Arial;"
                                "color : #4a050a;"
                                "backgotund-color : #945bb3;")

        self.line.setPlaceholderText("Enter your name")
        
        self.button.clicked.connect(self.submit)

    def submit(self):
        text = self.line.text()
        print(f"Hello {text}")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()