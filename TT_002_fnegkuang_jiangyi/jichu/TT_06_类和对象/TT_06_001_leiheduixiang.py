'''
类个对象
'''

class Person:
    '这是一个Person类'
    #定义类变量
    hair = 'black'
    #构造方法
    def __init__(self,name = 'charlie',age = 8):
        #为person对象增加两个实例变量
        self.name = name
        self.age = age
    #普通方法
    def say(self,content):
        print(content)

p = Person()
print(p.name,p.age)
p.name = '孙悟空'
print(p.name,p.age)
p.say('棒棒哒')

'''
python是动态语言，可谓p增加动态增加实例变量，只要为新变量赋值即可
也可动态删除实例变量 用del语句
'''
#为p对象增加一个skills实例变量
p.skills = ['progeamming','swimming']
print(p.skills)
#删除p对象的name实例变量
del p.name
#print(p.name)

'''
为对象动态增加方法
python不会自动将调用者自动绑定到第一个参数(即使第一个参数命名为self也没用)
'''
#定义一个函数
def info(self):
    print('----info函数----',self)
#使用info对p的foo方法赋值（动态增加方法）
p.foo = info
#Python不会自动将调用者绑定到第一个参数
#因此程序需要手动将调用者绑定到第一个参数
p.foo(p)

#使用lambda表达式为p对象的bar方法赋值（动态增加方法）
p.bar = lambda self:print('--lambda表达式--',self)
p.bar(p)


'''
若希望动态增加的方法自动绑定到第一个参数
借助Types模块下的MethodType进行包装
'''
def intro_func(self,content):
    print("我是一个人，信息为：%s" %content)
from types import MethodType
#使用MethodType对intro_func进行包装，将该函数的第一个参数绑定为p
p.intro = MethodType(intro_func,p)
p.intro("生活在别处")



class Dog:
    def jump(self):
        print("执行jump方法")
    def run(self):
        #必须加self
        self.jump()
        print('执行run方法')
d = Dog()
d.run()


'''
构造方法中，self参数代表构造方法正在初始化的对象
'''
class InConstructor:
    def __init__(self):
        #局部变量
        roo = 0
        #初始化的对象的foo实例变量
        self.foo = 6
print(InConstructor().foo)


'''
自动绑定的self参数不依赖调用形式，下面两个结果一样
'''
class User:
    def test(self):
        print('self参数:',self)
u = User()
u.test()
#变量赋值
foo = u.test
foo()


'''
当self参数作为对象的默认引用时，程序可以像访问普通变量一样来访问这个self参数，甚至
可以把 self 参数当成实例方法的返回值
'''
class ReturnSelf:
    def grow(self):
        #判断一个对象里面是否有age属性或者age方法，
        # 返回BOOL值，有age特性返回True,否则返回False。
        if hasattr(self,'age'):
            self.age += 1
        else:
            self.age = 1
        return self
rs = ReturnSelf()
rs.grow().grow().grow()
print("rs的age属性值是：", rs.age)


























