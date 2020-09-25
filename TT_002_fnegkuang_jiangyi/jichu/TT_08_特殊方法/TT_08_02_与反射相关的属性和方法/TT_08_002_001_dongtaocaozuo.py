#与反射相关的属性和方法
'''
程序在运行过程中要动态判断是否包含某个属性（包括方法）
甚至用动态设置某个属性值，通过python的反射支持来实现
'''

#动态操作属性
'''
hasattr(obj,name)  检查obj对象是否包含名为name的属性或方法
getattr(obj,name[,default])  获取object对象中名为name的属性的属性值
setattr(obj,name,value,/)  将obj对象的name属性设为value
'''



class Comment:
    def __init__(self,detail,view_times):
        self.detail = detail
        self.view_times = view_times
    def info(self):
        print('内容%s' %self.detail)
c = Comment('fx',20)
#判断是否包含指定的属性或方法
print(hasattr(c,'detail'))
print(hasattr(c,'view_times'))
print(hasattr(c,'info'))

#获取指定属性的属性值
print(getattr(c,'detail'))
print(getattr(c,'view_times'))
#由于info是方法所有下面代码报错：name 'info' id not defined
# print(getattr(c,'info','moren'))

#为指定属性设置属性值
setattr(c,'detail','天气不错')
setattr(c,'view_times',12)

#为不存在的属性赋值 可以  相当于添加新的属性
setattr(c,'xinde',1)
print(c.xinde)

#输出重新设置后的属性值
print(c.detail)
print(c.view_times)

#对不存在的方法进行设置
def bar():
    print('简单的bar()方法')
setattr(c,'info',bar)
c.info()


#将c的info设置为字符串，而不是方法，运行将会报错
setattr(c,'info','222')
# c.info()



