# PYTHON PyQt6 DIGITAL CLOCK

import os
import sys
from PyQt6.QtCore import Qt, QTime, QTimer
from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget


class DigitalClock(QWidget):

    def __init__(self):
        super().__init__()
        self.time_label = QLabel("12:00:00", self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 400, 300, 100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_label.setStyleSheet(
            "font-size : 150px; color : #26ff00;"
        )
        self.setStyleSheet("background-color : black;")

        # Resolve path relative to this script
        font_path = os.path.join(os.path.dirname(__file__), "DS-DIGIT.TTF")
        font_id = QFontDatabase.addApplicationFont(font_path)

        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            my_font = QFont(font_family, 150)
            self.time_label.setFont(my_font)
        else:
            print(f"Warning: Could not load '{font_path}'. Falling back to monospace.")
            self.time_label.setFont(QFont("Consolas", 150))

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        # In PyQt formats, 'AP' or 'ap' is used for AM/PM designation
        current_timer = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_timer)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec())