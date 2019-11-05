


# import numpy as np
# import numba
# from numba import jit

# # 不使用numba的情况
# @jit(nopython=True)
# def t():
#     x = 0
#     for i in np.arange(5000):
#         x += i
#     return x


# %timeit t()


with open('pc.py') as f:
    a = f.read()
    print(a)
