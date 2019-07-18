# -*- coding: utf-8 -*-


def ten_2_two(number):
    res = bin(number)
    print(res)
    res = format(number, 'b')
    print(res)


def ten_2_eight(number):
    res = oct(number)
    print(res)
    res = format(number, 'o')
    print(res)


def ten_2_sixteen(number):
    res = hex(number)
    print(res)
    res = format(number, 'x')
    print(res)


def unknow_2_ten(number, jinzhi):
    number = str(number)
    jinzhi = int(jinzhi)
    res = int(number, jinzhi)
    print(res)

if __name__ == "__main__":
    num = 12345678
    ten_2_two(num)
    ten_2_eight(num)
    ten_2_sixteen(num)

    num = -12345678
    ten_2_two(num)
    ten_2_eight(num)
    ten_2_sixteen(num)

    num2 = "1010101"
    num8 = "7654321"
    num16 = "fedcba987654321"
    unknow_2_ten(num2, 2)
    unknow_2_ten(num8, 8)
    unknow_2_ten(num16, 16)
