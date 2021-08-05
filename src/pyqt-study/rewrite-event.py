# -*- coding:utf-8 -*-

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication


class rewriteEvent(QWidget):
	def __init__(self):
		super(rewriteEvent, self).__init__()
		self.initUI()

	def initUI(self):
		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('Rewrite Event')
		self.show()

	# 重写键盘输入事件，若若输入了ESC键，则程序退出
	def keyPressEvent(self, e):
		if e.key() == Qt.Key_Escape:
			self.close()



if __name__ == "__main__":
	app = QApplication(sys.argv)
	re = rewriteEvent()
	sys.exit(app.exec_())