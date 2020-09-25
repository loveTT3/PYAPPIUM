#析构方法 __del__

'''
与__init__()对应的是__del__()方法
__init__()  初始化Python对象
__del__()  销毁python对象  任何对象在被系统回收之时，都要自动调用__del__()方法
'''
'''
并不是对一个变量执行了del操作，该变量所引用的对象就会被回收--之后当对象的引用计数变为0时，该对象才会被回收
如果一个对象有多个变量引用他，del其中一个变量是不会回收该对象的
'''
class Item:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def __del__(self):
        print('del删除对象')
im= Item('鼠标',22.2)
x = im #1  删除后变先回收后结束
del im
print('-----------')





















