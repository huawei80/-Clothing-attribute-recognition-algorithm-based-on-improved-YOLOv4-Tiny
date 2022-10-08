import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator
plt.rcParams["font.sans-serif"]=["SimHei"]

def rongHe():
    x_axis_data = [ 2, 3, 4, 5]  # x
    y_axis_data = [52.23, 52.71, 52.65, 50.31]  # y

    for x, y in zip(x_axis_data, y_axis_data):
        plt.text(x, y + 0.2, '%.2f' % y , ha='center', va='bottom', fontsize=10)  # y_axis_data1加标签数据

    plt.plot(x_axis_data, y_axis_data, 'r.-')  # 'bo-'表示蓝色实线，数据点实心原点标注
    ## plot中参数的含义分别是横轴值，纵轴值，线的形状（'s'方块,'o'实心圆点，'*'五角星   ...，颜色，透明度,线的宽度和标签 ，

    x_major_locator=MultipleLocator(1)
    ax=plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    # plt.legend()  # 显示上面的label
    plt.xlabel('融合特征层数', fontsize=10)  # x_label
    plt.ylabel('准确率/%', fontsize=10)  # y_label

    plt.ylim(50,54)#仅设置y轴坐标范围
    # plt.xlim(0,8)#仅设置y轴坐标范围
    plt.savefig('不同特征层.jpg')
    plt.show()


def get_s():
    x_axis_data = [1,2, 3, 4, 5,6]  # x
    y_axis_data = [47.39, 49.68, 50.96, 52.51, 52.53, 52.56]  # y

    for x, y in zip(x_axis_data, y_axis_data):
        plt.text(x, y + 0.2, '%.2f' % y, ha='center', va='bottom', fontsize=10)  # y_axis_data1加标签数据

    plt.plot(x_axis_data, y_axis_data, 'r.-')  # 'bo-'表示蓝色实线，数据点实心原点标注
    ## plot中参数的含义分别是横轴值，纵轴值，线的形状（'s'方块,'o'实心圆点，'*'五角星   ...，颜色，透明度,线的宽度和标签 ，

    x_major_locator = MultipleLocator(1)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    # plt.legend()  # 显示上面的label
    plt.xlabel('尺度维度' ,fontsize=10)  # x_label
    plt.ylabel('准确率/%', fontsize=10)  # y_label

    plt.ylim(47, 54)  # 仅设置y轴坐标范围
    # plt.xlim(0,8)#仅设置y轴坐标范围
    plt.savefig('scale.jpg')
    plt.show()

if __name__ == "__main__":
    #不同特征层数的融合实验对比
    rongHe()
    #不同scale的取值的实验结果对比
    get_s()