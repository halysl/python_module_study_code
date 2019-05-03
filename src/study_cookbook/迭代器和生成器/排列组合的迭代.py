# -*- coding: utf-8 -*-

from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement


def pai_lie_zu_he():
    li = ["a", "b", "c"]
    print("带顺序的排列，也就是(a, b) != (b, a)")
    for i in permutations(li):
        print(i)
    for i in permutations(li, 2):
        print(i)
    for i in permutations(li, 1):
        print(i)
    print("无顺序的组合，也就是(a, b) == (b, a)")
    for i in combinations(li, 3):
        print(i)
    for i in combinations(li, 2):
        print(i)
    for i in combinations(li, 1):
        print(i)
    print("无顺序的组合，也就是(a, b) == (b, a)，但是元素可以重复")
    for i in combinations_with_replacement(li, 3):
        print(i)
    for i in combinations_with_replacement(li, 2):
        print(i)
    for i in combinations_with_replacement(li, 1):
        print(i)

if __name__ == "__main__":
    pai_lie_zu_he()
