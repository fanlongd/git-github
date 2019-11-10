''' 可变参数 '''


def squsum(*param):
    '''计算平方和'''
    suma = 0
    for i in param:
        suma += i*i
    print(suma)


squsum(1, 2, 3, 4)
