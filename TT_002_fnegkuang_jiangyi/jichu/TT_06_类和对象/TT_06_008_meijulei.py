#枚举类
'''
实例有限且固定的类，在python中被称为美剧类
'''


'''
枚举入门
》直接使用Enum列出多个枚举值来创建枚举类
》通过集成Enum基类派生枚举类
'''
#直接使用Enum列出枚举值创建枚举类
#Enum()函数就是Enum的创造方法，第一个参数是枚举类的类名，第二个参数是元组，列出所有枚举值
import enum
Season = enum.Enum('Season',('Spring','summer','fall','winter'))
#直接访问指定枚举
print(Season.Spring)
#访问枚举成员的变量名
print(Season.Spring.name)
#访问指定枚举的值
print(Season.Spring.value)
#根据枚举变量名访问枚举对象
print(Season['summer'])
#根据枚举值访问枚举对象
print(Season(3))
#遍历Season枚举的所有成员
for name , member in Season.__members__.items():
    print(name,'>=',member,',',member.value)

'''
集成Enum来派生枚举类，这样可以为枚举额外定义方法
'''
import enum
class Orientation(enum.Enum):
    #为序列指定value值
    EAST = '东'
    SOUTH = '南'
    WEST = '西'
    NORTH  = '北'
    def info(self):
        print('这是一个代表方向【%s】的枚举'%self.value)
    print(Orientation.SOUTH)
    print(Orientation.SOUTH.value)
    #通过枚举变量名访问枚举
    print(Orientation['WEST'])
    #通过枚举值来访问枚举
    print(Orientation('南'))        
    #调用枚举的info（）方法
    Orientation.info()
    #遍历Orientation枚举的所有成员
    for name,member in Orientation.__members__.items():
        print(name,"=>",member,',',member.value)



'''
枚举的构造器
'''
















