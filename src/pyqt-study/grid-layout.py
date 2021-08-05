# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget

# 创建网格布局类，继承自QWidget类
class gridLayout(QWidget):
	def __init__(self):
		super(gridLayout, self).__init__()
		self.initUI()

	def initUI(self):

		grid = QGridLayout()  # 实例化一个pyqt内置网格类
		self.setLayout(grid)  # 将该实例设置为当前窗口布局

		# 一个计算器上出现的字符的列表
		names = ['cls', 'Bck', '', 'Close',
		         '7', '8', '9', '/',
		         '4', '5', '6', '*',
		         '1', '2', '3', '-',
		         '0', '.', '=', '+']

		# 列表生成式，生成一个5行4列的二维数组，单个元素为(x,y)
		positions = [(i,j) for i in range(5) for j in range(4)]

		# 根据定位和names列表，生成一个按钮，然后窗口放置该控件（按钮）到指定位置
		for position, name in zip(positions, names):

			if name == '':
				continue
			button = QPushButton(name)
			grid.addWidget(button, *position)

		self.move(300, 150)
		self.setWindowTitle('Grid Layout')
		self.show()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	gp = gridLayout()
	sys.exit(app.exec_())