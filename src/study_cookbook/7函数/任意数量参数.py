# -*- coding: utf-8


def avg_func(*arg):
    print(arg)
    isint = False not in [isinstance(i, (int, float)) for i in arg]
    avg = 0.0
    if isint:
        avg = sum(arg)/len(arg)
    return avg


def dict_func(**kwarg):
    print(kwarg)

if __name__ == "__main__":
    avg = avg_func(1.0, 2, 3, 4, 5)
    print(avg)
    dict_func(a=1, b=2, c=3)
