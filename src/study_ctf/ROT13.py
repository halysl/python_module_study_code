import re

def ree():
    isnum = re.compile(r'\d')
    isalpha_am = re.compile(r'[a-m]')
    isalpha_nz = re.compile(r'[n-z]')
    return isnum,isalpha_am,isalpha_nz

def get_data():
    string = input("请输入经过ROT13加密的字符串：")
    string = string.lower()
    return string

def ROT13(string):
    string_temp = []
    isnum,isalpha_am,isalpha_nz = ree()
    for i in string:
        if(isnum.match(i)):
            string_temp.append()
        elif(isalpha_am.match(i)):
            i = chr(ord(i)+13)
            string_temp.append(i)
        elif(isalpha_nz.match(i)):
            i = chr(ord(i)-13)
            string_temp.append(i)
        elif(i == " "):
            string_temp.append(" ")
        else:
            print("error")
    print("经过ROT3解密后的字符串为：%s"%(''.join(string_temp)))

def main():
    string = get_data()
    ROT13(string)


if __name__ == "__main__":
    main()