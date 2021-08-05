import re
def three_word(text):
    a = re.sub(r'[^a-zA-Z]',"?",text)
    print(a)
    a = a.split("?")
    b = 0
    for i in a:
        try:
            if(i[0].isalpha()):
                b = b*10+1
        except:
            b = b*10
    b = str(b)

string = "Hello World hello"
text = "He is 123 man"
three_word(string)
three_word(text)