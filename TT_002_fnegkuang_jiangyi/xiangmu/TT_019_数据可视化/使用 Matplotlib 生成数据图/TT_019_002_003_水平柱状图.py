#水平柱状图
'''
barh()函数
'''

import matplotlib.pyplot as plt
import numpy as np
#准备数据
x_data = ['11','22','33','44','55','66','77']
y1_data = [11,22,33,44,55,66,77]
y2_data = [11,33,55,77,66,22,44]
bar_width = 0.3
#
plt.barh(y=range(len(x_data)),width=y1_data,label='第一个',color='pink',alpha=0.8,height=bar_width)
plt.barh(y=np.arange(len(x_data))+bar_width,width=y2_data,label='第二个',color='green',alpha=0.8,height=bar_width)

#在柱状图上显示具体数值
for y,x in enumerate(y1_data):
    plt.text(x+3,y-bar_width/2,'%s'%x,ha='center',va='bottom')
for y,x in enumerate(y2_data):
    plt.text(x+3,y+bar_width/2,'%s'%x,ha='center',va='bottom')
#为y轴设置刻度值
plt.yticks(np.arange(len(x_data))+bar_width/2,x_data)
#设置标题
plt.title('标题')
plt.xlabel('横坐标')
plt.ylabel('纵坐标')
plt.legend('best')
plt.show()

