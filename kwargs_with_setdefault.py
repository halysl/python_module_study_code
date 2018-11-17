# -*- coding: utf-8 -*-
# @Date    : 2018-10-30 18:37:17
# @Author  : Light (halysl0817@gmail.com)
# @Link    : ${link}
# @Version : $Id$
# @slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
# @info: $info$

def devide(a, b, **kwargs):
    """
    返回除值
    :param a number
    :param a number
    :param \*\*kwargs: Optional arguments that 'Precision'
    :return normal result float
    :return exception e.message str

    :exception1 ZeroDivisionError
    :exception2 TypeError
    """
    kwargs.setdefault('precision', 2)
    try:
        result = float(a)/b
        return '%.*f' % (kwargs['precision'], result)
    except ZeroDivisionError as e:
        return e.message
    except TypeError as e:
        return e.message

if __name__ == "__main__":
    pass