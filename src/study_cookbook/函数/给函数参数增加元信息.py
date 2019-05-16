# -*- coding: utf-8 -*-


def test(a: int, b: float) -> float:
    return a + b

if __name__ == "__main__":
    func = test
    res = test(1, 2.0)

    print("func={}\nhelp(func)={}\n"
          "func.__annotation__={}\nfunc(1, 2.0)={}\n".format(
           func, help(func), func.__annotations__, res))
