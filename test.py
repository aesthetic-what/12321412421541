import sys
from PyQt5.QtCore import QTimer
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.timer = QTimer()
        self.timer.timeout.connect(self.traffic_light)
        self.timer.start(2000)

        self.state = 0

        uic.loadUi("greenlight.ui", self)

        self.frame.setStyleSheet("background-color: rgb(144, 144, 144)")
        self.red.setStyleSheet("background-color: red; border-radius: 60px")
        self.yellow.setStyleSheet("background-color: darkyellow; border-radius: 60px")
        self.green.setStyleSheet("background-color: rgb(1, 50, 32); border-radius: 60px")

        self.min_frame.setStyleSheet("background-color: rgb(144, 144, 144)")
        self.min_red.setStyleSheet("background-color: rgb(139, 0, 0); border-radius: 60px")
        self.min_green.setStyleSheet("background-color: rgb(0, 128, 0); border-radius: 60px")


    def set_light(self, light, color):
        light.setStyleSheet(f"background-color: {color}; border-radius: 60px")


    def traffic_light(self):
        if self.state == 0:
            self.set_light(self.red, 'red')
            self.set_light(self.yellow, 'rgb(139, 128, 0)')
            self.set_light(self.green, 'rgb(1, 50, 32)')
            self.set_light(self.min_green, 'rgb(0, 128, 0)')
            self.set_light(self.min_red, 'rgb(139, 0, 0)')
            self.state = 1
        elif self.state == 1:
            self.set_light(self.red, 'red')
            self.set_light(self.yellow, 'yellow')
            self.set_light(self.green, 'rgb(1, 50, 32)')
            self.set_light(self.min_green, 'rgb(0, 128, 0)')
            self.state = 2
        elif self.state == 2:
            self.set_light(self.red, 'darkred')
            self.set_light(self.yellow, 'yellow')
            self.set_light(self.green, 'rgb(1, 50, 32)')
            self.set_light(self.min_green, 'rgb(1, 50, 32)')
            self.set_light(self.min_red, 'red')
            self.state = 3
        elif self.state == 3:
            self.set_light(self.red, 'darkred')
            self.set_light(self.yellow, 'rgb(139, 128, 0)')
            self.set_light(self.green, 'green')
            self.set_light(self.min_red, 'red')
            self.set_light(self.min_green, 'rgb(1, 50, 32)')
            self.state = 0








if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main_window()
    window.show()
    sys.exit(app.exec_())