#os模块代表了程序所在的操作系统，主要用于获取程序运行所在操作系统的相关信息

'''
os.__all__

os.name  返回导入依赖模块的操作系统名称
os.environ  返回在当前系统上所有环境变量组成的字典
os.fsencode(filename)  该函数对类路径（path-like）的文件名进行编码
os.fsdecode(filename)   该函数对类路径（path-like）的文件名进行解码
os.PathLike     这是一个类，代表一个类路径(path-like)对象
os.getenv(key,default=None)     获取指定环境变量的值
os.  

'''


import os
#显示导入依赖模块的操作系统名称
print(os.environ)
#获取PYTHONPATH环境变量的值
print(os.getenv('PYTHONPATH'))
#返回当前系统的登录用户名
print(os.getlogin())
#获取当前进程的父进程ID
print(os.getppid())
#返回房钱系统的cpu数量
print(os.cpu_count())
#返回路径分割符
print(os.sep)
#返回当前系统的路径分隔符
print(os.pathsep)
#返回当前系统的换行符
print(os.linesep)
#返回适合作为加密使用的最多由三个字节组成的bytes对象
print(os.urandom(3))



'''
进程管理函数 用于启动新进程终止已有进程等

''










