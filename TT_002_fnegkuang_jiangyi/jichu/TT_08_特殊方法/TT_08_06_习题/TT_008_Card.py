#自定义代表扑克牌的Card类
#提供：比较大小的运算符支持  标准  先比片面值再比花色 @#￥%



flowers = ('@','#','$','%')
values = ('2','3','4','5','6','7','8','9','10','J','Q','K','A')
class Card:
    def __init__(self,flower,value):
        self.flower = flower
        self.value = value
    def __gt__(self,other):
        if not isinstance(other,Card):
            raise TypeError('必须是对象')
        if values.index(self.value) > values.index(other.value):
            return True
        elif values.index(self.value) == values.index(other.value) and flowers.index \
            (self.flower) > flowers.index(other.flower):
            return True
        else:
            return False











