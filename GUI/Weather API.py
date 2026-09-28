# PYTHON PyQt6 WEATHER API APP

import sys
import requests
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class WeatherApp(QWidget):

    def __init__(self):
        super().__init__()
        self.city_input = QLineEdit(self)
        self.get_weather_btn = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")
        self.resize(420, 520)

        # Main Layout
        vbox = QVBoxLayout()
        vbox.setSpacing(15)

        self.city_input.setPlaceholderText("Enter city name...")

        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_btn)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        # Center content
        self.city_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.description_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Stylesheet
        self.setStyleSheet("""
            QWidget {
                background-color: #2b3137;
                font-family: Arial;
            }
            QLineEdit {
                font-size: 26px;
                padding: 10px;
                border: 2px solid #57606a;
                border-radius: 8px;
                color: #ffffff;
                background-color: #1e2227;
            }
            QPushButton {
                font-size: 22px;
                font-weight: bold;
                padding: 12px;
                background-color: #2ea44f;
                color: white;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #2c974b;
            }
            QLabel {
                color: #ffffff;
            }
        """)

        self.temperature_label.setStyleSheet("font-size: 65px; font-weight: bold; color: #58a6ff;")
        self.emoji_label.setStyleSheet("font-size: 85px; font-family: 'Segoe UI Emoji';")
        self.description_label.setStyleSheet("font-size: 24px; color: #8b949e; text-transform: capitalize;")

        # Signal connections
        self.get_weather_btn.clicked.connect(self.get_weather)
        self.city_input.returnPressed.connect(self.get_weather)

    def get_weather(self):
        # Replace with your OpenWeatherMap API key (free at openweathermap.org)
        api_key = "d46ad4955bf7d73f2056415e725501da"
        city = self.city_input.text().strip()

        if not city:
            self.display_error("Please enter a city name")
            return

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()

            if data.get("cod") == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError:
            match response.status_code:
                case 400:
                    self.display_error("Bad request:\nPlease check your input")
                case 401:
                    self.display_error("Invalid API key")
                case 403:
                    self.display_error("Access forbidden")
                case 404:
                    self.display_error("City not found")
                case 500:
                    self.display_error("Internal server error")
                case _:
                    self.display_error(f"HTTP error:\n{response.status_code}")
        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nServer took too long")
        except requests.exceptions.RequestException as req_err:
            self.display_error(f"Request Error:\n{req_err}")

    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 24px; color: #f85149;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 65px; font-weight: bold; color: #58a6ff;")
        
        temp_c = data["main"]["temp"]
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]

        self.temperature_label.setText(f"{temp_c:.1f}°C")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)

    @staticmethod
    def get_weather_emoji(weather_id):
        match weather_id:
            case _ if 200 <= weather_id <= 232:
                return "⛈️"
            case _ if 300 <= weather_id <= 321:
                return "🌦️"
            case _ if 500 <= weather_id <= 531:
                return "🌧️"
            case _ if 600 <= weather_id <= 622:
                return "❄️"
            case _ if 701 <= weather_id <= 781:
                return "🌫️"
            case 800:
                return "☀️"
            case _ if 801 <= weather_id <= 804:
                return "☁️"
            case _:
                return "🌡️"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec())