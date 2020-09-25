


def test5():
    age =20 
    print(age)
    #访问局部范围的“变量数组”
    print(locals())
    print(locals()['age'])
    locals()['age'] = 12
    print('xxx',age)
    globals()['x'] = 19
x = 5
y = 20
print(globals())
print(locals())
print(x)
print(globals()['x'])
globals()['x'] = 39
print(x)
locals()['x'] = 99
print(x)



name = 'charlie'
def test():
    print(name)
    #添加以下代码报错，局部变量遮蔽了全局变量
    #name = '孙悟空'
test()
print(name)

#解决办法一 访问被遮蔽的全局变量
def test2():
    print(globals()['name'])
    name = '孙悟空'
test2()
print(name)
#解决办法二 在函数张声明全局变量
def test3():
    global name
    print(name)
    name = '孙悟空'
test3()
print(name)



