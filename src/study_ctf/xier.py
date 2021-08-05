import numpy as np

def say():
    print('''
    矩阵相关，将来做
    ''')
def getData():
    string = input("请输入密文：")
    code_string = input("请输入密钥：")
    return string,code_string

def word(string,code_string):
    max1 = np.mat((1,len(string)))
    max2 = np.mat((len(code_string)//len(string),len(string)))


def main():
    string,code_string = getData()
    encode_string = word(string,code_string)


if __name__ == "__main__":
    main()