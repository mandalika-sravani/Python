# PyQt6 Layout Manager

import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout)
from PyQt6.QtGui import QIcon

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layout GUI")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("GUI/channel-7.jpeg"))
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        l1 = QLabel("Label 1")
        l2 = QLabel("Label 2")
        l3 = QLabel("Label 3")
        l4 = QLabel("Label 4")
        l5 = QLabel("Label 5")
        l6 = QLabel("Label 6")

        l1.setStyleSheet("background-color : red;")
        l2.setStyleSheet("background-color : blue;")
        l3.setStyleSheet("background-color : green;")
        l4.setStyleSheet("background-color : yellow;")
        l5.setStyleSheet("background-color : violet;")
        l6.setStyleSheet("background-color : pink")

        #vbox = QVBoxLayout()

        #vbox.addWidget(l1)
        #vbox.addWidget(l2)
        #vbox.addWidget(l3)
        #vbox.addWidget(l4)
        #vbox.addWidget(l5)

        #central_widget.setLayout(vbox)

       # hbox = QHBoxLayout()
        
       # hbox.addWidget(l1)
        #hbox.addWidget(l2)
       # hbox.addWidget(l3)
       # hbox.addWidget(l4)
       # hbox.addWidget(l5)

        #central_widget.setLayout(hbox)

        gridbox = QGridLayout()
        
        gridbox.addWidget(l1, 0, 0)
        gridbox.addWidget(l2, 0, 1)
        gridbox.addWidget(l3, 0, 2)
        gridbox.addWidget(l4, 1, 0)
        gridbox.addWidget(l5, 1, 1)
        gridbox.addWidget(l6, 1, 2)

        central_widget.setLayout(gridbox)

        
        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()