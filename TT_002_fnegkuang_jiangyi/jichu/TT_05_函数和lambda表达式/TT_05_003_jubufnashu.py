


def get_math_func(type,nn):
    #计算平方
    def square(n):
        return n * n
    #计算立方
    def cube(n):
        return n * n * n
    #计算阶乘
    def factorial(n):
        result = 1
        for index in range(2,n+1):
            result *= index
        return result
    if type == 'square':
        return square(nn)
    elif type == 'cube':
        return cube(nn)
    else:
        return factorial(nn)
print(get_math_func('square',3))
print(get_math_func('cube',3))
print(get_math_func("",3))



def foo():
    name = 'mmm'
    def bar():
        #报错
        #print(name)
        name = "孙悟空"
    bar()
foo()

def foor():
    name = 'mmm'
    def bar():
        nonlocal name
        print(name)
        name = '孙悟空'
    bar()
foor()







