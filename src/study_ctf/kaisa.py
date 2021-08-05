def getData():
    alp = [chr(i) for i in range(97,97+26)]
    string = input("请输入凯撒加密内容：")
    return string

def kaisa(string):
    if(string.isalpha()):
        string = string.lower()
        for i in range(1,27):
            print(str(i),end=" ")
            for j in string:
                if((ord(j)+i)>=97+26):
                    j = chr(ord(j)+i-26)
                else:
                    j = chr(ord(j)+i)
                print(j,end="")
            print()

def main():
    string = getData()
    kaisa(string)

if __name__ == "__main__":
    main()