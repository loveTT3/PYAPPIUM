#__dir__方法
'''
__dir__()方法用于列出该对象内部的所有属性（包括方法）名
返回包含所有属性（方法）名的序列
'''
'''
当对某个对象执行dir(object)函数时，实际上就是将该对象的__dir__()方法返回值进行排序 然后包装成列表
'''

class Item:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def info(self):
        pass
im = Item('鼠标',22.2)
print(im.__dir__())
print(dir(im))





