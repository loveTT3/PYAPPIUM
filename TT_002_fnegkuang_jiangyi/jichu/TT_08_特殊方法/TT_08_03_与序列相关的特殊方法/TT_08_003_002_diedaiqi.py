#迭代器

'''
开发者需要实现迭代器，需实现两个方法
__iter__(self):   该方法返回一个迭代器（iterator） 
迭代器必须返回一个__next__()方法  
                该方法返回迭代器的下一个元素
__recersed__(self):  为内建的recersed()反转函数提供支持  当程序调用reversed()函数对
                    指定迭代器执行反转时  实际上由该方法实现
'''


'''
f(n+2) = f(n+1) + f(n)
'''
#定义一个斐波那契数列的迭代器
class Fibs:
    def __init__(self,len):
        self.first = 0
        self.sec=1
        self.__len = len
    def __next__(self):
        if self.__len ==0:
            raise StopIteration
        self.first,self.sec = self.sec,self.first + self.sec
        self.__len -=1
        return self.first
    def __iter__(self):
        return self
fibs = Fibs(10)
print(next(fibs))
for  el in fibs:
    print(el,end=' ')





