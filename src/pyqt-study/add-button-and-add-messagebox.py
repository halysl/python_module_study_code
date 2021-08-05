# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton
from PyQt5.QtGui import QFont


#设计一个新类，继承QWidgets类
class Example(QWidget):
	# 初始化方法，注意的是，python3中从父类调用初始化方法是，需要添加参数，如：
	# super(className, self)
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	# 初始化方法中的另一部分
	def initUI(self):
		QToolTip.setFont(QFont('SansSerif', 10))  # 设置“工具提示框”的字体
		# 给部件（整个窗口）添加提示文本，语句食用富文本，<b></b>代表加粗，<i></i>代表倾斜
		self.setToolTip('This is a <i>QWidget</i> widget')  

		btn = QPushButton('button', self)  # 建立一个按钮，并附着在当前widget上
		btn.setToolTip('This is a <b>QPushButton</b> widget')  # 给按钮添加提示文本
		btn.resize(btn.sizeHint())  # sizeHint()让系统给按钮一个合适的大小，也可自定义
		btn.move(50, 50)

		self.setGeometry(300, 300, 300, 300) 
		self.setWindowTitle('Tooltips')
		self.show()


if __name__ == '__main__':

	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())