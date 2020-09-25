#while循环
'''

'''
count_i = 0
while count_i < 10:
    print("count: ",count_i)
    count_i += 1 
print("循环结束")


#使用while循环遍历列表和元组
a_tuple = ('fkit','crazy','charlie')
i = 0
while i < len(a_tuple):
    print(a_tuple[i])
    i += 1

src_list = [12,45,34,13,100,24,56,74,109]
a_list = []
b_list = []
c_list = []
while len(src_list) > 0:
    ele = src_list.pop()
    if ele % 3 == 0:
        a_list.append(ele)
    elif ele %3 ==1:
        b_list.append(ele)
    else:
        c_list.append(ele)
print("整除3： ", a_list)
print("除以3余1： ",b_list)
print("除以3余2： ",c_list)


'''
#for-in循环
s_max = input("请输入您想计算的阶乘：")
mx = int(s_max)
result = 1
for num in range(1,mx+1):
    result *= num 
print(result)
'''

#使用for-in循环遍历列表和元组
a_tuple = ('crazyit','fkit','Charlie')
for ele in a_tuple:
    print(ele)

src_list = [12,45,3.4,13,'a',4,56,'crazyit',109.5]
my_sum = 0
my_count = 0
'''
isinstance（）函数，该函数用于判断某个变量是否为指定类型的实例 ，
其 中前一个参数是要判断的变量，后一个参数是类型
'''
for ele in src_list:
    if isinstance(ele,int) or isinstance(ele,float):
        print(ele)
        my_sum += ele
        my_count += 1
print('总和： ' ,my_sum)
print('平均数： ',my_sum/my_count)

'''
根据索引遍历
'''
a_list = [330,1.4,50,'fkit',-3.5]
for i in range(0,len(a_list)):
    print(a_list[i])


#使用for-in循环遍历字典
'''
items():返回字典中所有的key-value对的列表
keys():返回字典中所有的key列表
values（）：返回字典中多有的value列表
'''
my_dict = {'语文':89,'数学':92,'英语':80}
for key,value in my_dict.items():
    print("key: ",key)
    print("value:",value)
print("---------------")
for key in my_dict.keys():
    print("keys: ",value)
    print("value: ",my_dict[key])
print("----------------")
for value in my_dict.values():
    print("value: ",value)

#嵌套循环
for i in range(0,5):
    j = 0
    while j < 3:
        print("i的值为： %d，j的值为：%d" %(i,j))
        j += 1



#统计列表中各元素出现的次数
src_list = [12,45,3.4,12,'fkit',45,3.4,'fkit',45,3.4]
sta = {}
for ele in src_list:
    if ele in sta:
        sta[ele] += 1
    else:
        sta[ele] = 1
for key , value in sta.items():
    #print(key ," 出现次数： ",value)
    print("%s 出现的次数为： %d" %(key,value))


#for表达式
#利用其它期间、元组、列表等可迭代对象创建新的列表
'''
for表达式方括号生成列表，
'''
a_range = range(10)
#a_list = [x * x for x in a_range]   #对a_range执行for表达式
a_list = [x * x for x in a_range if x %2 == 0]
print(a_list)

'''
for表达式圆括号生成一个生成器（generator）,可使用for循环迭代
'''
c_generator = (x * x for x in a_range if x % 2 == 0)
for i in c_generator:
    print(i , end='\t')

'''
for表达式使用多个循环
'''
d_list = [(x,y) for x in range(4) for y in range(5)]
print(d_list)

dd_list = []
for x in range(4):
    for y in range(5):
        dd_list.append((x,y))

'''
for表达式，指定if条件
'''
src_a = [30,12,66,34,39,78,36,57,121]
src_b = [3,5,7,11]
result = [(x,y) for x in src_b for y in src_a if y % x == 0]
print(result)







