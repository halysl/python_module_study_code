def inputData():
    string = input("请输入栅栏加密的文字：")
    code = input("请输入分栏：（0代表从2到6逐个分栏）：")
    code = int(code)
    return string,code

def code2(string):
    string_temp = []
    string_temp.append(string[0::2])
    string_temp.append(string[1::2])
    print("分成2栏的结果是：%s" % (''.join(string_temp)))

def code3(string):
    string_temp = []
    string_temp.append(string[0::3])
    string_temp.append(string[1::3])
    string_temp.append(string[2::3])
    print("分成3栏的结果是：%s" % (''.join(string_temp)))

def code4(string):
    string_temp = []
    string_temp.append(string[0::4])
    string_temp.append(string[1::4])
    string_temp.append(string[2::4])
    string_temp.append(string[3::4])
    print("分成4栏的结果是：%s" % (''.join(string_temp)))

def code5(string):
    string_temp = []
    string_temp.append(string[0::5])
    string_temp.append(string[1::5])
    string_temp.append(string[2::5])
    string_temp.append(string[3::5])
    string_temp.append(string[4::5])
    print("分成5栏的结果是：%s" % (''.join(string_temp)))

def code6(string):
    string_temp = []
    string_temp.append(string[0::6])
    string_temp.append(string[1::6])
    string_temp.append(string[2::6])
    string_temp.append(string[3::6])
    string_temp.append(string[4::6])
    string_temp.append(string[5::6])
    print("分成6栏的结果是：%s" % (''.join(string_temp)))

def main():
    string, code = inputData()
    if (code == 0):
        code2(string)
        code3(string)
        code4(string)
        code5(string)
        code6(string)
    elif (code == 2):
        code2(string)
    elif (code == 3):
        code3(string)
    elif (code == 4):
        code4(string)
    elif (code == 5):
        code4(string)
    elif (code == 6):
        code4(string)
    else:
        print("error")

if __name__ == "__main__":
    main()