# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QProgressBar, QPushButton, QApplication
from PyQt5.QtCore import QBasicTimer

class progressBar(QWidget):
	def __init__(self):
		super(progressBar, self).__init__()
		self.initUI()

	def initUI(self):

		self.pbar = QProgressBar(self)
		self.pbar.setGeometry(30, 40, 200, 25)

		self.btn = QPushButton('Start', self)
		self.btn.move(40, 80)
		self.btn.clicked.connect(self.doAction)

		self.timer = QBasicTimer()
		self.step = 0

		self.setGeometry(300, 300, 280, 170)
		self.setWindowTitle('Progress Bar')
		self.show()

	def timeEvent(self, e):
		if self.step >= 100:
			self.time.stop()
			self.btn.setText('Finished')
			return

		self.step = self.step + 1
		self.pbar.setValue(self.step)

	def doAction(self):
		if self.timer.isActive():
			self.timer.stop()
			self.btn.setText('Start')
		else:
			self.timer.start(100, self)
			self.btn.setText('Stop')


if __name__ == "__main__":
	app = QApplication(sys.argv)
	pb = progressBar()
	sys.exit(app.exec_())