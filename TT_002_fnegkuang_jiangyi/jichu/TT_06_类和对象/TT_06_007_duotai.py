#多态


'''
多态性
x指向的对象不同，因此它呈现出不同的行为特征，这就是多态 。
'''
class Bird:
    def move(self,field):
        print('鸟在%s上自由飞翔' %field)
class Dog:
    def move(self,field):
        print('狗在%s上飞快奔跑' %field)
x = Bird()
x.move('天空')
x = Dog()
x.move('草地')



'''

'''
class Canvas:
    def draw_pic(self,shape):
        print('--开始绘图--')
        shape.draw(self)
class Rectangle:
    def draw(self,canvas):
        print('在%s上绘制矩形' %canvas)
class Triangle:
    def draw(self,canvas):
        print('在%s上绘制三角形' %canvas)
class Circle:
    def draw(self,canvas):
        print('在%s上绘制圆形' %canvas)

c = Canvas()
c.draw_pic(Rectangle())
c.draw_pic(Triangle())
c.draw_pic(Circle())




'''
检查类型
issubclass(cls,class_or_tuple)：检查cls是否为后一个类或元组包含的多个勒种任意类的子类
isinstance(cbj,class_or_tuple):检查obj是都为后一个类或元组包含的多个类中任意类的对象

issubclass判断是否为子类
isinstance判断是否为该类或子类的实例
'''
#定义一个字符串
hello = 'hello'
#'hello'是str类的实例，输出True
print('"hello"是否是str类的实例：',isinstance(hello,str))
#'hello'是object类的子类的实例，输出True
print('"hello"是否是object类及其子类的实例：',isinstance(hello,object))
#'str'是object的子类，输出True
print('"str"是否是object的子类',issubclass(str,object))
#'hello'不是tuple类即其子类的实例，输出False
print('"hello"是否是tuple类的实例：',isinstance(hello,tuple))
#str不是tuple类的子类，输出False
print('"str"是否是tuple类的子类：',issubclass(str,tuple))
my_list = [2,4]
#[2,4]是list类的实例，输出True
print('[2,4]是否是list类的实例:',isinstance(my_list,list))
#[2,4]是object类的子类的实例，输出True
print('[2,4]是否是object类及其子类的实例',isinstance(my_list,object))
#list是object类的子类，输出True
print('list是否是object类的子类：',issubclass(list,object))
#[2,4]不是tuple及其子类的实例，输出False
print('[2,4]是否是tuple及其子类的实例',isinstance(my_list,tuple))
#list不是tuple类的子类输出False
print('list是否是tuple类的子类',issubclass(list,tuple))

'''
可使用元组
'''
data = (20,'jj')
print('data是否为列表或元组的实例：',isinstance(data,(list,tuple)))  #True
print('str是否为list或tuple的子类：',isinstance(str,(list,tuple)))  #False
print('str是否为list或tuple或object的子类： ',issubclass(str,(list,tuple,object))) #True

'''
__bases__属性，返回直接父类组成的元组
'''
class A:
    pass
class B:
    pass
class C(A,B):
    pass
print('类A的所有父类：',A.__bases__)
print('类B的所有父类：',B.__bases__)
print('类C的所有父类：',C.__bases__)
print('类A的所有子类：',A.__subclasses__())
print('类B的所有子类：',B.__subclasses__())





