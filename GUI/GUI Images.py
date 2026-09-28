# PyQt6 Images

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QIcon, QPixmap

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image GUI")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("GUI/channel-7.jpeg"))

        label = QLabel(self)
        label.setGeometry(0, 0, 500, 500)

        pixmap = QPixmap("GUI/Baby_Krishna_0fefb806-9b72-41a1-b195-326207d26ecc.webp")
        label.setPixmap(pixmap)

        label.setScaledContents(True)



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()