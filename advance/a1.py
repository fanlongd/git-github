# print函数中的 flush 参数用法

import time

print('---RUNOOB EXAMPLE ： Loading 效果---')

print('Loading', end='')
for i in range(20):
    print('.', end='', flush=True)
    time.sleep(0.5)
