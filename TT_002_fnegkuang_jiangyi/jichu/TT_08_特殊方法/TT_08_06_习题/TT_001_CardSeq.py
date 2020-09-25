#序列，包含52张扑克牌 分别梅花草花方块红桃2-A
#要求：提供序列的各种操作方法



def check_key(key):
    if not isinstance(key,int):
        raise TypeError('索引值必须为整数')
    if key < 0:
        raise IndexError('索引值必须大于0')
    if key >= 52:
        raise IndentationError('索引值不能超过%d'%52)
class CardSeq:
    def __init__(self):
        self.flowers = ['@','#','$','%']
        self.values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        self.__changed = {}
        self.__deleted = []
    def __setitem__(self,key,value):
        check_key(key)
        self.__changed[key] = value
    def __getitem__(self,key):
        check_key(key)
        if key in self.__changed:
            return self.__changed[key]
        if key in self.__deleted:
            return None
        flower = key // 13
        value = key % 13
        return self.flowers[flower] + self.values[value]
    def __delitem__(self,key):
        check_key(key)
        if key in self.__changed:
            del self.__changed[key]
        if key not in self.__deleted:
            self.__deleted.append(key)
    def __len__(self):
        return 52

if __name__ == '__main__':
    cs = CardSeq()
    print(cs[23])
    cs[23] = 'qqq'
    print(cs[23])
    del cs[23]
    print(cs[23])
    print(cs.__len__())
    print(len(cs))
    print(cs[0])
    print(cs[51])