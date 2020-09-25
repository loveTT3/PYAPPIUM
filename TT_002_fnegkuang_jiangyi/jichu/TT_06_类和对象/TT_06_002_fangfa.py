'''
方法
'''

def foo():
    print("全局控件的foo方法")
bar = 20
class Bird:
    def foo():
        print("Bird控件的foo方法")
    bar = 200
    def foo1(self):
        print("有参数的foo方法")
#调用全局控件的函数和变量
foo()
print(bar)
#调用Bird空间的函数和变量
Bird.foo()
print(Bird.bar)
#手动为方法的第一个参数传入参数值，完全等同于bird.foo1()
bird = Bird()
Bird.foo1(bird)
#当通过 User 类调用 wa l k（）实例方法时
# Python 只要求手动为第一个参数绑定参数值，并不要求必须绑定 User 对象
Bird.foo1('sf')



'''
类方法和静态方法
'''
class Bird1:
    #使用@classmethod修饰的方法是类方法
    @classmethod
    def fly(cls):
        print('类方法fly:',cls)
    #使用@staticmethod修饰的方法为静态方法
    @staticmethod
    def info(p):
        print('静态方法info',p)
#调用类方法，Bird类会自动绑定到第一个参数
Bird1.fly()
#调用静态方法，不会自动绑定，需手动绑
Bird1.info('sf')

bb = Bird1()
#使用对象调用fly方法，依然可使用类调用
bb.fly()
#对象调静态方法，可是类调用
bb.info('sf')


'''
@函数装饰器
被修饰的函数总是被替换成@符号所引用的函数的返回值，因此被修饰的函数会变成什
么，完全由于@符号所引用的函数的返回值决定
'''
def funA(fn):
    print('A')
    fn()
    return 'sf'
#将funB作为funA()的参数，也就是下面的@funA代码相当于执行funA(funB) 
@funA
def funB():
    print("B")
#funA()执行完后返回sf，因此funB不再是函数，而被替换成字符串
print(funB)


def foo2(fn):
    def bar(*args):
        print('===1===',args)
        n = args[0]
        print('===2===',n*(n-1))
        print(fn.__name__)
        fn(n*(n-1))
        print('*'*15)
        return fn(n*(n-1))
    return bar
@foo2
def my_test(a):
    print('==my_test==',a)
print(my_test)
my_test(10)
my_test(6,5)


def auth(fn):
    def auth_fn(*args):
        print('-----模拟执行权限检查-----')
        fn(*args)
    return auth_fn
@auth
def test(a,b):
    print('执行test函数，参数a：%s,参数b:%s' %(a,b))
test(20,15)



































