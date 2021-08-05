'''
https://py.checkio.org/mission/first-word/

You are given a string where you have to find its first word.

When solving a task pay attention to the following points:

There can be dots and commas in a string.
A string can start with a letter or, for example, a dot or space.
A word can contain an apostrophe and it's a part of a word.
The whole text can be represented with one word and that's it.
Input: A string.

Output: A string.
'''

import re
def first_word(text):
    text = re.sub('[^a-zA-Z\']',"?",text)
    print(text)
    a = text.split('?')
    totel = 0
    print(a)
    for i in a:
        try:
            while(i[0].isalpha()):
                print(i)
                break
            break
        except:
            continue


text = " word s4 wad"
first_word(text)