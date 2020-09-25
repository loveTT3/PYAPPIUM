#zip()函数
'''
zip()把N个列表压缩成一个zip对象（可迭代对象）
如果两个列表长度不相等 以短的为标准
'''
a = ['a','b,','c']
b = [1,2,3]
c = [x for x in zip(a,b)]
print(c)

'''

'''
books = ['aaa','bbb','ccc']
price = [21,22,34]
for book ,price in zip(books,price):
    print("%s的价格是：%5.2f"%(book,price))

#sorted()函数
my_list = ['fkit','crazy','Charlie','fox','Emlily']
for s in sorted(my_list,key = len):
    print(s)


#使用break结束循环
for i in range(0,10):
    print("i的值是：",i)
    if i == 2:
        break
    else:
        print('else块：',i)

#使用continue忽略本次循环
for i in range(0,3):
    print('i的值是：',1)
    if i == 1:
        continue
    print("continue后的输出语句")

#使用return结束方法
def test():
    for i in range(10):
        for j in range(10):
            print('i的值是：%d,j的值是：%d'%(i,j))
            if j == 1:
                return
            print('return后的输出语句')
test()















