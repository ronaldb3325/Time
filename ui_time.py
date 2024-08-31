# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_time.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLCDNumber, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.WindowModal)
        Form.resize(198, 100)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(18)
        Form.setFont(font)
        Form.setWindowTitle(u"Zeit")
        self.lcd_minutes = QLCDNumber(Form)
        self.lcd_minutes.setObjectName(u"lcd_minutes")
        self.lcd_minutes.setGeometry(QRect(110, 0, 81, 101))
        self.lcd_minutes.setDigitCount(2)
        self.lcd_minutes.setProperty("intValue", 10)
        self.lcd_hours = QLCDNumber(Form)
        self.lcd_hours.setObjectName(u"lcd_hours")
        self.lcd_hours.setGeometry(QRect(10, 0, 71, 101))
        font1 = QFont()
        font1.setPointSize(33)
        font1.setBold(True)
        self.lcd_hours.setFont(font1)
        self.lcd_hours.setDigitCount(2)
        self.lcd_hours.setProperty("intValue", 10)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        pass
    # retranslateUi

