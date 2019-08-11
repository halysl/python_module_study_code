# -*- coding: utf-8 -*-
import webbrowser

# 指定浏览器
c = webbrowser.get('firefox')
c.open('http://www.python.org')

webbrowser.open_new('http://www.python.org')
webbrowser.open_new_tab('http://www.python.org')
