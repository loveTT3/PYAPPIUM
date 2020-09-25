#序列：100 - 999 
#要求：提供序列各种操作方法


start = 100
end = 999
num = end - 100 +1
def check_key(key):
    if not isinstance(key,int):
        raise TypeError('索引必须是整数')
    if key < 0:
        raise IndexError('索引必须大于0')
    if key >= num:
        raise IndexError('索引必须小于%d'%num)
def check_value(value):
    if not isinstance(value,int):
        raise TypeError('值必须输数字')
    if value > end or value < start:
        raise IndexError('值必须在 %d 和 %d 之间'%(start,end))
class NumSeq:
    def __init__(self):
        self.__changed = {}
        self.__deleted = []
    def __len__(self):
        return num
    def __getitem__(self,key):
        check_key(key)
        if key in self.__changed:
            return self.__changed[key]
        if key in self.__deleted:
            return None
        return start + key
    def __setitem__(self,key,value):
        check_key(key)
        check_value(value)
        self.__changed[key] = value        
    def __delitem__(self,key):
        if key in self.__changed:
            del self.__changed[key]
        if key not in self.__deleted:
            self.__deleted.append(key)

if __name__ == '__main__':
    ns = NumSeq()
    print(ns[899])
    print(len(ns))
    print(ns[0])
    ns[0] = 222
    print(ns[0])
    del ns[0]
    print(ns[0])


