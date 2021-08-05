import re
def between_markers(text: str, begin: str, end: str) -> str:
    if(re.search(begin,text)== None):
        a = 0
    else:
        a = re.search(begin,text).span()
        a = list(a)
        a = a[1]

    if (re.search(end, text) == None):
        b = -1
    else:
        b = re.search(end, text).span()
        b = list(b)
        b = b[0]
    print(a,b)
    if(a<b):
        print(text[a:b])
        #return(text[a:b])
    else:
        print('')
        #return ''



between_markers('No[/b] hi', '[b]', '[/b]')