'''
https://py.checkio.org/mission/long-repeat/
在这里你应该找到字符串中最长的相同字符重复出现的次数，并返回它的重复次数。例如：字符串“aaabbcaaaa”包含具有相同字母“aaa”，“bb”，“c”和“aaaa”的四个子字符串。 最后一个子字符串是最长的一个字符串，你应该返回 4 。

输入: 一个字符串.

输出: 一个整数.
'''
def long_repeat(string):
    count_max = [0,0,0,0,0,0,0,0,0,0]
    j = 0
    while string:
        for i in string:
            temp = string[0]
            if i==temp:
                count_max[j] += 1
            else:
                break
        string = string[count_max[j]:]
        j += 1
    maxnum = 0
    for i in range(10):
        print(count_max[i])
        if count_max[i]>=maxnum:
            maxnum = count_max[i]
    return maxnum

def main():
    str = "ddvvrwwwrggg"
    print(long_repeat(str))
if __name__ == "__main__":
    main()