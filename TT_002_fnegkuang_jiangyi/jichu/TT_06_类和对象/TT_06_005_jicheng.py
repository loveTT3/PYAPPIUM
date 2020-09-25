#类的继承
#子类继承父类时，将多个父类放在子类之后的括号里
#class SubClass(SuperClass1，SuperClass2):


class Fruit:
    def info(self):
        print('我是一个水果，重%g克' %self.weight)
class Food:
    def taste(self):
        print('不同食物口感不同')

class Apple(Fruit,Food):
    pass

a = Apple()
a.weight = 5
a.info()
a.taste()

'''
多继承
父类中相同的方法，则匹配找到的第一个
'''
class Item:
    def info(self):
        print('Item中的方法： ','这是一个商品')
class Product:
    def info(self):
        print('Product中的一个方法： ','这是一个工业商品')

class Mouse(Item,Product):
    pass
m = Mouse()
m.info()


'''
重写父类的方法
'''
class Bird:
    def fly(self):
        print('我在天空里自由自在地飞翔')
class Ostrich:
    #子类重写父类的方法
    def fly(self):
        print('我只能在地上跑')
os = Ostrich()
os.fly()


'''
使用未绑定方法调用被重写的方法
通过类名调用，需要显示绑定第一个参数self
'''
class BaseClass:
    def foo(self):
        print('父类中的foo方法')
class SubClass:
    def foo(self):
        print('重写的方法')
    def bar(self):
        print('执行bar方法')
        self.foo()
        #调用父类的foo()方法
        BaseClass.foo(self)


'''
使用super函数调用父类的构造方法
1.使用未绑定方法，即类.方法
2.使用super()函数调用父类的构造方法
'''
class Emplyee:
    def __init__(self,salary):
        self.salary = salary
    def work(self):
        print('工资是： ',self.salary)
class Customer:
    def __init__(self,favorite,address):
        self.favorite = favorite
        self.address = address
    def info(self):
        print('爱好：%s，地址：%s '%(self.favorite,self.address))
class Manager(Emplyee,Customer):
    def __init__(self,salary,favorite,address):
        print('--Manage的构造方法--')
        super().__init__(salary)
        #与上一行代码效果相同
        #super (Manager , self) .一＿in it一一 （ salary)
        Customer.__init__(self,favorite,address)
m = Manager(25000,'IT','北京')
m.work()
m.info() 

























