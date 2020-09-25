#创建字典
'''
元组可以作为字典的key，列表不行
'''
scores = {'语文':89,'数学':92,'英语':93}
print(scores)
empty_dict = {}
print(scores)
dict2 = {(20,30):'good',30:'bad'}
print(dict2)
'''
dict()函数创建字典，可传入多个列表或元组作为key——value对，列表和元组只能包含两个元素
不为dict（）函数传参，创建空字典
'''
vegetables = [('calery',1.58),('brocoli',1.29),('lettuce',2.19)]
dict3 = dict(vegetables)
print(dict3)
cars = [['bmw',8.5],['bens',8.3],['AUDI',7.9]]
dict4 = dict(cars)
print(dict4)
'''
为dict指定关键字参数创建字典，此时字典的key不允许使用表达式
其 key 直接写 spinach 、 cabbage，不需要将它们放在寻 ｜ 号中
'''
dict6 = dict(spinach = 1.39,cabbage = 2.59)
print(dict6)


#字典基本用法
scores = {'语文':89}
print(scores['语文'])
scores['数学'] = 97
scores[92] = 5.7
print(scores)
del scores['语文']
del scores['数学']
print(scores)
scores[92] = 22
print(scores)
print('s' in scores)
print(92 in scores)


#字典的常用方法
print(dir(dict))
cars  = {'BMW':8.5,'BEENS':8.3,'Audi':7.9}
print(cars.get('BMW'))
print(cars.get('PORSCHE'))  #返回None
#print(cars['PORSCHE'])  #返回KeyError异常
cars.update({'BMW':4.5,"PORSCHE":9.3})      #更新键值对，若存在key则修改，不存在则添加
cars.clear()    #清空字典
'''
items() keys values 返回值需要list（）函数将它们转换为列表
'''
cars = {'BMW':8.5,'BENS':8.3,'AUDI':7.9}
print(list(cars.items()))
print(list(cars.keys()))
print(list(cars.values())[2])
ims = cars.items()
print(list(ims)[1])
'''
pop()方法获取指定key对应的value并删除这个键值对
'''
cars  =  {'BMW':8.5,'BENS':8.3,'AUDI':7.9}
print(cars.pop('AUDI'))
print(cars)
'''
popitem()方法随机演出字典中的一个key-value对
实际上popitem()弹出的是一个元组
'''
k,v = cars.popitem()
print(k,v)
'''
setdefault()方法根据key获取对应的value值
额外的功能一－当程序要获取的key 在字典中不存在时，该方法会先为这个不存在的 key 设置一个默认的 value ， 然后
再返回该 key 对应的 value 
'''
cars = {'BMW': 8.5,'BENS': 8.3,'AUDI ': 7.9}
#设置默认值，该 key 在 diet 中不存在 ， 新增 key-value 对
print(cars.setdefault('PORSCHE',9.2))
print(cars)
print(cars.setdefault('BMW',3.4))
print(cars)
'''
fromkeys()使用给定的多个key创建字典，key对应的value都为None
'''
a_dict = dict.fromkeys(['a','b'])
print(a_dict)
b_dict = dict.fromkeys((13,17))
print(b_dict)
c_dict = dict.fromkeys((13,17),'good')    #创建包含两个key的字典，置顶默认的value
print(c_dict) 


#使用字典格式化字符串
temp = '书名是：%(name)s,价格是:%(price)010.2f,出版社是：%(publish)s'
book = {'name':'三毛','price':22.2,'publish':'文学'}
print(temp % book)




