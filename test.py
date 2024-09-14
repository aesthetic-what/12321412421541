import sys
from PyQt5 import uic
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel


class main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("greenlight.ui", self)
        self.timer = QTimer()
        self.timer.timeout.connect(self.traffic_light)
        self.timer.start(2000)

        self.display_timer = QTimer()
        self.display_timer.timeout.connect(self.update_timer_display)
        self.timer.start(1000)


        self.state = 0
        self.countdown = 2

        self.label.setText(str(self.countdown))



    def set_light(self, light, color):
        light.setStyleSheet(f"background-color: {color}; border-radius: 60px")

    def update_timer_display(self):
        # Обновляем отсчет на экране каждую секунду
        self.countdown -= 1
        self.label.setText(str(self.countdown))

        # Если отсчет завершился, сбрасываем значение
        if self.countdown <= 0:
            self.countdown = 2


    def traffic_light(self):
        if self.state == 0:
            self.set_light(self.red, 'red')
            self.set_light(self.yellow, 'grey')
            self.set_light(self.green, 'grey')
            self.set_light(self.min_green, 'rgb(0, 200, 0)')
            self.set_light(self.min_red, 'grey')
            self.state = 1
        elif self.state == 1:
            self.set_light(self.red, 'red')
            self.set_light(self.yellow, 'yellow')
            self.set_light(self.green, 'grey')
            self.set_light(self.min_green, 'rgb(0, 200, 0)')
            self.state = 2
        elif self.state == 2:
            self.set_light(self.red, 'grey')
            self.set_light(self.yellow, 'yellow')
            self.set_light(self.green, 'grey')
            self.set_light(self.min_green, 'rgb(0, 200, 0)')
            self.set_light(self.min_red, 'grey')
            self.state = 3
        elif self.state == 3:
            self.set_light(self.red, 'grey')
            self.set_light(self.yellow, 'grey')
            self.set_light(self.green, 'green')
            self.set_light(self.min_red, 'red')
            self.set_light(self.min_green, 'grey')
            self.state = 0
        
        self.countdown = 2


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main_window()
    window.show()
    sys.exit(app.exec_())