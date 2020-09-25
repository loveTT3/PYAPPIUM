#柱状图
'''
并列的两个柱柱
'''

import matplotlib.pyplot as plt
import numpy as np

#构建数据
x_data = ['11','22','33','44','55','66','77']
y1_data = [11,22,33,44,55,66,77]
y2_data = [11,44,66,55,22,77,33]
bar_width=0.3
#x数据改为range(len(x_data)),即0,1,2,3
plt.bar(x=range(len(x_data)),height=y1_data,label='第一个',color='red',alpha=0.8,width=bar_width)
#x数据改为np.arange(len(x_data))+bar_width
# plt.bar(x=np.arange(len(x_data))+bar_width+0.05,height=y2_data,label='第二个',color='blue',alpha=0.8,width=bar_width)
plt.bar(x=range(len(x_data))+bar_width+0.05,height=y2_data,label='第二个',color='blue',alpha=0.8,width=bar_width)

#在柱状图上显示具体的数值
for x,y in enumerate(y1_data):
    plt.text(x,y+3,'%s'%y,ha='center',va='bottom')
for x,y in enumerate(y2_data):
    plt.text(x+bar_width,y+3,'%s'%y,ha='center',va='top')
#设置标题
plt.title('标题')
#为x轴添加刻度值
plt.xticks(np.arange(len(x_data))+bar_width/2,x_data)
#设置两坐标轴名称
plt.xlabel('x轴')
plt.ylabel('y轴')
plt.legend()
plt.show()
















