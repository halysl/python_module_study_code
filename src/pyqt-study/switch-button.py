# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QPushButton, QFrame, QApplication
from PyQt5.QtGui import QColor
import sys

class switchButton(QWidget):

    def __init__(self):
        super(switchButton, self).__init__()

        self.initUI()


    def initUI(self):      

        self.col = QColor(0, 0, 0)

        # 设置三个按钮，setCheckable()方法，该方法决定按钮是否有按下状态（而不仅仅是可以连接一次事件）
        redb = QPushButton('Red', self)
        redb.setCheckable(True)
        redb.move(10, 10)

        #clicked方法此时添加一个变量bool，由当前按钮的状态决定
        redb.clicked[bool].connect(self.setColor)

        greenb = QPushButton('Green', self)
        greenb.setCheckable(True)
        greenb.move(10, 60)

        greenb.clicked[bool].connect(self.setColor)

        blueb = QPushButton('Blue', self)
        blueb.setCheckable(True)
        blueb.move(10, 110)

        blueb.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" % self.col.name())

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Toggle button')
        self.show()


    def setColor(self, pressed):

        source = self.sender()

        if pressed:
            val = 255
        else: val = 0

        if source.text() == "Red":
            self.col.setRed(val)                
        elif source.text() == "Green":
            self.col.setGreen(val)             
        else:
            self.col.setBlue(val) 

        self.square.setStyleSheet("QFrame { background-color: %s }" %
            self.col.name())  


if __name__ == '__main__':

    app = QApplication(sys.argv)
    sb = switchButton()
    sys.exit(app.exec_())