#导入模块的语法


'''
import 
from import
'''

import sys
#sys下的argv变量用于获取运行python程序的命令行参数  
#argv[0]用于获取python程序的程序名
print(sys.argv[0])

import sys as s, os as o
print(s.argv[0])
#os吓得sep变量代表平台上的路径分隔符
print(o.sep)

from sys import argv as v,winver as a
print(v[0])
print(a)


