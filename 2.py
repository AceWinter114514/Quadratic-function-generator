import numpy as np
import matplotlib.pyplot as plt
import os


print("MadeByAceWinter")
while True:
    a = int(input('请输入二次项系数a：'))
    if a == 0:
        print('二次项系数不能为0')
    else:
        break
b = int(input('请输入一次项系数b：'))
c = int(input('请输入常数项c：'))

def quadratic_function(x, a=1, b=0, c=0) -> float:
    return a * x**2 + b * x + c

def general_to_vertex(a, b, c) -> tuple:
    # 计算顶点 h 和 k
    h = -b / (2 * a)
    k = c - (b**2) / (4 * a)
    return h, k

def check_function(a, b, c) -> None:
    if a > 0:
        print('抛物线开口向上')
    elif a < 0:
        print('抛物线开口向下')
    else:
        print('不是二次函数')
        return
    if a > 0:
        print('最小值为：', general_to_vertex(a, b, c)[1])
    elif a < 0:
        print('最大值为：', general_to_vertex(a, b, c)[1])
    else:
        print('不是二次函数')
def plot_interactive_quadratic() -> None:
    x1,x2 = input("请输入x的取值范围(形如“1,2”):").split(',')
    x = np.linspace(int(x1), int(x2), ((int(x2)-int(x1))*50))
    y = quadratic_function(x, a, b, c)
    # 绘制图像
    plt.figure(figsize=(10,10))
    plt.plot(x, y, label=f'y = ({a}x²) + ({b}x) + ({c})', color='blue')

    # 添加标题和坐标轴标签
    plt.title('Graph of Quadratic Function', fontsize=16)
    plt.xlabel('x', fontsize=14)
    plt.ylabel('y', fontsize=14)

    # 显示网格和图例
    plt.grid(color='pink',linestyle=':', linewidth=1)
    plt.axhline(0, color='black', linewidth=0.8)  # x轴
    plt.axvline(0, color='black', linewidth=0.8)  # y轴
    plt.legend(fontsize=12)

    # 显示图像
    plt.show()
    if __name__ == '__main__':
        print("二次函数为：y="+str(a)+"x²+"+str(b)+"x+"+str(c))
        print(f"顶点坐标为：{general_to_vertex(a, b, c)}")
        if general_to_vertex(a, b, c)[0] < 0:
            print(f"顶点式为：y={a}(x{general_to_vertex(a, b, c)[0]})²+{general_to_vertex(a, b, c)[1]}")
        else:
            print(f"顶点式为：y={a}(x-{general_to_vertex(a, b, c)[0]})²+{general_to_vertex(a, b, c)[1]}")
        check_function(a, b, c)
        os.system("pause")
plot_interactive_quadratic()