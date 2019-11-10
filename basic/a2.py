
# filter函数
import timeit

def is_prime(i):
    '''判断是否为素数'''
    for i_x in range(2, i):
        if i % i_x == 0:
            break
        else:
            return i            


TMPLIST = filter(is_prime, range(2, 1000))
NEWLIST = list(TMPLIST)
print(NEWLIST)
