# -*- coding: utf-8 -*-
# @Date    : 2018-11-27 18:37:17
# @Author  : Light (halysl0817@gmail.com)
# @Link    : ${link}
# @Version : $Id$
# @slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
# @info: $info$

# map
# map(函数, iterable...)
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result1 = map(lambda x: x ** 2, list1)
print(list(result1))

result2 = map(lambda x, y: x + y, list1, list2)
print(list(result2))

tuple1 = (1, 2, 3, 4)
print(list(map(lambda x: x ** 2, tuple1)))


# filter
# filter(函数, iterable...)
list1 = [1, 2, 3, 4, 5]
print(list(filter(lambda x: x % 2 == 0, list1)))
print([x for x in list1 if x % 2 == 0])

list1 = [1, 2, 3, 4, 5]
print([x for x in list1 if x % 2 == 0])


# reduce
# reduce(函数, iterable, 初始化值)
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = reduce(lambda x, y: x + y, list1)
print(result)
result2 = reduce(lambda x, y: str(x) + str(y), list1, '==')
print(result2)


# sorted
# sorted(iterable)
# 列表排序(默认从小到大)
result = sorted([36, 6, -12, 9, -22])
print(result)
# 字符串排序，按照ASCII的大小排序
result = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(result)
# reverse逆序
result = sorted([36, 6, -12, 9, -22], reverse=True)
print(result)
# 添加函数排序使用关键参数key
L = [{1: 5, 3: 4}, {1: 3, 6: 3}, {1: 1, 2: 4, 5: 6}]
result = sorted(L, key=lambda x: len(x))
print(result)
# 元祖、字典使用排序
a = [('b', 2), ('a', 1), ('c', 0)]
print(sorted(a, key=lambda x: x[0]))
print(sorted(a, key=lambda x: x[1]))

b = [{'city': '深圳', 'tem': 40}, {'city': '广州', 'tem': 30}]
result = sorted(b, key=lambda x: x['tem'])
print(result)
