from ui_time import *

from pyqtgraph.Qt import QtWidgets
import pyqtgraph as pg
import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import datetime

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =  Ui_Form()
        self.ui.setupUi(self)
        self.calcTime()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.Tool)
        #ico = QPixmap("pytask.png")
        #self.setWindowIcon(ico)
        timer = QTimer(self)
        timer.timeout.connect(self.calcTime)
        timer.start(20000)


    def calcTime(self):
        now = datetime.datetime.now() # current date and time
        h = int(now.strftime("%H"))
        m = int(now.strftime("%M"))
        #s = int(now.strftime("%S"))
        #print("calctime "+str(h)+":"+str(m)+str(s))
        self.ui.lcd_hours.display(h)
        self.ui.lcd_minutes.display(m)


if __name__ == '__main__':
    app = pg.mkQApp()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())