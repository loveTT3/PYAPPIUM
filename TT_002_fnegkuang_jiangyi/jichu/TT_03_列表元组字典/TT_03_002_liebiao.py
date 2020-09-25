#创建列表
'''
1.使用方括号语法创建
2.使用list()函数来创建     同样的，还有tuple()函数
3.list（），tuple()两个方法最多只能有一个元素
'''
# a_tuple = ('crazyit',20,-1.2)
# a_list = list(a_tuple)
# print(a_list)
# a_range = range(10)
# b_list = list(a_range)
# print(b_list)
# c_list = list(range(1,10,2))
# print(c_list)
a_list = ['crazyit',20,-1.2]
a_tuple = tuple(a_list)
print(a_tuple)
a_range = range(10)
b_tuple = tuple(a_range)
print(b_tuple)
c_tuple = tuple(range(1,10,2))
print(c_tuple)



#增加列表元素
'''
append()方法,可接收元组列表等
'''
a_list = ['crazyit',20,-2]
a_list.append('fkit')
a_tuple = (3.4,5.6)
a_list.append(a_tuple)
print(a_list)
a_list.append(['aaa','b'])
a_list.append(tuple('nb'))
print(a_list)
'''
extend()方法,只追加列表中的元素，不把追加的列表当成一个整体
'''
b_list = ['a','b']
b_list.extend(['1',22])
b_list.extend(range(12))
print(b_list)
'''
insert()方法将指定元素插入列表指定位置
'''
c_list = list(range(1,6))
print(c_list)
c_list.insert(3,'crazy')     
print(c_list)       # [l, 2 , 3,’ CRAZY ’ , 4 , SJ
c_list.insert(3,tuple('crazy'))
print(c_list)       #[1 , 2 , 3 , (’ c '.,’ r ’,’ a ’,’ z ’ , ’ Y’ ),’ CRAZY ’ , 4 , SJ


#删除
'''
del()语句,按索引删除，可删除列表元素，也可删除变量
'''
a_list = ['crazyit',20,-2.4,(3,4),'fkit']
del a_list[2]
print(a_list)
del a_list[1:3]     #删除第2个到第4个（不包含）
print(a_list)
b_list = list(range(1,10))
del a_list[2:-2:2]
print(b_list)
del b_list[2:4]
print(b_list)
'''
remove()，根据元素本身执行删除操作，只删除第一个找到的元素，若找不到，则引发ValueError错误
'''
c_list = [20,'crazyit',30,-4,'crazyit',3.4]
c_list.remove(30)
c_list.remove('crazyit')
print(c_list)
'''
clear()，清空列表所有元素
'''
c_list.clear()
print(c_list)



#修改列表元素
a_list = [2,4,-3.4,'crazyit',23]
a_list[2] = 'fkit'
a_list[-2] = 9527
print(a_list)
'''
slice语法，不要求新赋值的元素个数与原来元素个数相等
即：可为列表增加元素，也可为列表删除元素
'''
b_list = list(range(1,5))
print(b_list)
b_list[1:3] = ['bui','c']
print(b_list)
b_list[3:3] = [1,'a','x','y','b',4]     #为列表插入元素
print(b_list)
b_list[2:5] = []    #从列表中删除元素
'''
使用slice语法赋值时，不能使用单个值，如果使用单个字符串赋值，则自动当成序列处理
每个字符都是一个元素
'''
b_list[1:3] = 'Charlie'
print(b_list)
'''
使用slice语法,可指定步数，但指定步数之后，需要被赋值的和赋值的元素个数相等
'''
c_list = list(range(1,10))
c_list[2:9:2] = ['','',c_list[1:6],'']
print(c_list)

#常用方法
'''
count():统计列表中元素出现的次数
'''
a_list = [2,30,'a',[5,30],30]
print(a_list.count(30))
'''
index()：判断元素在列表中出现的位置，若没有出现，返回ValueError错误
可传入start，end参数，指定搜索范围
'''
a_list = [2,30,'a','b','crazyit',30]
print(a_list.index(30))
print(a_list.index(30,2))   #从索引2开始定位元素位置，返回5
#print(a_list.index(30,2,4))     #从缩影2到4之间定位元素30出现的位置
'''
pop()实现元素出栈,即移出最后一个元素
'''
stack = []
stack.append('fkit')
stack.append('crazyit')
stack.append('Charlie')
print(stack)
print(stack.pop())
print(stack)
'''
reverse()反转列表中所有元素
'''
a_list = list(range(1,8))
a_list.reverse()
print(a_list)
'''
sort()将列表进行排序
'''
a_list = [3,4,-2,-30,14,9.3,3.4]
a_list.sort()   #按大小排
print(a_list)
b_list = ['Python','Swift','Ruby','Go','Kotlin','Erlang']
b_list.sort()   #按字符编码
print(b_list)
'''
key 参数用于为每个元素都生成
一个比较大小的“ 键”； reverse 参数则用于执行是否需要反转排序一－－默认是从小到大排序；如果
将该参数设为 True ，将会改为从大到小排序 。
'''
b_list.sort(key = len)
print(b_list)
b_list.sort(key = len , reverse = True)
print(b_list)



