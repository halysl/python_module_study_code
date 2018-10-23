a = [{'a':1, 'b':2}, {'a':2, 'b':1}]
b = []

for item in a:
    print(item.get('a', ''))
    print(item.get('b', ''))

for item in b:
    print(item.get('a', ''))
    print(item.get('b', ''))     