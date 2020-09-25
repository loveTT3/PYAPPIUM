#sys模块代表了Python解释器
#主要用于获取和Python解释器相关的信息

import sys
'''
常见模块
sys.argv:获取运行python程序的命令行参数，sys.argv[0]通常指python程序  [1]代表为python程序提供的第一个参数
sys.byteorder:显示本地字节序的指示符。如果本地字节序是大端模式，返回big，否则返回little
sys.copyright:该属性返回与python解释器有关的版权信息
sys.executable:该属性返回Python解释器在磁盘上的存储路径
sys.exit():通过引发SystemExit异常来退出程序，放在try块中不能阻止finally的执行
sys.flags:该只读属性返回运行python命令时指定的旗标
sys.getfilesystemencoding()：返回当前系统保存文件所用的字符集
sys.getrefcount(object):返回指定对象的引用次数
sys.getrecursionlimit():返回python解释器当前支持的递归深度，该属性可通过setrecursionlimit()函数改变
sys.getswitchinterval():返回在当前python解释器中线程切换的时间间隔 可通过setwitchinterval()函数改变
sys.implementation:返回当前python解释器的实现
sys.maxsize：返回python整数支持的最大值 32位平台值为2**31-1  64位平台为2**63-1
sys.modules:返回模块名和载入模块对应关系的字典
sys.path:该属性指定python查找模块的路径列表。可通过修改属性来动态增加python加载模块的路径
sys.platform:返回python解释器所在平台的标识符
sys.stdin:返回系统的标准输入流--一个类文件对象
sys.stdout:返回系统的标准输出流--一个类文件对象
sys.stderr:返回系统的错误输出流--一个类文件对象
sys.version:返回当前python解释器的版本信息
sys.winver:返回当前python解释器的主版本号
'''

#显示本地字节序的指示符
print(sys.byteorder)
#显示与python解释器有关的版权信息
print(sys.copyright)
#显示python解释器在磁盘上的存储路径
print(sys.executable)
#显示在当前系统中保存文件所用的字符集
print(sys.getfilesystemencoding())
#显示python整数支持的最大值
print(sys.maxsize)
#显示python解释器所在的平台
print(sys.platform)
#显示当前python解释器的版本信息
print(sys.version)
#返回当前python解释器的主版本号
print(sys.winver)