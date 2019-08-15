import sys
import time


sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=32, cols=120))

print('正在加载......')
for i in range(101):
    time.sleep(0.05)
    show = ('>' * i).ljust(100)
    percent = f'{i}%'
    print(f'{show}{percent}')
    if i < 100:
        print('\033[3F')
print('Done!')
