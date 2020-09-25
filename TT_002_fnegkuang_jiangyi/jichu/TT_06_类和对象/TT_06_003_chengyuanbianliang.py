#成员变量



'''
类变量和实例变量
'''
class Address:
    #两个类变量
    detail = '广州'
    post_code = '510660'
    def info(self):
        #直接访问类变量报错
        #print(detail)
        print(Address.detail)
        print(Address.post_code)
        print(self.detail)
print(Address.detail)
addr = Address()
addr.info()
Address.detail = '佛山'
Address.post_code = '460110'
addr.info()
#使用对象访问该对象所属类的类变量
print(addr.detail)

class Inventory:
    item = '鼠标'
    quantity = 2000
    def change(self,item,quantity):
        #以下语句不是对变量赋值，而是定义新的实例变量
        self.item = item
        self.quantity = quantity 
iv = Inventory()
iv.change('显示器',500)
#访问实例变量
print(iv.item)
print(iv.quantity)
#访问类变量
print(Inventory.item)
print(Inventory.quantity)


'''
使用property函数定义属性
'''
#property(fget = None,fset = None,fdel = None,doc = None)
#四个参数 读 写 删除 文档说明
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def setsize(self,size):
        self.width,self.height = size
    def getsize(self):
        return self.width,self.height
    def delsize(self):
        self.width,self.height = 0,0
    size = property(getsize,setsize,delsize,'用于描述矩形大小的属性')
#访问size属性说明文档
print(Rectangle.size.__doc__)
#通过内置的help（）函数查看Rectangle.size说明文档
help(Rectangle.size)
rect = Rectangle(4,3)
print(rect.size)
#赋值
rect.size = 9 ,7
print(rect.width)
print(rect.height)
del rect.size
print(rect.width)
print(rect.height)

#传入少量参数，只能读写不能删除
class User:
    def __init__(self,first,last):
        self.first = first
        self.last = last
    def getfullname(self):
        return self.first + ',' + self.last
    def setfullname(self,fullname):
        first_last = fullname.rsplit(',')
        self.first = first_last[0]
        self.last = first_last[1]
    fullname = property(getfullname,setfullname)
u = User('悟空','孙')
print(u.fullname)
u.fullname = '八戒,朱'
print(u.first)
print(u.last)


#使用@property修饰方法，相当于为该属性设置getter方法
class Cell:
    #使用@property修饰方法，使该方法变成了state属性的getter方法
    #若只有该方法，则state属性只是一个只读属性
    @property
    def state(self):
        return self._state
    @state.setter
    def state(self,value):
        if 'alive' in value.lower():
            self._state = 'alive'
        else:
            self._state = 'dead' 
    @property
    def is_dead(self):
        return not self._state.lower() == 'alive'
c = Cell()
c.state = 'Alive'
print(c.state)
print(c.is_dead)





















