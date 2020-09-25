#特殊方法
'''
方法名属性名前后添加双下划线  属于特殊方法和特殊属性
'''


#__repr__方法
'''
__repr__方法告诉外界对象具有的状态信息
返回对象实现类的“类名+object at+内存地址”值
'''
'''
输出Item对象时，实际输出的是Item对象的__repr__()方法的返回值
'''
class Item:
    def __init__(self,name,price):
        self.name = name
        self.price = price
im = Item('鼠标',22.2)
#下面两行代码效果一样
print(im)
print(im.__repr__())
print(im.__repr__)




#重写__repr__()方法
class Apple:
    def __init__(self,color,weight):
        self.color = color
        self.weight = weight
    def __repr__(self):
        return 'Apple[color=' + self.color + ",weight=" +str(self.weight) + "]" 
a = Apple('红色',22)
print(a)










