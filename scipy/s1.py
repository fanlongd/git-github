# encoding=utf-8
# scipy
import numpy as np 


def main():
    # 积分 integrate
    from scipy.integrate import quad, dblquad, nquad
    print('QUAD:', quad(lambda x: np.exp(-x), 0, np.inf))
    print('DBLQUAD:', dblquad(
                        lambda t, x: np.exp(-x*t)/t**3, 0, np.inf,
                        lambda x: 1, lambda x: np.inf
                        )
            )
    
    def f(x, y):
        return x*y

    def bound_y():
        return [0, 1]

    def bound_x(y):
        return [0, 1-2*y]

    print('NQUAD:', nquad(f, [bound_x, bound_y]))

    # # optimizer 优化器
    # from scipy.optimize import minimize
    
    # def rosen(x):
    #     return sum()

if __name__ == '__main__':
    main()