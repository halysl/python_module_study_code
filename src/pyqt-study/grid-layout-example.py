# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QGridLayout, QLineEdit, QTextEdit, QWidget


# 一个网格布局示例类，继承自QWidget类
class gridLayoutExample(QWidget):
	def __init__(self):
		super(gridLayoutExample, self).__init__()
		self.initUI()

	def initUI(self):

		# 创建三个标签
		title = QLabel('Title')
		author = QLabel('Author')
		review = QLabel('Review')
		# 创建两个单行编辑框和一个文本编辑框
		titleEdit = QLineEdit()
		authorEdit = QLineEdit()
		reviewEdit = QTextEdit()
		# 网格布局创建，setspacing(num)表示每行之间的距离
		grid = QGridLayout()
		grid.setSpacing(10)
		# 分别将标签和编辑器放置在一起，根据addWidgrt()方法，最多提供五个参数，分别是控件、空间所在行，控件所在列，控件占据行，控件占据列
		grid.addWidget(title, 1, 0)
		grid.addWidget(titleEdit, 1, 1)
		
		grid.addWidget(author, 2, 0)
		grid.addWidget(authorEdit, 2, 1)

		grid.addWidget(review, 3, 0)
		grid.addWidget(reviewEdit, 3, 1, 5, 1)

		self.setLayout(grid)

		self.setGeometry(300, 300, 350, 300)
		self.setWindowTitle('Grid Layout Example')
		self.show()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	gle = gridLayoutExample()
	sys.exit(app.exec_())