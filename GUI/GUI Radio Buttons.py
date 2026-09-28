# PyQt6 Radio Buttons

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QCheckBox, QRadioButton, QButtonGroup
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Radio Button GUI")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("GUI/channel-7.jpeg"))
        self.r1 = QRadioButton("Visa", self)
        self.r2 = QRadioButton("MasterCard", self)
        self.r3 = QRadioButton("Gift Card", self)
        self.r4 = QRadioButton("In-store", self)
        self.r5 = QRadioButton("Online", self)
        self.radio = QButtonGroup(self)
        self.initUI()

    def initUI(self):
        self.r1.setGeometry(0, 0, 300, 50)
        self.r2.setGeometry(0, 50, 300, 50)
        self.r3.setGeometry(0, 100, 300, 50)
        self.r4.setGeometry(0, 150, 300, 50)
        self.r5.setGeometry(0, 200, 300, 50)
        self.setStyleSheet("QRadioButton{"
                           "font-size : 30px;"
                           "font-family : Arial;"
                            "color : #9c1f00;"
                            "font-weight : bold;"
                            "padding : 10px;"
                            "}")

        self.radio.addButton(self.r1)
        self.radio.addButton(self.r2)
        self.radio.addButton(self.r3)
        self.radio.addButton(self.r4)
        self.radio.addButton(self.r5)

        self.r1.toggled.connect(self.radio_button_changed)
        self.r2.toggled.connect(self.radio_button_changed)
        self.r3.toggled.connect(self.radio_button_changed)
        self.r4.toggled.connect(self.radio_button_changed)
        self.r5.toggled.connect(self.radio_button_changed)

    def radio_button_changed(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()