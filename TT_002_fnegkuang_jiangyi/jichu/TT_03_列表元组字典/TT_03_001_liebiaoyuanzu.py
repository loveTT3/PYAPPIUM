#创建列表
my_list = ['crazy',20,'Python']
#创建元组
my_tuple = ('crazy',20,'Python')

#列表元组通用用法
#打印
a_tuple = ('crazy',20,5.6,'fkit',-17)
print(a_tuple)     #打印元组
print(a_tuple[1])
print(a_tuple[-3])

#切片(包前不包后)
print(a_tuple[1:3])     #20,5.6
print(a_tuple[1:-2])
print(a_tuple[0:8:2])    #访问第三个到第九个，间隔为2

#加法
'''
和是两个列表或者元组包含的元素的总和
列表只能和列表相加，元组只能和元组相加
'''
a_tuple = ('crazy',20,-1.2)
b_tuple = (127,'crazy','fkit',3.33)
print(a_tuple+b_tuple)
a_list = [20,30,50,100]
b_list = ['a','b',11]
print(a_list + b_list)

#乘法
'''
列表和元组可以和整数进行乘法运算
意义：把包含的元素重复N次
'''
a_tuple = ('crazy',22)
print(a_tuple*3)
a_list = [30,'Python']
print(a_list*2)


#把用户输入的日期翻译成英文表达方式
#('st')只是字符串加上括号，不是元组,('st',)表示只有一个元素的元组
'''
order_endings = ('st','ne','rd')\
    +('th',) * 17 + ('st','nd','rd') + ('th',) * 7 +  ('st',)
day = input("请输入日期(1-31)： ")
day_int = int(day)
print(day + order_endings[day_int-1])
'''


#in运算符
print(22 in a_tuple)
print(22 not in a_tuple)

#长度
print(len(a_list))

#最大值#最小值，需可比较
a_tuple = (20,10,-2,15.2,102,50)
print(max(a_tuple))
b_list = ['crazy','fkit','Python']
print(min(b_list))


#序列封包
'''把多个值赋给变量时，自动封装成元组'''
vals = 10,20,30
print(vals)
print(type(vals))
#序列解包
'''将序列（元组或列表等）直接赋值给变量，此时元素会一次赋值给每个变量（要求元素个数和变量个数相等）'''
a_tuple = tuple(range(1,10,2))
print(a_tuple)
a,b,c,d,e = a_tuple
print(a,b,c,d,e)
#解包只解出部分变量,变量前加* 代表列表
first,second,*rest = range(1,10)
print(str(first) + "---" + str(second)+ "---" +str(rest))
*begin,last = range(1,10)
print(str(begin) + "---" + str(last))
first,*middle,last = range(10)
print(str(first) + "---" + str(middle) + "---" + str(last))