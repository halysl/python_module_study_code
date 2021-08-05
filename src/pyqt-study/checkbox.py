# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt


class checkBox(QWidget):
	def __init__(self):
		super(checkBox, self).__init__()
		self.initUI()

	def initUI(self):
		# 创建一个复选框
		cb = QCheckBox('Show title', self)
		cb.move(20, 20)
		cb.toggle()
		cb.stateChanged.connect(self.changeTitle)

		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('Check Box')
		self.show()

	def changeTitle(self, state):
		# 若复选框的状态为“已选”，则设置窗口标题为xxx，否则为“ ”
		if state == Qt.Checked:
			self.setWindowTitle('QCheckBox')
		else:
			self.setWindowTitle(' ')

if __name__ == "__main__":
	app = QApplication(sys.argv)
	cb = checkBox()
	sys.exit(app.exec_())