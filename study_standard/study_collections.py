# -*- coding:utf-8 -*-

from collections import defaultdict
from collections import Counter
from collections import deque
from collections import namedtuple


def study_default_dict():
    """
    默认字典
    常规字典：对未知的key没法append添加值
    默认字典：当key不存在时，创建一个key：null类似的字典
    """
    colours = (
        ('Yasoob', 'Yellow'),
        ('Ali', 'Blue'),
        ('Arham', 'Green'),
        ('Ali', 'Black'),
        ('Yasoob', 'Red'),
        ('Ahmed', 'Silver'),
    )

    favourite_colours = defaultdict(list)

    for name, colour in colours:
        favourite_colours[name].append(colour)

    print(favourite_colours)


def study_counter():
    """
    count会对一个迭代对象或者生成器的每个元素进行计数
    :return:
    """
    colours = (
        ('Yasoob', 'Yellow'),
        ('Ali', 'Blue'),
        ('Arham', 'Green'),
        ('Ali', 'Black'),
        ('Yasoob', 'Red'),
        ('Ahmed', 'Silver'),
    )

    fav = Counter(name for name, colour in colours)
    print(fav)


def study_deque():
    """
    双头队列，可从头部或尾部，插入或弹出
    append appendleft
    pop popleft
    :return:
    """
    d = deque()
    d.append(1)
    d.append(2)
    d.append([3, 4, 5])
    d.extend([6, 7, 8])
    print(d)

    d.pop()
    d.popleft()
    print(d)


def study_named_tuple():
    """
    命名元组
    可以通过.的方法调用元组信息，但其不是字典
    :return:
    """
    Animal = namedtuple('Animal', 'name age type')
    perry = Animal(name="perry", age=31, type="cat")
    print('perry:', perry)
    print('perry.name:%s' % perry.name)
    print('perry.age:%s' % perry.age)
    print('perry[0]:%s' % perry[0])


study_default_dict()
study_counter()
study_deque()
study_named_tuple()
