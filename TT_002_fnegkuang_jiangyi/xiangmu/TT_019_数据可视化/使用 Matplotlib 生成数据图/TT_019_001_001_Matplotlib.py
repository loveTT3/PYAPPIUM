import matplotlib.pyplot as plt

#复式折线图 颜色类型粗细


'''
#定义两个列表分别作为x，y轴
x_data = ['1','2','3','4','5','6']
y_data = [58000 , 60200 , 63000 , 71000 , 84000 , 107000]
#第一个代表横坐标的值，第二个代表纵坐标的值
plt.plot(x_data ,y_data)
#用show()来显示图形
#plt.show()
'''


'''
以下两种情况都会生成多条折线的复式折线图
'''
'''
#包含多条折线的复式折线图
x_data = ['1','2','3','4','5','6']
y_data = [58000 , 60200 , 63000 , 71000 , 84000 , 107000]
y_data2 = [100,200,30000,40000,60000,100]
#第一个代表横坐标的值，第二个代表纵坐标的值
plt.plot(x_data,y_data,x_data,y_data2)
#用show()来显示图形
#plt.show()
'''


'''
#包含多条折线的复式折线图
x_data = ['1','2','3','4','5','6']
y_data = [58000 , 60200 , 63000 , 71000 , 84000 , 107000]
y_data2 = [100,200,30000,40000,60000,100]
#第一个代表横坐标的值，第二个代表纵坐标的值
plt.plot(x_data,y_data)
plt.plot(x_data,y_data2)
#用show()来显示图形
#plt.show()
'''


'''
指定颜色、线宽、样式等
linestyle支持：-代表实线是默认值，--代表虚线，:代表点线，-.代表短线点相间的虚线
'''

x_data = ['1','2','3','4','5']
#x_data = [1,2,3,4,5]
y_data = [100,200,222,400,2039]
y_data2 = [999,888,666,111,666]
plt.plot(x_data,y_data,color = 'red',linewidth = 2.0,linestyle = '--')
plt.plot(x_data,y_data2,color = 'green',linewidth = 3.0,linestyle = '-.')
plt.show()



