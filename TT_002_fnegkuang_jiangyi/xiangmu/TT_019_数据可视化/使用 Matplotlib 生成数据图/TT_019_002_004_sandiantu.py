#散点图
'''
scatter()函数
参数：
    x:指定x轴数据
    y:指定y轴数据
    s：指定散点的大小
    c：指定散点的颜色
    alpha  指定散点的透明度
    linewidths  指定散点边框的宽度
    edgecolors   指定散点边框的颜色
    marker  指定散点的图形样式。参数支持”（点标记）、 ’，＇ （像素标记）、’0’ （圆形标记） 、
'v' （向下三角形标记〉、 Tj\T （ 向上三角形标记〉、可（向左三角形标记）、＇＞＇ （向右三角
形标记〉、 ’ l ’ （向下三叉标记）、’2’（向上三叉标记）、’3 ’ （ 向左三叉标记）、 ＇4' （向右三
叉标记）、 ＇ s’ （正方形标i己） 、＇p' （五地形标记）、 ’制 （星形标记〕、’h' （八边形标记）、
曰’（另 一种八边形标记）、＇＋＇ （力口号标记〉、＇x ' Cx 标记〉 、。’ （菱形标记〉、 ’d ’ （尖菱
形标记）、 ’｜’ （竖线标记）、 ” （横线标记）等值。
    cmap 指定散点的颜色映射 会使用不同的颜色来来区分散点的值
'''

import matplotlib.pyplot as plt
import numpy as np

plt.figure()
#定义从-pi到pi之间的数据，平均取64个点
x_data = np.linspace(-np.pi,np.pi,64,endpoint='True')
#延正弦曲线绘制散点图
plt.scatter(x_data,np.sin(x_data),c='purple',
    s=50,
    alpha=0.5,
    marker='p',
    linewidths=1,
    edgecolors=['green','yellow']
    )
#绘第二个图（只包含一个起点），突出起点
plt.scatter(x_data[0],np.sin(x_data)[0],c='red',
    s=150,
    alpha=1)
#绘第二个图（只包含一个结束点）突出结束点
plt.scatter(x_data[63],np.sin(x_data)[63],c='black',
    s=150,
    alpha=1
)

a=plt.gca()
a.spines['right'].set_color('none')
a.spines['top'].set_color('none')
a.spines['bottom'].set_position(('data',0))
a.spines['left'].set_position(('data',0))
plt.title('名称')
plt.show()









