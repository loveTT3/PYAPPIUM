#隐藏和封装
#只要将Python类的成员命名为以双下画线开头的，Python 就会把它们隐藏起来 。


class User:
    def __hide(self):
        print('示范影藏的hide方法')
    def getname(self):
        return self.__name
    def setname(self,name):
        if len(name) < 3 or len(name) > 8:
            raise ValueError('用户名长度必须在3-8之间')
        self.__name = name
    name  = property(getname,setname)
    def setage(self,age):
        if age < 18 or age >70:
            raise ValueError('用户名年龄必须在18-70之间')
        self.__age = age
    def getage(self):
        return self.__age
    age = property(getage,setage)
u = User()
#u.name = 'fwk'
u.name = 'ioio'
u.age = 25
print(u.name)
print(u.age)

#Python 会 “偷偷”地 改变 以双下画线开头的方法名，会在这些方法名前添加单下画线和类名 。 
#此上面的一hide（）方法其实可以按如下方式调用（通常并不推荐这么干）。
u._User__hide()
#对User对象的name实例变量进行赋值，
# 通过这种方式可“绕开”setname（）方法的检查逻辑，直接对User对象的name属性赋值
u._User__name = 'io'
print(u.name)
























