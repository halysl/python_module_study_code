# -*- coding:utf-8 -*-

import sys
# QInputDialog类提供用户一个对话框，对话框内的数据可以传递，即用户可以通过对话框输入数据
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QInputDialog, QApplication


class inputDialog(QWidget):
	def __init__(self):
		super(inputDialog, self).__init__()
		self.initUI()

	def initUI(self):

		self.btn = QPushButton('Dialog', self)
		self.btn.move(20, 20)
		self.btn.clicked.connect(self.showDialog)

		self.le = QLineEdit(self)
		self.le.move(130, 22)

		self.setGeometry(300, 300, 200, 150)
		self.setWindowTitle('Input Dialog')
		self.show()

	def showDialog(self):
		# QInputDialog.getText()方法提供若干个参数，自身，对话框标题，对话框提示内容，（默认带一个文本栏）
		text, ok = QInputDialog.getText(self, 'Input Dialog', 'enter your name')
		# 若点击ok，则执行
		if ok:
			self.le.setText(str(text))

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ig = inputDialog()
	sys.exit(app.exec_())