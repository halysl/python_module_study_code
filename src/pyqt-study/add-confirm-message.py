# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox


#设计一个新类，继承QWidgets类
class Example(QWidget):
	# 初始化方法，注意的是，python3中从父类调用初始化方法是，需要添加参数，如：
	# super(className, self)
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	# 初始化方法中的另一部分
	def initUI(self):		

		self.setGeometry(300, 300, 300, 300) 
		self.setWindowTitle('Quit button')
		self.show()

	# 关闭事件在点击右上角关闭时会触发
	def closeEvent(self, event):

		# 设置一个reply，接受一个方法的返回值，该方法返回一个字段
		# 该方法五个参数，分别是：自身self，确认提示对话框的标题，确认提示对话框的内容，两个按钮，一个默认按钮
		reply = QMessageBox.question(self, 'Message', 
			"Are you sure to quit?", 
			QMessageBox.Yes|QMessageBox.No, QMessageBox.No)

		# 根据reply的值，进行判断，若确定则退出，否则忽略这次关闭事件
		if reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()


if __name__ == '__main__':

	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())