# -*- coding:utf-8 -*-

import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication


# 创建通信类，继承自QObject类
class Communicate(QObject):
	closeApp = pyqtSignal()


class sendSignal(QMainWindow):
	def __init__(self):
		super(sendSignal, self).__init__()
		self.initUI()

	def initUI(self):
		# 实例化一个通信类对象，并将其closeApp字段连接至窗体关闭事件
		self.c = Communicate()
		self.c.closeApp.connect(self.close)

		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle("Send Signal")
		self.show()

	# 当鼠标进行点击时，将通信类对象的closeApp连接的事件（窗体关闭）触发
	def mousePressEvent(self, event):
		self.c.closeApp.emit()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ss = sendSignal()
	sys.exit(app.exec_())