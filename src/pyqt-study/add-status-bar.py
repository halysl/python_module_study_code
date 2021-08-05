# -*- coding:utf-8 -*-

import sys
# QMainWindow类提供了一个应用主窗口。默认创建一个拥有状态栏、工具栏和菜单栏的经典应用窗口骨架。
from PyQt5.QtWidgets import QApplication, QMainWindow


# 创建一个新类，继承自QMainWindow类
class Example(QMainWindow):
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	# 初始化方法中的另一部分
	def initUI(self):

		# 调用QMainWindow类的statusBar方法
		self.statusBar().showMessage('Ready')
		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('Statusbar')
		self.show()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())