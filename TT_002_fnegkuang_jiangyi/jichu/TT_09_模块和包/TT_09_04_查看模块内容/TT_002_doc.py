#使用__doc__属性查看文档
import string


#help()函数查看的就是程序单元的__doc__属性值
# help(string.capwords)
print(string.capwords.__doc__)

s = string.capwords('aa aa aaa')
print(s)
ss = string.capwords('aa;aa;aa',sep = ';')
print(ss)


print(string.__file__)
