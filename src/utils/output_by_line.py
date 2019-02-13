import os

def a():
    currect_path = os.path.dirname(os.path.abspath(__file__))
    with open(currect_path+'/temp', 'r') as f:
        data = ''
        for i in f.readlines():
            data += ''.join([' - ', i, '\n'])
    print(data)

def b():
    currect_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(currect_path, 'temp')
    with open(file_path, 'r') as f:
        data = [''.join(['-', i, '\n']) for i in f.readlines()]
        if data:
            print(''.join(data))
        else:
            print(None)

if __name__ == "__main__":
    a()
    b()

