#控制台超市系统
'''
元组代表商品：元素：商品条码、商品名称、商品单价
dict字典代表当前仓库中所有商品，key为商品条码，calue为商品元组
list列表代表用户购物清单，元素：购物明细，每个明细也是list列表
'''
'''
功能：
显示当前超市的商品清单：遍历代表仓库的dict的value（）
显示用户的购物清单：
用户添加购买的商品：
用户修改购买的商品的数量
用户删除已购买的商品：
'''

#定义仓库
respository = dict()
#定义购物清单对象
shop_list = []

#定义一个函数来初始化商品
def init_repository():
    goods1 = ('1000001','红楼梦',88.0)
    goods2 = ('1000002','西游记',23.2)
    goods3 = ('1000003','水浒传',55.5)
    goods4 = ("1000004",'三国',125.7)

    #商品入库（放入dict中），条码为key
    respository[goods1[0]] = goods1
    respository[goods2[0]] = goods2
    respository[goods3[0]] = goods3
    respository[goods4[0]] = goods4

#显示超市商品清单，遍历respository字典
def show_goods():
    print("欢迎光临")
    print("商品清单：")
    print("%13s%40s%10s" %("条码","商品名称","单价"))
    for goods in respository.values():
        print("%15s%40s%12s" % goods)

#显示购物清单，遍历shop_list列表
def show_list():
    print("=" * 100)
    if not shop_list:
        print("还未购买商品")
    else:
        title = "%-5s|%15s|%40s|%10s|%4s|%10s" % \
            ("ID",'条码','商品名称','单价','数量','小计') 
        print(title)
        print("-" * 100)
        #记录总价
        sum = 0
        for i , item in enumerate(shop_list):
            id = i +1
            #获取购物明细的第一个元素 商品条码
            code = item[0]
            #获取商品条码读取商品，在获得商品名称
            name = respository[code][1]
            price = respository[code][2]
            #获取购物明细的第2个元素:商品数量
            number = item[1]
            #购买的单件商品的价格小计
            amount = price * number

            #总计
            sum += amount
            line = "%-5s|%17s|%40s|%12s|%6s|%12s" %\
                (id,code,name,price,number ,amount)
            print(line)
        print("-" * 100)
        print("                          总计：" ,sum)
    print("=" * 100)

#添加购买的商品，在shop_list上添加
def add():
    code = input("请输入条码：\n")
    if code not in respository:
        print("条码错误，从新输入")
        return
    else:             
        goods = respository[code]
        number = input("请输入购买数量：\n")
        shop_list.append([code,int(number)])
        
#修改购买商品的数量，修改shop_list列表元素
def edit():
    id = input("输入要修改的商品的ID：\n")
    index = int(id) - 1
    item = shop_list[index]
    number = input("输入新的购买数量: \n")
    item[1] = int(number)

#删除已购买的商品明细项
def delete():
    id = input("请输入要删除的购物明细id \n")
    index = int(id) -1
    del shop_list[index]

def payment():
    show_list()
    print('\n' *3)
    print("欢迎下次光临")
    #退出程序
    import os
    os._exit(0)

cmd_dict = {'a':add,'e':edit,'d':delete,'p':payment,'s':show_goods}
def show_command():
    cmd = input("请输入操作指令： \n" + 
        "添加（a）  修改（e）   删除（d）  结算（p）  超市商品（s） \n" )
    if cmd not in cmd_dict:
        print("指令有误")
    else:
        cmd_dict[cmd]()

init_repository()
show_goods()
while True:
    show_list()
    show_command()
