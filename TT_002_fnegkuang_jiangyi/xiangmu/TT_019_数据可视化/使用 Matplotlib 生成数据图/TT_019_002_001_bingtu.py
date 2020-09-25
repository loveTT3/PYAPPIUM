#饼图
'''
调用pie()函数绘制饼图

'''

import matplotlib.pyplot as plt
#准备数据
data= [0.16881,0.14966,0.07471,0.06992,0.04762,0.03541,0.02925,0.02411,0.02316,0.01409,0.36326]
#准备标签
labels = ['Javaz','C ','C＋＋','Python',
'VisualBasic.NET','C#','PHP','JavaScript','SQL', 'Assembly langugage' ,'其他 ']

#将排在第四的语言分离出来
explode = [0,0,0,0.3,0,0,0,0,0,0,0]
#使用自定义颜色
colors = ['red','pink','magenta','purple','orange','green','yellow','gray']
#将横纵坐标标准化处理，保证饼图是一个正圆，否则是椭圆
plt.axes(aspect='equal')
#控制xy轴的范围(用于控制饼图的圆心和半径)
plt.xlim(0,8)
plt.ylim(0,8)

a=plt.gca()
a.spines['bottom'].set_color('none')
a.spines['top'].set_color('none')
a.spines['left'].set_color('none')
a.spines['right'].set_color('none')
#绘制饼图
plt.pie(x = data,
    labels=labels,
    explode=explode,
    colors=colors,
    autopct='%3.f%%',
    pctdistance=0.8,
    labeldistance=1.15,
    startangle=180,
    center=(4,4),
    radius=3.8,
    counterclock=False,
    wedgeprops={'linewidth':1,'edgecolor':'green'},
    textprops={'fontsize':12,'color':'black'},
    frame=1
)

#不显示x轴和y轴的刻度值
plt.xticks(())
plt.yticks(())
#biaot
plt.title('饼图')
plt.show()









