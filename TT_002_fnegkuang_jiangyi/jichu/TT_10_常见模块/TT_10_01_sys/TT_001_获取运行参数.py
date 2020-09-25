#获取运行参数

'''
通过sys模块的argv属性可获取运行python程序的命令行参数
argv属性值
python   程序名   第一个参数   第二个参数  
        argv[0]    argv[1]      argv[2]
'''

from sys import argv
print(len(argv))
for a in argv:
    print(a)


