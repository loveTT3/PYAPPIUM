#生成器：依次访问千米那目录下的所有Python源文件（以.py为后缀的文件）





import os
def files_generator():
    for i in os.listdir(r'.'):
        yield i
if __name__ == '__main__':
    fg = files_generator()
    print(next(fg))
    for i in fg:
        print(i,end = ' ')
    






