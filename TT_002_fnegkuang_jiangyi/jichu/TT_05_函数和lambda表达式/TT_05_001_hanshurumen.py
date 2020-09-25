def my_max(x,y):
    z = x if x  > y else y
    return z

def say_hi(name):
    print("===正在执行say——hi（）函数===")
    return name + ", 您 好！"

a = 9
b = 3
result = my_max(a,b)
print(result)
print(say_hi("孙悟空"))


#为函数提供文档
def my_max1(x,y):
    '''
        获取两个数之间的较大的那喝
    '''
    z = x if x  > y else y
    return z

#查看帮助文档
help(my_max)
print(my_max1.__doc__)

#多个返回值
'''
多个返回值会自动封装成元组
'''
def sum_and_avg(list):
    sum = 0
    count = 0
    for e in list:
        #如果e是数值
        if isinstance(e,int) or isinstance(e,float):
            count += 1
            sum += e
    return sum , sum/count
my_list = [20,15,2,8,'a',5.9,-1.8]

#tp = sum_and_avg(my_list)
#print(tp)
'''通过序列解包来获取多个返回值'''
s , avg = sum_and_avg(list)
print(s)
print(avg)



#递归函数，必须向已知方向进行
#计算 已知f(0)=1 f(1)=4    求f(n+2) = 2 * f(n+1) + f(n)
def fn(n):
    if n == 0:
        return 1
    elif n == 1:
        return 4
    else:
        return 2 * fn(n - 1) + fn(n - 2)
print(fn(10))
#计算 已知f(20)=1 f(21)=4   求f(n+2) = 2 * f(n+1) + f(n)
def fnn(n):
    if n == 20:
        return 1
    elif n == 21:
        return 4
    else:
        return fnn(n + 2) - 2 * fnn(n + 1)










