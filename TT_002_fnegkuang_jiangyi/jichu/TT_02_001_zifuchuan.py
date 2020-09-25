import time

str1 = "    I'm a coder   "
str2 = 'i ''m' #拼接字符串
print(str2)


#大小写相关方法
print(str1.title())
print(str1.lower())
print(str1.upper())


#删除空白
print(str1.lstrip())    #左边
print(str1.rstrip())    #右边
print(str1.strip())     #前后的空白


#查找、替换相关方法
s = 'crazyit.org is a goood site'
print(s.startswith('cra'))  #是否已‘cra’开头
print(s.endswith('ite'))     #是否已‘ite’结尾
print(s.find('org'))    #寻找出现的位置
print(s.index('org',3))  #从索引3开始查找‘org’出现的位置
print(s.replace('it','xxxx'))    #将it换位xxx

#自定义映射表
table={97:945,98:946,116:964}
table1=str.maketrans('org','nbb') 
print(str.maketrans('org','nbb'))    #将o换为n  rg换为bb
print(s.translate(table1))


#分割、连接方法
ss = 'crazeit.org is a good site'
print(ss.split())   #用空白对字符串分割
print(ss.split(None,2))   #使用空b白分割，最多分割前两个单词
print(ss.split('.'))    #使用.分割
mylist = ss.split()
print('/'.join(mylist))     #使用/作为分隔符，将mylist连接成字符串

#索引运算符
a = 'abcdefghijklmnopqretuvwxyz'
print(a[2:8:3])     #获取索引2-8的子串 步长为3


#is   is not 判断两个变量所引用的对象是否相同
a = time.gmtime()
b = time.gmtime()
print(a == b)
print(a is b)    #两个变量引用对象是否相同
#全局id（）显示对象的内存地址
print(id(a))
print(id(b))
