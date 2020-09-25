#管理图例
'''
传入两个list参数  第一个(handles)引用折线，第二个(labels)代表添加的图例
'''

import matplotlib
#针对不支持中文的修改
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

x_data = ['20','21','22','23','24','25','26']
y1_data = [10,20,40,50,10,21,44]
y2_data = [99,88,77,33,45,33,22]
ln1 = plt.plot(x_data,y1_data,color='red',linewidth=2,linestyle='--')
ln2 = plt.plot(x_data,y2_data,color='black',linewidth=3,linestyle='-.')

#matplotlib不支持中文字体，坐下以下代码不能产生图例
#plt.legend(handles=[ln2,ln1],labels=['实例11','实例22'],loc='best')

#试着去实现中文,但是失败，下面另一种方法会成功
#my_font = fm.FontProperties(fname="C:\Windows\Fonts\msyh.ttf")
#plt.legend(handles=[ln2,ln1],labels=['第一个','第二个'],loc='best',prop=my_font)


'''
loc参数代表位置，参数值：
'best'：自动选择最佳位置                  
'upper right' ： 将图例放在右上角
'upper left' ： 放在左上角
'lower left' ： 左下角
'lower right' : 右下角
'right' : 右边
'center left' : 左边居中
'center right' : 右边居中
'lower center' : 底部居中
'upper center' : 顶部居中
'center' ： 放在中心
'''




#查询配置文件matplotlibrc地址
#print(matplotlib.matplotlib_fname())




import matplotlib.pyplot as plt
x_data = ['20','21','22','23','24','25','26']
#定义两个列表分别作为两条折线的 Y 轴数据
y1_data = [10,20,40,50,10,21,44]
y2_data = [99,88,77,33,45,33,22]
#指定折线的颜色、 线宽和样式
ln1 = plt.plot(x_data,y1_data,color='red',linewidth=2,linestyle='--',label='中文')
ln2 = plt.plot(x_data,y2_data,color='black',linewidth=3,linestyle='-.',label='222')
import matplotlib.font_manager as fm
#使用Matplotlib的字体管理器加载中文字体
my_font =fm.FontProperties(fname = "C:\Windows\Fonts\msyh.ttf")
#调用legend()函数设置图例
plt.legend(prop=my_font ,loc='best')
#调用show()函数显示图形
plt.show()


'''
永久改变字体
找到配置文件，修改配置Matplotlib参数
matplotlib.matplotlib_fname() 找到配置文件
修改参数：font.family : Microsoft YaHei
'''
#print(matplotlib.matplotlib_fname())


#参考文档
ckwd = 'https://matplotlib.org/users/legend_guide.html#creating-artists-specifically-for-adding-to-the-legend-aka-proxy-artists'




