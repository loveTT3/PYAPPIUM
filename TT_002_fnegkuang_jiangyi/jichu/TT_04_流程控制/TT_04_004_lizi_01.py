
#数字转人民币读法

'''
把一个浮点数分解成整数和小数部分字符串
num是需要被分解的浮点数
返回分解的整数部分和小数部分
第一个数组是整数，第二个数组是小数
'''

def divide(num):
    #整数部分
    integer = int(num)
    print(integer)
    #小数部分 
    franction = round((num - integer)*100)
    return (str(integer) , str(franction))

han_list = ["零",'壹','贰','叁','肆','伍','陆','柒','捌','玖']
unit_list = ["十",'百','千']

def four_to_hanster(num_str):
    result = ""
    num_len = len(num_str)
    for i in range(num_len):
        num = int(num_str[i])
        if i != num_len -1 and num != 0:
            result += han_list[num] + unit_list[num_len-2-i]
        else:
            result += han_list[num]
    return result

def integer_to_str(num_str):
    str_len = len(num_str)
    if str_len > 12:
        print('数字太大，翻译不了')
        return
    elif str_len > 8:
        return four_to_hanster(num_str[:-8]) + '亿' + \
            four_to_hanster(num_str[-8:-4]) + '万' + \
            four_to_hanster(num_str[-4:])
    elif str_len > 4:
        return four_to_hanster(num_str[:-4]) + '万' +\
            four_to_hanster(num_str)
    else:
        return four_to_hanster(num_str)
num = float(input('输入数字'))
integer,fraction = divide(num)
print(integer_to_str(integer))
#print(integer)
print(fraction)


