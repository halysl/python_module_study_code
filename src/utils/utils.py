# -*- coding: utf-8 -*-
# @Date    : 2018-11-29 15:37:17
# @Author  : Light (halysl0817@gmail.com)
# @Link    : ${link}
# @Version : $Id$
# @slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
# @info: $info$


STYLE = {
    'fore':  # 前景色
        {
            'black': 30,  # 黑色
            'red': 31,  # 红色
            'green': 32,  # 绿色
            'yellow': 33,  # 黄色
            'blue': 34,  # 蓝色
            'purple': 35,  # 紫红色
            'cyan': 36,  # 青蓝色
            'white': 37,  # 白色
        },

    'back':  # 背景
        {
            'black': 40,  # 黑色
            'red': 41,  # 红色
            'green': 42,  # 绿色
            'yellow': 43,  # 黄色
            'blue': 44,  # 蓝色
            'purple': 45,  # 紫红色
            'cyan': 46,  # 青蓝色
            'white': 47,  # 白色
        },

    'mode':  # 显示模式
        {
            'mormal': 0,  # 终端默认设置
            'bold': 1,  # 高亮显示
            'underline': 4,  # 使用下划线
            'blink': 5,  # 闪烁
            'invert': 7,  # 反白显示
            'hide': 8,  # 不可见
        },

    'default':
        {
            'end': 0,
        },
}


def style_print(string, mode='', fore='', back=''):
    """调用ANSI_Escape_color，使输入结果渲染颜色

    :param string: str 字符串 'test'
    :param mode:str 显示模式 'bold'
    :param fore:str 前景色 'green'
    :param back:str 背景色 'red'
    :return: '\033[1;32;41m test \033[0m'
    """
    mode = '%s' % STYLE['mode'].get(mode, '')
    fore = '%s' % STYLE['fore'].get(fore, '')
    back = '%s' % STYLE['back'].get(back, '')

    style = ';'.join([s for s in [mode, fore, back] if s])
    style = '\033[%sm' % style if style else ''
    end = '\033[%sm' % STYLE['default']['end'] if style else ''

    print '%s%s%s' % (style, string, end)