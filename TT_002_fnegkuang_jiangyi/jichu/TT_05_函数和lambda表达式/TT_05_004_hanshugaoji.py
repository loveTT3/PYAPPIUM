

#使用函数变量
def pow(base,exponent):
    result = 1
    for i in range(1,exponent+1):
        result *= base
    return result
my_fun = pow
print(my_fun(2,5))




#使用函数作为函数形参
def map(data,fn):
    result = []
    for e in data:
        result.append(fn(e))
    return result
def square(n):
    return n * n
def cube(n):
    return n * n * n
def factorial(n):
    result = 1
    for index in range(2,n+1):
        result += index 
    return result
data = [3,4,9,5,8]
print("原数据：",data)
print(map(data,square))
print(map(data,cube))
print(map(data,factorial))
print(type(map))


#使用函数作为返回值
def get_math_func(type):
    def square(n):
        return n * n
    def cube(n):
        return n * n * n
    def factorial(n):
        result = 1
        for index in range(2 , n + 1):
            result += index
        return result
    if type == "square":
        return square
    if type == 'cube':
        return cube
    else:
        return factorial
math_func = get_math_func("cube")
print(math_func(5))
math_func = get_math_func('square')
print(math_func(5))
math_func = get_math_func('other')
print(math_func(5))







