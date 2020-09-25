#自定义一个代表二维坐标系上某个点的Point类（包括x和y两个属性）
#为Point提供自定义的减法运算符支持 计算结果返回两点之间的距离



class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __sub__(self,u):
        if not isinstance(u,Point):
            raise TypeError('必须是对象')
        return(((self.x-u.x)**2 + (self.y-u.y)**2 )** 0.5)

if __name__ == '__main__':
    p1 = Point(5,5)
    p2 = Point(3,5)
    print(p2-p1)











