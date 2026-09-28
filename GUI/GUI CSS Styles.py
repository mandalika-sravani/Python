# PyQt6 CSS Styles

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("CSS Styles GUI")
        self.setWindowIcon(QIcon("GUI/channel-7.jpeg"))
        self.b1 = QPushButton("Button 1")
        self.b2 = QPushButton("Button 2")
        self.b3 = QPushButton("Button 3")
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.b1)
        hbox.addWidget(self.b2)
        hbox.addWidget(self.b3)

        central_widget.setLayout(hbox)

        self.b1.setObjectName("button1")
        self.b2.setObjectName("button2")
        self.b3.setObjectName("button3")


        self.setStyleSheet("""
            QPushButton {
                font-size : 35px;
                font-family : Arial;
                padding : 15px 75px;
                margin : 25px;
                border : 2px solid;
                border-radius : 15px;
                color : white;
            }
            QPushButton#button1{
                background-color : #cf3f30;
            }
            QPushButton#button2{
                background-color : #77c447;
            }
            QPushButton#button3{
                background-color : #254ea1;
            }

            QPushButton#button1:hover{
                background-color : #eb877c;
            }
            QPushButton#button2:hover{
                background-color : #abf27e;
            }
            QPushButton#button3:hover{
                background-color : #78c8eb;
            }
                        
        """)



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()