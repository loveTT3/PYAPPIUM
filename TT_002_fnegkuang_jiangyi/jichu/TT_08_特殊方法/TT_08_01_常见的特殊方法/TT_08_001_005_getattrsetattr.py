#__getattr__  __setattr__

'''
当程序操作（访问设置删除）对象的属性时，方法如下：
__getattribute__(self,name)  访问对象的name属性时被自动调用
__getattr__(self,name)  访问对象的name属性且该属性不存在时被自动调用
__setattr__(self,name,value)  对对象的name属性赋值时被自动调用
__delattr__(self,name)  当程序删除独享的name属性时被自动调用
'''

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def __setattr__(self,name,value):
        print('-------设置%s属性-------' %name)
        if name == 'size':
            self.width,self.height = value
        else:
            self.__dict__[name] = value
    
    def __getattr__(self,name):
        print('-----bubu读取%s属性-----' %name)
        if name == 'size':
            return self.width,self.width
        else:
            raise AttributeError
    def __delattr__(self,name):
        print('------删除%s属性------'  %name)
        if name == 'size':
            self.__dict__['width'] = 0
            self.__dict__['height'] = 0

rect = Rectangle(3,4)
print(rect.size)
rect.size = 6,8
print(rect.width)
del rect.size
print(rect.size)




#
class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    #重写__setattr__()方法对设置的属性值进行检查
    def __setattr__(self,name,value):
        if name == 'name':
            if 2< len(value) <=8 or len(value) >8:
                self.__dict__['name']= value
            else:
                raise ValueError('value的长度必须在2~8之间')
        elif name == 'age':
            if 10 < value <60:
                self.__dict__['age'] = value
            else:
                raise ValueError('age的值必须在10——60之间')
u = User('Tom',22)
print(u.name)
print(u.age)
# u.age = 2  #引发异常
# u.name = 'aa'  #引发异常



















