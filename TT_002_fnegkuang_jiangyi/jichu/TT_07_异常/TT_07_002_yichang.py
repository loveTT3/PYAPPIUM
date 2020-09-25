#异常
'''
所有异常的基类都是BaseException
BaseException的主要子类就是Exception 不管是用户自定义异常类还是系统的异常类，都从Exception诞生
但用户要实现自定义异常，则应该继承Exception类
'''


'''
sys模块的argv列表获取运行python程序时提供的参数
通常:sys.argv[0]代表正在运行的Python程序名
sys.argv[1]代表运行程序所提供的第一个参数
sys.aargv[2]代表运行程序所提供的第二个参数。。以此类推
'''
import sys
try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = a/b
    print('您输入的两个数相除的结果是：',c)
except IndexError:
    print('索引错误，运行程序时输入的参数个数不够')
except ValueError:
    print('数值错误，程序只能接受整数参数')
except ArithmeticError:
    print('算术错误')
except Exception:
    print('位置异常')



#多异常捕获
'''
使用一个except块捕获多种异常，将多个异常类用圆括号括起来，中间逗号隔开，元组
'''
import sys
try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = a/b
    print('两数相除结果是：',c)
except(IndexError,ValueError,ArithmeticError):
    print('程序发生索引异常，数字格式异常，算式异常之一')
except:
    print('未知异常')



#访问异常信息
'''
args:该属性返回异常的错误编号和描述字符串
errno：该属性返回异常的错误编号
strerror：该属性返回异常的描述字符串
with_traceback:通过该方法可处理异常的传播轨迹信息
'''
def foo():
    try:
        fis = open('a.txt')
    except Exception as e:
        #访问异常的错误编号和错误信息
        print(e.args)
        #访问异常的错误编号
        print(e.errno)
        #访问异常的错误信息
        print(e.strerror)
        print(e.with_traceback)
foo()


#else块
'''

'''
s = input('请输入除数：')
try:
    result = 20/int(s)
    print('20除以%s的结果是:%g'%(s,result))
except ValueError:
    print('之错误，必须输入数值')
except ArithmeticError:
    print('算术错误，不能输入0')
else:
    print('没有出现异常')



'''
体现else作用
'''
def else_test():
    s = input('请输入除数')
    result = 20/int(s)
    print('20除以%s的结果是：%g'%(s,result))
def right_main():
    try:
        print('try块的代码，没有异常')
    except:
        print('程序出现异常')
    else:
        else_test()
def wrong_main():
    try:
        print('try块的代码没有异常')
        else_test()
    except:
        print('程序出现异常')
# wrong_main()
# right_main()





#使用finally回收资源
'''
有时候，程序在try里打开一些物力资源（例如数据库连接，网络连接和磁盘文件等）这些物理资源都需被显示回收
python的垃圾回收机制不会回收任何物理资源，只能回收堆内存对象所占用的内存
'''
import os
def test():
    fis = None
    try:
        fis = open('a.text')
    except OSError as e:
        print(e.strerror)
        #结束方法
        return
        # os._exit(1)
    finally:
        if fis is not None:
            try:
                fis.close()
            except OSError as ioe:
                print('ioe.strerror')
        print('执行finally块里的资源回收')
test()


































