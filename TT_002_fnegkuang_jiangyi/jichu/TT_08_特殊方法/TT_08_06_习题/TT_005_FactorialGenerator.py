#生成器：可依次返回1234的阶乘

'''
创建生成器需要两步操作
    1.定义一个包含yield语句的函数
            》每次返回一个值，类似return语句
            》冻结执行，每次执行到yeild语句被暂停
    2.调用第2步创建的函数得到生成器
特点：只有通过next()函数调用生成器或遍历生成器时，函数才会真正的执行
'''


def aaa(len):
    a = 1
    for e in range(2,len+1):
        a =  a * e
    print(a)
aaa(10)

def factorial_generator(n):
    a_list = [1]
    for e in range(2,n+1):
        a_list.append(a_list[-1] * e)
    for i in range(n):
        yield a_list[i]
if __name__ == '__main__':
    fg = factorial_generator(10)
    print(next(fg))
    for i in fg:
        print(i,end=' ')