# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton
from PyQt5.QtCore import QCoreApplication


#设计一个新类，继承QWidgets类
class Example(QWidget):
	# 初始化方法，注意的是，python3中从父类调用初始化方法是，需要添加参数，如：
	# super(className, self)
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	# 初始化方法中的另一部分
	def initUI(self):		

		qbtn = QPushButton('quit', self)  # 建立一个quit按钮，并附着在当前widget上
		qbtn.clicked.connect(QCoreApplication.instance().quit)  # 实现点击按钮退出效果
		qbtn.resize(qbtn.sizeHint())  # sizeHint()让系统给按钮一个合适的大小，也可自定义
		qbtn.move(50, 50)

		self.setGeometry(300, 300, 300, 300) 
		self.setWindowTitle('Quit button')
		self.show()


if __name__ == '__main__':

	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())