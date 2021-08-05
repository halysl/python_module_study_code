# -*-coding:utf-8 -*-

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QStatusBar, QGridLayout, 
	                         QMainWindow, QLabel, QTextEdit)


# 目的设计出一个界面，实时输出全局按键次数
class editorWithCount(QMainWindow):
	def __init__(self):
		super(editorWithCount, self).__init__()
		self.initUI()

	def initUI(self):		

		label = QLabel('0', self)
		label.move(15,10)

		textEdit = QTextEdit(self)
		textEdit.move(30,10)		


		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('Editor With Count')
		self.show()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	ewc = editorWithCount()
	sys.exit(app.exec_())
