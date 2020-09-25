'''
lambda表达式格式：
    lambda [parameter_list] : 表达式
要点：
    lambda必须使用lambda关键字定义
    lambda之后，冒号左边时参数列表，可没有参数，可以有多个参数，若有多个，用逗号隔开
'''

import string
def get_math_func(type):
    # result = 1
    #该函数的返回时lambad表达式
    if type == "square":
        return lambda n : n * n
    elif type == 'cube':
        return lambda n : n * n * n
    else:
        return lambda n : (1 + n)  * n / 2
#调用get_math_func,程序返回一个嵌套函数
math_func = get_math_func('cube')
print(math_func(5))
math_func = get_math_func('square')
print(math_func(5))
math_func = get_math_func('other')
print(math_func(5))




















