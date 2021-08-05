# -*- coding:utf-8*-

import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QWidget


'''
创建箱布局类，继承自QWidget类
引入拉伸概念，将小组件放在大致的方位，可随着窗体变化而变化
'''
class boxLayout(QWidget):
	def __init__(self):
		super(boxLayout, self).__init__()
		self.initUI()

	def initUI(self):

		okButton = QPushButton('ok')
		cancalButton = QPushButton('cancel')

		hbox = QHBoxLayout()
		hbox.addStretch(1)
		hbox.addWidget(okButton)
		hbox.addWidget(cancalButton)

		vbox = QVBoxLayout()
		vbox.addStretch(1)
		vbox.addLayout(hbox)

		self.setLayout(vbox)

		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('Box Layout')
		self.show()


if __name__ == "__main__":
	app =QApplication(sys.argv)
	bp = boxLayout()
	sys.exit(app.exec_())