# -*- coding: utf-8 -*-

import time
from math import sqrt


def find_prime(upper):
    """找出小于upper的所有质数
        原理：素数分解定理，即任意合数都可以唯一分解为多个素数之积"""
    
    prime_list = list()   # 存放找到的质数
    for i in range(2, upper):   # 从2开始，逐一甄别是否是质数
        is_prime = True     # 假设当前数值i是质数
        for p in prime_list:    # 遍历当前已经找到的质数列表
            if i % p == 0:
                is_prime = False
                break
            elif p > sqrt(i):
                break
        
        if is_prime:
            prime_list.append(i)
    
    return prime_list


upper = 10000
t0 = time.time()
prime_list = find_prime(upper)
print(prime_list)
t1 = time.time()
print('查找%d以内的质数耗时%0.3f秒，共找到%d个质数'%(upper, t1-t0, len(prime_list)))
