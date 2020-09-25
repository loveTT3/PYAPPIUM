#柱状图
'''
bar()函数 
'''

import matplotlib.pyplot as plt
import numpy as np

#构建数据
x_data = ['11','22','33','44','55','66','77']
y1_data = [11,22,33,44,55,66,77]
y2_data = [22,33,55,77,44,11,66]
#绘图
plt.bar(x=x_data,height=y1_data,label='第一个',color='steelblue',alpha=0.8)
plt.bar(x=x_data,height=y2_data,label='第二个',color='indianred',alpha=0.8)
#在柱状图上显示具体的数值，ha控制水平对齐方式，va控制垂直对齐方式
for x,y in  enumerate(y1_data):
    plt.text(x,y+3,'%s' %y,ha='center',va='bottom')
for x,y in enumerate(y2_data):
    plt.text(x,y+3,'%s' %y,ha='center',va='top')
#设置标题
plt.title('标题')
#为两坐标设置名称
plt.xlabel('横坐标')
plt.ylabel('纵坐标')
#显示图例
plt.legend()
plt.show()












