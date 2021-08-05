'''
https://py.checkio.org/mission/monkey-typing/
让我们假设我们的猴子正在打字，打字和打字，并产生了各种各样的短文本段。让我们试着检查他们是否合理的单词包含。

给你一些可能包含合理词汇的文字。您应该计算给定文本中包含多少个单词。一个词应该是完整的，可能是其他词的一部分。文字信箱没有关系。单词用小写字母表示，不要重复。如果一个单词出现在文本中多次，它应该只计算一次。

例如，text-“ "How aresjfhdskfhskd you?", word-("how", "are", "you", "hello")。结果将是3。

输入：两个参数。一个文本作为字符串（py2的unicode）和单词作为一组字符串（py2的unicode）。

输出：整数文本中的单词数量。
'''
def count_words(text, words):
    count = 0
    text = text.lower()
    for i in words:
        if i in text:
            count += 1
    return count


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")