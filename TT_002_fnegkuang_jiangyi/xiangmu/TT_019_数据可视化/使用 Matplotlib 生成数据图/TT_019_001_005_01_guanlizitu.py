#管理多个子图
'''
调用subplot()函数创建子图，然后在子图上进行绘制
subplot(nrows,ncols,index,**kwargs)函数的参数
nrows参数指定将数据图区域分成多少行
ncols参数指定将数据图区域分成多少列
index参数指定获取第几区域
也可直接传入一个三位数的参数，分别代表行列位置
'''


import matplotlib.pyplot as plt
import numpy as np

plt.figure()
#定义一个从-pi到pi之间的数据，平均取64个数据点
#生成一个包含多个数值的列表，numpy.xin()、numpy.cos()、numpy.tan()等函数返回的也是列表
#传入列表包含多少值，返回的列表就包含多少值
x_data = np.linspace(-np.pi,np.pi,64,endpoint=True)
#将整个figure分成两行两列，第三个参数标识将该图形放在第一个网格中
plt.subplot(2,1,1)
#绘制正弦曲线
#plt.gca()获取数据图上的坐标轴对象
plt.plot(x_data,np.sin(x_data))
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.gca().spines['bottom'].set_position(('data',0))
plt.gca().spines['left'].set_position(('data',0))
plt.title('正弦')
#plt.show()


#将整个figure分成两行两列，并将该图放在第2个网格中
plt.subplot(223)
#绘制余弦曲线
plt.plot(x_data,np.cos(x_data),color='red',linewidth=1,linestyle=':',label='余弦曲线')
plt.legend(loc='upper right')
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
plt.title('余弦')


#将整个figure分成两行两列，并将改图放在第三个网格中
#每次调用subplot()函数后的代码标识在该子图区域绘图
plt.subplot(224)
#绘制正切曲线
ax = plt.gca()
plt.plot(x_data,np.tan(x_data),label='正切')
plt.legend(loc='best')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
plt.title('正切')

plt.show()



'''
y_data = [1,2,3,4,5]
plt.plot(y_data,color='black',linewidth=2,linestyle='--',label='第一个')
plt.show()
'''

















