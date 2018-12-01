# -*- coding:utf-8 -*-


def study_enumerate():
    values = ['Apple', 'Bit', 'Coast', 'Docker']
    for index, value in enumerate(values):
        print(index, value)

    for index, value in enumerate(values, 1):
        print(index, value)

    li = list(enumerate(values, 1))
    print(li)


study_enumerate()

"""
result:
(0, 'Apple')
(1, 'Bit')
(2, 'Coast')
(3, 'Docker')
(1, 'Apple')
(2, 'Bit')
(3, 'Coast')
(4, 'Docker')
[(1, 'Apple'), (2, 'Bit'), (3, 'Coast'), (4, 'Docker')]
"""