#引发异常
'''
常用语法
1 raise：单独一个raise。该语句引发当前上下文捕获的异常（比如在except中），或默认引发的RuntimeError
2 raise异常类：raise后带一个异常类 该语句引发置顶异常类的默认实例
3 raise异常对象：引发指定的异常对象
'''


#except和raise同时使用
class AuctionException(Exception):
    pass
class AuctionTest:
    def __init__(self,init_price):
        self.init_price = init_price
    def bid(self,bid_price):
        d = 0.0
        try:
            d = float(bid_price)
        except Exception as e:
            print('转换出异常：',e)
        #再次引发自定义异常
            raise AuctionException('竞拍价必须是数值，不能包含其他字符')
        if self.init_price > d:
            raise AuctionException('竞拍价比起拍价低，不允许竞拍')
        initprice = d
def main():
    at = AuctionTest(20.4)
    try:
        at.bid('df')
    except AuctionException as ae:
        print('main函数捕获异常',ae)
main()








