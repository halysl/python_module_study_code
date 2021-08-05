import sys
from PyQt5.QtWidgets import QApplication, QWidget # 常见模块

if __name__ == '__main__':
	# 先建立一个app实例
	app = QApplication(sys.argv)

	w = QWidget() # qt基础类，无参数的构造一个实例
	w.resize(250,150) # 自定义大小
	w.move(300,300) # 移动到屏幕某处 
	w.setWindowTitle('simple') # 设置窗口标题
	w.show() # 显示窗口

	sys.exit(app.exec_()) # 主循环
