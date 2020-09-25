#生成器：该生成器可按顺序返回52张扑克牌  分别是四色的2-A

'''
创建生成器需要两步操作
    1.定义一个包含yield语句的函数
            》每次返回一个值，类似return语句
            》冻结执行，每次执行到yeild语句被暂停
    2.调用第2步创建的函数得到生成器
特点：只有通过next()函数调用生成器或遍历生成器时，函数才会真正的执行
'''


def card_generator():
    nums = 52
    flowers = ('@','#','$','%')
    values = ('2','3','4','5','6','7','8','9','10','J','Q','K','A')
    for i in range(nums):
        yield flowers[i // 13] + values[i % 13]

if __name__ == '__main__':
    cg = card_generator()
    print(next(cg))
    print(next(cg))
    for i in cg:
        print(i,end = ' ')


