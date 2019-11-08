# 开始numpy的学习
# encoding=utf-8
#%%
import numpy as np


def main():
    lst=[[1., 3., 5.],
        [2., 4., 6.]]
    print(type(lst))
    np_lst=np.array(lst)
    print(type(np_lst))
    print(np_lst.shape)
    print(np_lst.dtype)
    print(np_lst.itemsize)
    print(np_lst.size)
    print(np.random.rand(2,4))

if __name__ == "__main__":
    main()
