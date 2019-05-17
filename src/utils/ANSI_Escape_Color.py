# -*- coding: utf-8 -*-
# @Date    : 2018-12-06 16:46:17
# @Author  : Light (halysl0817@gmail.com)
# @Link    : ${link}
# @Version : 0.1
# @slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
# @info: 调用ANSI_Escape_color，使输入结果渲染颜色

#   格式：开头                      字符串   结尾（可省去）
#        \033[显示方式;前景色;背景色m $str    \033[0m
#   说明:
#
#   前景色            背景色            颜色
#   ---------------------------------------
#     30                40              黑色
#     31                41              红色
#     32                42              绿色
#     33                43              黃色
#     34                44              蓝色
#     35                45              紫红色
#     36                46              青蓝色
#     37                47              白色
#
#   显示方式           意义
#   -------------------------
#      0           终端默认设置
#      1             高亮显示
#      4            使用下划线
#      5              闪烁
#      7             反白显示
#      8              不可见
#
#   例子：
#   \033[1;31;40m    <!--1-高亮显示 31-前景色红色  40-背景色黑色-->
#   \033[0m          <!--采用终端默认设置，即取消颜色设置-->]]]


STYLE = {
    'fore':
        {   # 前景色
            'black': 30,  # 黑色
            'red': 31,  # 红色
            'green': 32,  # 绿色
            'yellow': 33,  # 黄色
            'blue': 34,  # 蓝色
            'purple': 35,  # 紫红色
            'cyan': 36,  # 青蓝色
            'white': 37,  # 白色
        },

    'back':
        {   # 背景
            'black': 40,  # 黑色
            'red': 41,  # 红色
            'green': 42,  # 绿色
            'yellow': 43,  # 黄色
            'blue': 44,  # 蓝色
            'purple': 45,  # 紫红色
            'cyan': 46,  # 青蓝色
            'white': 47,  # 白色
        },

    'mode':
        {   # 显示模式
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

    print('%s%s%s' % (style, string, end))


def TestColor():
    style_print('正常显示')
    # 测试显示模式
    style_print('高亮', mode='bold')
    style_print('下划线', mode='underline')
    style_print('闪烁', mode='blink')
    style_print('反白', mode='invert')
    style_print('不可见', mode='hide')
    # 测试前景色
    style_print('黑色', fore='black')
    style_print('红色', fore='red')
    style_print('绿色', fore='green')
    style_print('黄色', fore='yellow')
    style_print('蓝色',   fore='blue')
    style_print('紫红色', fore='purple')
    style_print('青蓝色', fore='cyan')
    style_print('白色',   fore='white')

    # 测试背景色
    style_print('黑色',   back='black')
    style_print('红色',   back='red')
    style_print('绿色',   back='green')
    style_print('黄色',   back='yellow')
    style_print('蓝色',   back='blue')
    style_print('紫红色', back='purple')
    style_print('青蓝色', back='cyan')
    style_print('白色',   back='white')

if __name__ == '__main__':
    TestColor()
