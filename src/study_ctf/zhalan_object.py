class Get_Data(object):
    def __init__(self):
        pass
    def get_string(self):
        string = input("请输入栅栏加密的文字：")
        return string
    def get_code(self):
        code = input("请输入分栏：（0代表从2到6逐个分栏）：")
        code = int(code)
        return code

class zhalan(object):
    def __init__(self):
        pass
    def zhalan(self,string,code):
        string_temp = []
        code_temp = code
        sum = 0
        if(code == 0):
            for i in range(2,7):
                self.zhalan(string,i)
        else:
            while(code):
                string_temp.append(string[sum::code_temp])
                code -= 1
                sum += 1
            print("分成%d栏，结果是%s"%(code_temp,''.join(string_temp)))

def main():
    get_date = Get_Data()
    string = get_date.get_string()
    code = get_date.get_code()
    print("你提供的字符串为%s，你选择的分栏数为%d"%(string,code))
    zl = zhalan()
    zl.zhalan(string,code)

if __name__ == "__main__":
    main()