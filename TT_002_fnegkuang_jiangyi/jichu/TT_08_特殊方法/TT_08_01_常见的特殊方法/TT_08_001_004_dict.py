#__dict__属性

'''
__dict__属性查看对象内部存储的所有属性名和属性值组成的字典
可通过字典语法来访问或修改指定属性的值
'''

class Item:
    def __init__(self,name,price):
        self.name = name
        self.price = price
im = Item('鼠标',22.3)
print(im.__dict__)
print(im.__dict__['name'])
print(im.__dict__['price'])
im.__dict__['name'] = '键盘'
im.__dict__['price'] = 33
print(im.name)
print(im.price)

















