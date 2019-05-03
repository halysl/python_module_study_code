# -*- coding: utf-8 -*-


def sep_by_other_symbol():
    li = ["a", 1, 2, 3]
    print(*li)
    print(*li, sep=",")
    print(*li, sep=":")
    print(*li, sep=",", end="!\n")
    for i in li:
        print(i)
    for i in li:
        print(i, end=" ")

if __name__ == "__main__":
    sep_by_other_symbol()
