# encoding=utf-8
# %%
import numpy as np


def main():
    lst = [
            [1., 3., 5.],
            [2., 4., 6.],
            [3., 7., 11.]
          ]
    print(type(lst))
    np_lst = np.array(lst)
    print(type(np_lst))
    print(np_lst.shape)
    print(np_lst.dtype)
    print(np_lst.itemsize)
    print(np_lst.size)

    # array opration
    print(np_lst)
    print(np.linalg.inv(np_lst))
    print(np_lst.transpose)

    print(np.random.rand(3, 3))
    

if __name__ == "__main__":
    main()
