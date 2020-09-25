#动态属性与__slots__


class Cat:
    def __init__(self,name):
        self.name = name 
def walk_func(self):
    print('%s慢慢走过青青草地' %self.name)
d1 = Cat('Tom')
d2 = Cat('Jack')
#d1.walk_func()  #报错
#为Cat动态添加walk()方法，该方法的第一个参数会自动绑定
Cat.walk = walk_func
d1.walk()
d2.walk()



'''
如果程序要限制为某个类动态添加属性和方法，则可通过__slots__属性来指定
'''
class Dog:
    #只允许为Dog实例动态添加walk age name 这三个属性或方法
    __sloat__ = ('walk','age','name')
    def __init__(self,name):
        self.name = name
    def test():
        print('预定义好的test方法') 
d = Dog('Snoopy')
from types import MethodType
d.walk = MethodType(lambda self:print('%s慢慢走' %self.name),d)
d.age = 5
d.walk()
#__slots__属性不限制通过类来动态添加方法
Dog.bar = lambda self:print('aaa')
d.bar()
'''
__slots__属性指定的限制只对当前类起作用
'''
class GunDog(Dog):
    def __init__(self,name):
        super().__init__(name)
    pass
gd = GunDog("Puppy")
gd.speed = 22
print(gd.speed)




'''
使用type()函数定义类
程序使用class定义的所有类都是type类的实例
'''
class Role:
    pass
r = Role()
#查看对象r的变量类型
print(type(r))   #<class '__main__.Role'>
#查看Role类本身的变量类型
print(type(Role))   #<class 'type>
'''
使用type()函数来动态创建类，可指定三个参数
参数一：创建的类名
参数二：该类继承的父类集合。支持多继承，所以使用元组,就算只有一个父类(也要写逗号)
参数三：该字典对象为该类绑定的类变量和方法。key为类变量或方法名，value是普通值就代表变量，函数就代表方法
'''
def fn(self):
    print('fn函数')
#使用type()函数定义类
Dog = type('Dog',(object,),dict(walk=fn,age=6))
d = Dog()
print(type(d))
print(type(Dog))
d.walk()
print(Dog.age)




'''
使用metaclass
'''
#定义ItemMetaClass类，继承type
class ItemMetaClass(type):
    #cls代表被动态修改的类   name代表被动态修改的类名
    #bases代表被动态修改的类的所有父类   attrs代表被动态修改的类的所有属性、方法组成的字典
    def __new__(cls,name,bases,attrs):
        attrs['cal_price'] = lambda self:self.price * self.discount
        return type.__new__(cls,name,bases,attrs)
'''
metaclass类的__new__方法的作用：当程序使用class定义新类时，
若指定metaclass，那么metaclass的__new__方法就会被自动执行
'''
class Book(metaclass=ItemMetaClass):
    __sloat__ = ('name','price','_discount')
    def __init__(self,name,price):
        self.name = name
        self.price = price
    @property
    def discount(self):
        return self._discount
    @discount.setter
    def discount(self,discount):
        self._discount = discount
class CellPhone(metaclass = ItemMetaClass):
    __slots__ = ('price','_discount')
    def __init__(self,price):
        self.price = price
    @property
    def discount(self):
        return self._discount
    @discount.setter
    def discount(self,discount):
        self.discount = discount















