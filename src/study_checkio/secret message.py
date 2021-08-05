import re
def find_message(text):
    """Find a secret message"""
    try:
        a = re.findall(r'[A-Z]',text)
        b =""
        for i in a:
            b += i
        return b
    except:
        return ""

text = "How are you? Eh, ok. Low or Lower? Ohhh."
print(find_message(text))