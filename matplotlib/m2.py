# encoding=utf-8
import numpy as np
import matplotlib.pyplot as plt


def main():
    fig = plt.figure()

    # scatter 散点图
    fig.add_subplot(3, 3, 1)
    n = 128
    X = np.random.normal(0, 1, n)   # 生成随机数
    Y = np.random.normal(0, 1, n)
    T = np.arctan2(Y, X)    # T变量用来标注颜色
    # plt.axes([0.025, 0.025, 0.95, 0.95])
    plt.scatter(X, Y, s=25, c=T, alpha=.6)
    plt.xlim(-1.5, 1.5), plt.xticks([])
    plt.ylim(-1.5, 1.5), plt.yticks([])
    plt.axis()
    plt.title('Scatter')
    plt.xlabel('x')
    plt.ylabel('y')
    # plt.show()

    # bar 柱状图
    fig.add_subplot(332)
    n = 10
    X = np.arange(n)
    Y1 = (1 - X / float(n)) * np.random.uniform(.5, 1.0, n)
    Y2 = (1 - X / float(n)) * np.random.uniform(.5, 1.0, n)

    plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white') # 画图并着色
    plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')
    for x, y in zip(X, Y1):     # 添加标注
        plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')   
    for x, y in zip(X, Y2):
        plt.text(x + 0.4, -y - 0.05, '%.2f' % y, ha='center', va='top')
    # plt.show()

    # pie 饼图
    fig.add_subplot(333)
    n = 20
    Z = np.ones(n)
    Z[0] *= 3
    plt.pie(
            Z, explode=Z * .05, colors=['%f' % (i / float(n)) for i in range(n)],
            labels=['%.2f' % (i / float(n)) for i in range(n)]
            )
    plt.gca().set_aspect('equal')
    plt.xticks([])
    plt.yticks([])
    # plt.show()

    # polar 极坐标图
    fig.add_subplot(334, polar=True)
    n = 20
    theta = np.arange(0.0, 2 * np.pi, 2 * np.pi / n)
    radii = 10 * np.random.rand(n)
    plt.polar(theta, radii)
    # plt.show()

    # heatmap 热图
    fig.add_subplot(335)
    from matplotlib import cm   # 调用colormap包

    data = np.random.rand(3,3)
    cmap = cm.Blues
    plt.imshow(data, interpolation='nearest', cmap=cmap,aspect='auto', vmin=0, vmax=1)
    # plt.show()

    # 3d图
    from mpl_toolkits.mplot3d import Axes3D
    splt = fig.add_subplot(336, projection='3d')
    splt.scatter(1, 1, 3, s=100)
    # plt.show()

    # hotmap 热力图
    fig.add_subplot(313)

    def f(x, y):
        return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 - y**2)

    n = 256
    x = np.linspace(-3, 3, n)
    y = np.linspace(-3, 3, n)
    X, Y = np.meshgrid(x, y)
    plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap=plt.cm.hot)
    
    plt.savefig('figure_2.png')
    plt.show()
if __name__ == '__main__':
    main()