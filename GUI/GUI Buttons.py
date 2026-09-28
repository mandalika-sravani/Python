# PyQt6 Buttons

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt6.QtGui import QIcon, QFont


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first GUI")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("GUI/channel-7.jpeg"))
        self.label = QLabel("Hello", self)
        self.initUI()

    def initUI(self):
        self.button = QPushButton("Click Me!", self)
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size : 30px;"
                             "color : #9c1f00;"
                             "background-color : #be95e8;"
                             "font-weight : bold;")
        self.button.clicked.connect(self.onClick)


        self.label.setFont(QFont("Arial", 25))
        self.label.setStyleSheet("color: #004e69;"
                            "background-color: #88cf95;"
                            "font-weight : bold;"
                            "text-decoration: underline;")
        self.label.setGeometry(150, 300, 200, 100)

    def onClick(self):
        self.label.setText("Goodbye!")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()