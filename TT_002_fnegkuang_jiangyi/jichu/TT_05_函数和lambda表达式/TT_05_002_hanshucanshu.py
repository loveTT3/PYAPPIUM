


#关键字参数
'''

'''
def girth(width,height):
    print("width: ",width)
    print("height: ",height)
    return 2 * (width + height)
#传统调用方式，根据位置传参
print(girth(3.5,4.8)) 
#关键字传参
print(girth(width=3.5,height=4.8))
print(girth(height=4.8,width=3.5))
#混合传参
#关键字参数必须位于位置参数之后
print(girth(3.5,height=4.8))



#参数默认值
''''''
def say_hi(name = '孙悟空',message = "欢迎来到花果山"):
    print(name,"你好")
    print('消息是： ',message)
say_hi()
say_hi('白骨精')
say_hi('白骨精','欢迎啊')
say_hi(message = '欢迎')
'''
制定了默认值的参数必须在没有默认值的参数之后
'''
def printTriangle(char,height = 5):
    for i in range(1,height + 1):
        for j in range(height - i):
            print(' ',end='')
        for j in range(2 * i -1):
            print(char,end = '')
        print()
printTriangle('a',6)
printTriangle('#',height=7)
printTriangle(char = '*')


#参数收集（个数可变的参数）
'''
多个参数当成元组传入
可变参数可以在任意位置，但最多只能有一个“普通”形参
'''
def test(a,*books):
    print(books)
    for b in books:
        print(b)
    print(a)
test(5,'三国','西游记')
'''
支持一个普通参数手机的参数和一个支持关键字参数收集的参数
普通参数收集为元组，关键字参数收集为字典
'''
def foo(x,y,z = 3,*books,**scores):
    print(x,y,z)
    print(books)
    print(scores)
foo(1,2,3,'西游记','三国',语文=89,数学=99)


#逆向参数收集
'''
在程序已有列表，元组，字典等对象的前提下，把元素拆开后传给函数的参数
在传入的列表，元组参数前加一个星号，在字典参数前加两个星号
'''
def test2(name,message):
    print("用户是：",name )
    print("欢迎消息",message)
my_list = ['孙悟空','欢迎啊']
dict1 = {'name':123,'message':22}
test2(*my_list)
test2(**dict1)

def test3(name,*nums):
    print(name)
    print(nums)
my_tuple = (1,2,3)
test3('Tom',*my_tuple)
'''
字典，key需要和参数一样
'''
def test4(book,price,desc):
    price(book,'这本书价格是：',price)
    price('描述信息',desc)
my_dict = {'price':55,'book':'红楼梦','desc':'很长很长'}
























#变量作用域
'''
globals() 返回全部范围内所有变量组成的“变量字典”
locals() 返回当前局部范围内所有变量组成的“变量字典”
vars(object) 返回在指定对象范围内所有变量组成的“变量字典”
'''
'''
print(globals())
print('*' * 100)
print(locals())
print('=' * 100)
print(vars(object))
'''

