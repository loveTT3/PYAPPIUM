#python的序列可包含多个元素


#序列相关方法
'''
__len__(self):该方法返回只决定序列中元素的个数
__getitem__(slef,key)：该方法获取指定索引对应的元素，key是整数值或slice对象，否则引发KeyError异常
__contains__(self,item)   判断是否包含指定元素
__setitems__(slef,key,value)  设置指定索引对应的元素  key是整数值或slice对象 否则KeyError异常
__delitems__(self,key)  删除指定索引对应的元素
'''

def check_key(key):
    if not isinstance(key,int):
        raise TypeError('索引必须是整数')
    if key < 0:
        raise IndexError('索引值必须是非负整数')
    if key >= 26 ** 3:
        raise IndexError('索引值不能超过%d' %26**3)
class StringSeq:
    def __init__(self):
        #用于存储被修改的数据
        self.__changed = {}
        #用于存储已删除元素的索引
        self.__deleted = []
    def __len__(self):
        return 26 ** 3
    def __getitem__(self,key):
        check_key(key)
        if key in self.__changed:
            return self.__changed[key]
        if key in self.__deleted:
            return None
        #否则按照规则返回序列元素
        three = key // (26 * 26)
        two = (key - three * 26 *26) // 26
        one = key % 26
        return chr(65 + three) + chr(65 + two) + chr(65 + one)
    def __setitem__(self,key,value):
        check_key(key)
        self.__changed[key] = value
    def __delitem__(self,key):
        check_key(key)
        if key not in self.__deleted:
            self.__deleted.append(key)
        if key in self.__changed:
            del self.__changed[key]
sq = StringSeq()
print(len(sq))
print(sq[26*26])
print(sq[1])
sq[1] = 'ss'
print(sq[1])
del sq[1]
print(sq[1])
sq[1] = 'sss'
print(sq[1])