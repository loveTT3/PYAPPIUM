#迭代器：返回1,1+2,1+2+3.。。的累积和




class Sums:
    def __init__(self,len):
        self.current_index = 1
        self.current_value = 0
        self.__len = len
    #迭代器所必须的next方法
    def __next__(self):
        #如果__len__长度为0 那么迭代结束
        if self.__len == 0:
            raise StopIteration
        self.current_value += self.current_index
        self.current_index += 1
        self.__len -= 1
        return self.current_value
    def __iter__(self):
        return self
s = Sums(4)
print(next(s))
for  el in s:
    print(el,end=' ')







