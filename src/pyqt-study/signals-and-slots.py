# -*- coding:utf-8 -*-

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication


class signalAndSlot(QWidget):
	def __init__(self):
		super(signalAndSlot, self).__init__()
		self.initUI()

	def initUI(self):

		# 实例化两个对象，一个QLCDNumber对象，一个QSlider对象
		lcd = QLCDNumber(self)
		sld = QSlider(Qt.Horizontal, self)

		# 将两个实例，箱布局，置入两个控件
		vbox = QVBoxLayout()
		vbox.addWidget(lcd)
		vbox.addWidget(sld)

		self.setLayout(vbox)
		# 事件连接，sld的valueChanged事件使得lcd的展示值变化
		sld.valueChanged.connect(lcd.display)

		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('Signal And Slot')
		self.show()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	sas = signalAndSlot()
	sys.exit(app.exec_())