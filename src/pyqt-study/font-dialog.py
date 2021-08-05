# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton, 
    QSizePolicy, QLabel, QFontDialog, QApplication)


class fontDialog(QWidget):
	def __init__(self):
		super(fontDialog, self).__init__()
		self.initUI()

	def initUI(self):

		vbox = QVBoxLayout()

		btn = QPushButton('Dialog', self)
		btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

		btn.move(20, 20)

		vbox.addWidget(btn)

		btn.clicked.connect(self.showDialog)

		# 示例字体
		self.lbl = QLabel('Knowledge only matters', self)
		self.lbl.move(130, 20)

		vbox.addWidget(self.lbl)
		self.setLayout(vbox)

		self.setGeometry(300, 300, 250, 180)
		self.setWindowTitle('Font Dialog')
		self.show()

	def showDialog(self):
		# 调用QFontDialog的grtFont()方法获取字体信息，赋值给font，再设置为label的字体
		font, ok = QFontDialog.getFont()
		if ok:
			self.lbl.setFont(font)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	fd = fontDialog()
	sys.exit(app.exec_())