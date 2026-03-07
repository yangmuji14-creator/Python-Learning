# 函数的参数类型:
# 1.普通参数：数字，布尔，字符串，列表，元组，集合，字典等。
# 2.特殊参数：函数。

# 加
# def add(x,y):
#     return x + y
#
# # 减
# def substruct(x,y):
#     return x - y
#
# # 乘法
# def multiply(x,y):
#     return x * y
#
# # 除法
# def divide(x,y):
#     return x / y
#
# # 运算
# def calc(x,y,oper):
#     return oper(x,y)
#
# z = calc(10,20,multiply)
# print(z)



# 匿名函数(lambda)：匿名函数指的是没有名称的函数，需要通过lambda表达式来声明函数，可以简化简单函数的编写（单行表达式）。
# 注意：1.函数逻辑比较简单（单行表达式）且只在一个地方使用时，可以考虑使用匿名函数，简化书写（通常作为高阶函数的参数使用）
#      2.匿名函数中可以返回结果，也可以不返回结果。返回结果时，不需要写return，表达式的运行结果就是要反回的结果。


# 需求1：打印一个分割线
# def outline():
#     print("-------------------------")

outline = lambda : print("----------------------------")
outline()


# 需求2：计算两个数之和
# def add(x,y):
#     return x + y

# add = lambda x,y: x + y
# c = add(100,200)
# print(c)



# 需求3：完成如下列表的排序操作，按照每一个元素的字符个数，从小到大排序；
# data_list = ["C++","C","Python","Jack","Java","JavaScript","Go","Rust"]
# print(data_list)
# data_list.sort()
# print(data_list)
# data_list.sort(key=lambda item : len(item))
# print(data_list)


# 命名函数与匿名函数的选择？
# ·建议使用匿名函数的情况：函数逻辑很简单，只在一个地方调用（常作为高阶函数的参数）
# ·建议使用命名函数的情况：函数逻辑复杂，需要多步操作，需要多个地方重复使用或需要加文档说明的场景




# ------------------------------------------------- 案例 ---------------------------------------------
# 案例1：计算n的阶乘
# 递归调用：函数中自己调用自己的情况 ----> 一定得有终结点

# def dg(x):
#     if x == 1:
#         return 1
#     else:
#         return x * dg(x - 1)
#
# print(dg(4))




# 案例2：电商订单计算器
"""
·定义一个函数，用于根据传入的一批商品信息（商品名，价格，数量），优惠（优惠券，积分抵扣），运费信息计算订单的总金额的函数。
具体规则如下：
· 优惠券需要商品金额满5000才可以使用，且优惠券金额不能超过商品总价。
· 积分抵扣需要商品总金额满5000才可以使用，100积分抵扣1元（且抵扣金额不能超过商品总价，积分只能整百抵扣）。
"""
def order_counter(*args,coupon,score,freight):
    """
    定义一个函数，用于根据传入的一批商品信息（商品名，价格，数量），优惠（优惠券，积分抵扣），运费信息计算订单的总金额的函数
    :param args: 商品信息（商品名，价格，数量）
    :param coupon: 优惠券
    :param score: 积分
    :param freight: 运费
    :return: 总金额
    """
    # 1.计算商品总价
    total_price = [goods[1] * goods[2] for goods in args]
    total_price = sum(total_price)


    # 2.扣除优惠券
    if total_price > 5000 and total_price >= coupon:
        total_price -= coupon

    # 3.扣除积分抵扣
    if total_price > 5000 and total_price >= score // 100:
        total_price -= score // 100


    # 4.加上运费
    return total_price + freight


