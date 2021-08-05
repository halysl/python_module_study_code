import kaisa
import zhalan
import zhalan_object
import ROT13
import zhujuan
import peigen
import xier

def menu():
    li = ["1 凯撒加密",
          "2 栅栏加密(2-6)",
          "3 栅栏加密(无限)",
          "4 ROT13(初版，待优化)",
          "5 猪圈密码",
          "6 培根密码",
          "7 当铺密码",
          "8 希尔加密"]
    for i in li:
        print(i)

def select():
    sel = input("请输入选择：")
    sel = int(sel)
    li = ["kaisa.main()",
          "zhalan.main()",
          "zhalan_object.main()",
          "ROT13.main()",
          "zhujuan.main()",
          "peigen.main()",
          "zhujuan.display2()",
          "xier.say()"]
    eval(li[sel-1])

def main():
    menu()
    select()

if __name__ == "__main__":
    main()
