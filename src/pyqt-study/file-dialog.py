# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QFileDialog, QApplication
from PyQt5.QtGui import QIcon


class fileDialog(QMainWindow):
	def __init__(self):
		super(fileDialog, self).__init__()
		self.initUI()

	def initUI(self):

		self.textEdit = QTextEdit()
		self.setCentralWidget(self.textEdit)
		self.statusBar()

		# 添加一个打开文件事件
		openfile = QAction(QIcon('web'), 'open', self)
		openfile.setShortcut('Ctrl+O')
		openfile.setStatusTip('Open new File')
		openfile.triggered.connect(self.showDialog)

		# 将打开文件事件放入菜单中
		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(openfile)

		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('File Dialog')
		self.show()

	def showDialog(self):
		# 调用QFileDialog的getOpenFileName()方法，打开一个文件选择对话框，返回一个文件名，默认位置为‘/home’
		fname = QFileDialog.getOpenFileName(self, 'Open File', '/home')
		if fname[0]:
			f = open(fname[0], 'r')

			with f:
				data = f.read()
				self.textEdit.setText(data)

if __name__ =="__main__":
	app = QApplication(sys.argv)
	fd = fileDialog()
	sys.exit(app.exec_())