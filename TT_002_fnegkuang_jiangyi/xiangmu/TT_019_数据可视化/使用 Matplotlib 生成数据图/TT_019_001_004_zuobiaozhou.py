import matplotlib.pyplot as plt

'''
x_data = [1,2,3,4,5]
y1_data = [11,22,33,44,55]
y2_data = [22,44,11,55,33]
ln1 = plt.plot(x_data,y1_data,color='red',linewidth=2,linestyle='--',label='第一条')
ln2 = plt.plot(x_data,y2_data,color='pink',linewidth=4,linestyle='-.',label='第二条')
plt.legend(loc='best')
#设置两个坐标轴的名称
plt.xlabel('横坐标')
plt.ylabel('纵坐标')
#设置数据图的标题
plt.title('这是一个标题')
#设置y轴上的数值文本
#第一个参数是点的位置，第二个参数是点的文字提示
plt.yticks([20,30,40],[r'低',r'中',r'高'])
plt.show()
'''


#对坐标轴的详细控制
import matplotlib.pyplot as plt
x_data = [1,2,3,4,5]
y1_data = [11,22,33,44,55]
y2_data = [22,44,11,55,33]
ln1 = plt.plot(x_data,y1_data,color='green',linewidth=4,linestyle=':',label='第一条线')
ln2 = plt.plot(x_data,y2_data,color='gray',linewidth=1,linestyle='-',label='第二条线')
plt.legend(loc='best')
#设置两个坐标轴名称
plt.xlabel('x 轴')
plt.ylabel('y 轴')
#设置图标题
plt.title('这是标题')
#设置y轴的刻度值
#第一个参数是点的位置，第二个坐标是点的文字提示
plt.yticks([11,22,33],['低','中','高'])
#plt.xticks([1,2,3,4,5],['一','二','三','四','五'])

#获取数据图上的坐标轴对象，是一个AxesSubplot对象
ax=plt.gca()
#设置将x轴的刻度值放在底部x轴上，bottom是放在底部x轴上  top是放在顶部x轴上
ax.xaxis.set_ticks_position('top')
#设置将y轴的刻度值放在左边y轴上，left right
ax.yaxis.set_ticks_position('left')
#设置右边坐标轴线的颜色（设置为none表示不显示）
ax.spines['right'].set_color('none')
#设置顶部坐标轴线的颜色（设置为none标识不显示）
ax.spines['top'].set_color('red')
#定义底部坐标轴线的位置（放在22数值处）
ax.spines['bottom'].set_position(('data',22))
plt.show()





