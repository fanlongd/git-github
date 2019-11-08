
# encoding=utf-8
import numpy as np
import matplotlib.pyplot as plt


def main():
    # line
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    c, s = np.cos(x), np.sin(x)
    plt.figure(1)
    plt.plot(x, c, color="blue", linewidth=1.0, linestyle="-", label="COS")
    plt.plot(x, s, "r*", label="SIN")
    plt.title('Cos & Sin')
    # 调用gca模块
    ax = plt.gca()
    # 设置坐标轴位置
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.spines["left"].set_position(("data", 0))
    ax.spines["bottom"].set_position(("data", 0))
    # 设置坐标轴范围
    # plt.axis([-np.pi/2, np.pi/2, -1, 1])
    # 设置坐标轴刻度
    ax.xaxis.set_ticks_position("bottom")
    ax.yaxis.set_ticks_position("left")
    plt.xticks(
                [-np.pi, -np.pi / 2, np.pi / 2, np.pi],
                [r'$-\pi$', r'$-\pi/2$', r'$\pi/2$', r'$\pi$']
               )
    plt.yticks(np.linspace(-1, 1, 5, endpoint=True))
    # 设置label属性
    for label in ax.get_xticklabels()+ax.get_yticklabels():
        label.set_fontsize(10)
        label.set_bbox(dict(facecolor="blue", edgecolor="None", alpha=0.0))
    # 设置legend
    plt.legend(loc="upper left")
    # 添加网格
    plt.grid()
    # 填充两个函数之间部分
    plt.fill_between(x, np.abs(x) < 0.5, c, c > 0.5, color="green", alpha=0.3)
    # plt.fill_betweenx(s, x, c, color="red", alpha=0.3)
    # 添加标注文字和标注线段
    t = np.pi/4
    plt.plot([t, t], [0, np.cos(t)], 'y', linewidth=2, linestyle='--')
    plt.annotate(
            r'$\cos(\pi/4)$', xy=(t, np.cos(t)), xytext=(+15, +5),
            xycoords='data', textcoords='offset points',
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.5')
                )
    
    plt.savefig("figure_1.png")     # 放在plt.show()前面
    plt.show()  

if __name__ == "__main__":
    main()
