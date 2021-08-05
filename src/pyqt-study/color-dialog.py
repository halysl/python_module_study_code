# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame, 
	                         QColorDialog, QApplication)
from PyQt5.QtGui import QColor


class colorDialog(QWidget):
	def __init__(self):
		super(colorDialog, self).__init__()
		self.initUI()

	def initUI(self):
		col = QColor(0, 0, 0)

		self.btn = QPushButton('Dialog', self)
		self.btn.move(20, 20)

		self.btn.clicked.connect(self.showDialog)

		# 创建一个frame实例，给其设定一个背景色
		self.frm = QFrame(self)
		self.frm.setStyleSheet("QWidget { background-color: %s }"%col.name())
		self.frm.setGeometry(130, 22, 100, 100)

		self.setGeometry(300,300,250,180)
		self.setWindowTitle('Color Dialog')
		self.show()

	def showDialog(self):
		# 调用QColorDialog的getColor()方法，获得一个颜色，将其设置为frame的底色
		col = QColorDialog.getColor()
		if col.isValid():
			self.frm.setStyleSheet("QWidget { background-color: %s }"%col.name())


if __name__ == "__main__":
	app = QApplication(sys.argv)
	cd = colorDialog()
	sys.exit(app.exec_())