# PyQt6 Checkbox

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QCheckBox
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Checkbox GUI")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("GUI/channel-7.jpeg"))
        self.checkbox = QCheckBox("Do you like food?", self)
        self.initUI()

    def initUI(self):
        self.checkbox.setGeometry(10, 0, 500, 100)
        self.checkbox.setStyleSheet("font-size : 30px;"
                                    "font-family : Arial;"
                                    "color : #9c1f00;"
                                    "font-weight : bold;")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self, state):
        if self.checkbox.isChecked():
            print("You like the food")
        else:
            print("You don't like the food")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()