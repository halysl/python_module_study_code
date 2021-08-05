# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


#设计一个新类，继承QWidgets类
class Example(QWidget):
	# 初始化方法，注意的是，python3中从父类调用初始化方法是，需要添加参数，如：
	# super(className, self)
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	# 初始化方法中的另一部分
	def initUI(self):
		# setGeometry方法需要四个参数，分别代表窗口在屏幕中的x轴和y轴，窗口的宽度和高度，等于实现了resize+move
		self.setGeometry(300, 300, 300, 300) 
		self.setWindowTitle('Icon')
		self.setWindowIcon(QIcon('web'))  # 设置图标文件，默认在窗口左上角

		self.show()


if __name__ == '__main__':

	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())