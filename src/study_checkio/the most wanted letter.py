'''
https://py.checkio.org/mission/most-wanted-letter/
给你一个其中包含不同的英文字母和标点符号的文本，你要找到其中出现最多的字母，
返回的字母必须是小写形式，
当检查最想要的字母时，不区分大小写，所以在你的搜索中 "A" == "a"。 
请确保你不计算标点符号，数字和空格，只计算字母。
如果你找到 两个或两个以上的具有相同的频率的字母， 返回那个先出现在字母表中的字母。 例如 -- “one”包含“o”，“n”，“e”每个字母一次，因此我们选择“e”。
'''
import re

def checkio(text):
    text = re.sub('[^a-zA-Z]',"",text)
    text = text.lower()
    arr = [[]*26]*26
    max_len = 0
    for i in range(26):
        temp = chr(ord('a')+i)
        arr[i] = re.findall(temp,text)
    for i in range(26):
        if len(arr[i])>max_len:
            max_len = len(arr[i])
            tt = arr[i][0]
    return tt


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")