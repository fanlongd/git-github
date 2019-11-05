# 主要用来遍历/循环 序列、集合、字典

a = [['apple', 'orange', 'banana', 'grape'], (1, 2, 3)]
for x in a:
    for y in x:
        if y == 'orange':
            break
        print(y)
else:
    print('fruit is gone')
