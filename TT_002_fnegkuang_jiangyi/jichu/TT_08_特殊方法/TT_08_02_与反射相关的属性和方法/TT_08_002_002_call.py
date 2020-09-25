#call属性

'''
hasattr(obj,name) 检查对象是否包含名为name的属性或方法
call    若包含该方法，则表明可调用
'''

'''
一个函数（甚至对象）之所以能执行，关键就在于__call__()方法
实际上   x(arg1,arg2...)是  x__call__(arg1,arg2)的快捷写法
'''



class User:
    def __init__(self,name,passwd):
        self.name = name 
        self.passwd = passwd
    def validLogin(self):
        print('验证%s的登录' %self.name)
u = User('aa','123')
#判断是否有__call__方法，即判断是否可调用
#包含则可调用   不包含则不可调用
print(hasattr(u.name,'__call__'))
print(hasattr(u.passwd,'__call__'))
print(hasattr(u.validLogin,'__init__'))





'''
自定义添加__call__

'''
class Role:
    def __init__(self,name):
        self.name = name
    def __call__(self):
        print('执行Role对象')
r  = Role('Tom')
#看似错误，因为提供了__call__方法因此调用对象的本质就是执行该对象的__call__方法
r()
r.__call__()











