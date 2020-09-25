#等高线图
'''
需要三维数据
contour()函数绘制等高线图  contourf()函数来填充颜色
参数：
    x  指定x轴数据
    y  指定y轴数据
    z  指定xy坐标对应的点的高度数据
    colors  指定不同高度的等高线的颜色
    alpha  指定等高线的透明度
    cmap  指定等高线的颜色映射 即自动使用不同的颜色来区分不同的高度区域
    lineswidths  指定等高线的宽度
    linestyles   指定等高线的样式 
'''


import matplotlib.pyplot as plt
import numpy as np

delta = 0.025
#生成代表x轴数据的列表
x = np.arange(-3.0,3.0,delta)
y = np.arange(-2.,2.0,delta)
#对x y数据进行网络化
X,Y  = np.meshgrid(x,y)
Z1 = np.exp(-X**2-Y**2)
Z2 = np.exp(-(X-1)**2-(Y-1)**2)
#计算z轴数据（高度数据）
Z = (Z1-Z2)*2
#为等高线填充颜色，16指定将等高线分为几部分
plt.contourf(x,y,Z,16,alpha=0.75,cmap='rainbow')
#绘制等高线
C= plt.contour(x,y,Z,16,colours='black',linewidth='0.5')
#绘制等高线数据
plt.clabel(C,inline=True,fontsize=10)
#去除坐标轴
plt.xticks(())
plt.yticks(())
plt.title('标题')
plt.xlabel('纬度')
plt.ylabel('经度')
plt.show()
