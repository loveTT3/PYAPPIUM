#if条件的类型
'''
False None 0 "" () [] {}作为布尔表达式时，会被解释器当Flase处理

'''
s = ""
if s:
    print("s不是空字符串")
else:
    print("s是空字符串")

my_list = []
if my_list:
    print('my_list不是空列表')
else:
    print("my_list是空列表")

my_dict = {}
if my_dict:
    print('my_dict是不是空字典')
else:
    print("my_dict是空字典")


#pass语句
'''
pass语句就是空语句，用于占位，什么都不做
'''
s = 5
if s > 5:
    pass
elif s < 5:
    pass
else:
    pass


#断言
'''

'''
s_age = input("请输入您的年龄：")
age = int(s_age)
assert 20 < age < 80
print("您输入的年龄在20到80之间")






