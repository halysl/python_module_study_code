def getDate():
    string = input("请输入经过培根加密的字符串：")
    return string

def manage1(string):
    string = string.strip()
    temp_one = string[0]
    for i in string:
        if(i != temp_one):
            temp_two = i
            break
        else:
            continue
    manger2(string,temp_one,temp_two)

def manger2(string,a,b):
    str_temp1 = []
    str_temp2 = []
    str1 = []
    str2 = []
    for i in string:
        if(i == a):
            str_temp1.append("a")
            str_temp2.append("b")
        else:
            str_temp1.append("b")
            str_temp2.append("a")
    #str_temp1 = ''.join(str_temp1)
    #str_temp2 = ''.join(str_temp2)
    while(str_temp1):
        a,b,c,d,e = str_temp1[0:5]
        str1.append(manage3(a,b,c,d,e))
        str_temp1 = str_temp1[5:]
    while(str_temp2):
        a,b,c,d,e = str_temp2[0:5]
        str2.append(manage3(a,b,c,d,e))
        str_temp2 = str_temp2[5:]
    print(''.join(str1))
    print(''.join(str2))


def manage3(a,b,c,d,e):
    if(a == 'a'):
        if(b == 'a'):
            if(c == 'a'):
                if(d == 'a'):
                    if(e == 'a'):
                        return "a"
                    else:
                        return "b"
                else:
                    if(e == 'a'):
                        return "c"
                    else:
                        return "d"
            else:
                if(d == 'a'):
                    if(e == 'a'):
                        return "e"
                    else:
                        return "f"
                else:
                    if(e == 'a'):
                        return "g"
                    else:
                        return "h"
        else:
            if(c == 'a'):
                if(d == 'a'):
                    if(e == 'a'):
                        return "i"
                    else:
                        return "j"
                else:
                    if(e == 'a'):
                        return "k"
                    else:
                        return "l"
            else:
                if(d == 'a'):
                    if(e == 'a'):
                        return "m"
                    else:
                        return "n"
                else:
                    if(e == 'a'):
                        return "o"
                    else:
                        return "p"
    elif(a == 'b'):
        if(b == 'a'):
            if(c == 'a'):
                if(d == 'a'):
                    if(e == 'a'):
                        return "q"
                    else:
                        return "r"
                else:
                    if(e == 'a'):
                        return "s"
                    else:
                        return "t"
            else:
                if(d == 'a'):
                    if(e == 'a'):
                        return "u"
                    else:
                        return "v"
                else:
                    if(e == 'a'):
                        return "w"
                    else:
                        return "x"
        else:
            if(c == 'a'):
                if(d == 'a'):
                    if(e == 'a'):
                        return "y"
                    else:
                        return "z"

def main():
    string = getDate()
    string = manage1(string)

if __name__ == "__main__":
    main()