# -*- coding:utf-8 -*-

import sys
# QMainWindow类提供了一个应用主窗口。默认创建一个拥有状态栏、工具栏和菜单栏的经典应用窗口骨架。
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


# 创建一个新类，继承自QMainWindow类
class Example(QMainWindow):
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	# 初始化方法中的另一部分
	def initUI(self):

		# 先创造一个QAction对象，该对象完成特定功能的抽象行为
		# 例如可以对某操作指定快捷键，添加状态栏提示，连接某个实际的操作
		exitAction = QAction(QIcon('web'), '&Exit', self) # 添加图标、添加“Exit”标示（&代表下划线）
		exitAction.setShortcut('Ctrl+Q') # 指定快捷键
		exitAction.setStatusTip('Exit Application') # 添加状态栏提示
		exitAction.triggered.connect(qApp.quit) # 触发某个操作

		self.statusBar()

		# 创建一个菜单栏
		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File') # addMenu()方法添加某个菜单到菜单栏	
		fileMenu.addAction(exitAction) # 在该菜单下添加一个抽象操作

		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('Menubar')
		self.show()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())