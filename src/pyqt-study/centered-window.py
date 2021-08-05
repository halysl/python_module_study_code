# -*- coding:utf-8 -*-

import sys
# QDesktopWidget提供了桌面窗口的信息
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication

#设计一个新类，继承QWidgets类
class Example(QWidget):
	# 初始化方法，注意的是，python3中从父类调用初始化方法是，需要添加参数，如：
	# super(className, self)
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	# 初始化方法中的另一部分
	def initUI(self):		

		self.resize(250, 150)
		self.center() # 居中放在self.center()中完成
		self.setWindowTitle('Center')
		self.show()

	# 居中方法
	def center(self):

		qr = self.frameGeometry()  # 获得主窗口的一个矩形图形（并不是真的窗口）
		cp = QDesktopWidget().availableGeometry().center()  # 计算显示器的绝对值，并获得中心点
		qr.moveCenter(cp)  # 将qr矩形移动到显示器的中心，中心对中心
		self.move(qr.topLeft())  # 将真实的窗口移动到qr矩形的左上角，左上角对左上角


if __name__ == '__main__':

	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())