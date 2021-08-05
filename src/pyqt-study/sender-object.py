# -*- coding:utf-8 -*-


import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow

# 创建新类，继承自QMainWindow类
class senderObject(QMainWindow):
	def __init__(self):
		super(senderObject, self).__init__()
		self.initUI()

	def initUI(self):

		btn1 = QPushButton('button1', self)
		btn1.move(30, 50)
		btn2 = QPushButton('button2', self)
		btn2.move(150, 50)

		self.statusBar()

		# 两个按钮（的点击方法）和一个slot绑定
		btn1.clicked.connect(self.buttonClicked)
		btn2.clicked.connect(self.buttonClicked)

		self.setGeometry(300, 300, 200, 150)
		self.setWindowTitle('who send info')
		self.show()

	def buttonClicked(self):
		# 调用sender()方法确定了事件源（谁发起的事件）
		sender = self.sender()
		self.statusBar().showMessage(sender.text() + ' was pressed')

if __name__ == "__main__":
	app = QApplication(sys.argv)
	so = senderObject()
	sys.exit(app.exec_())