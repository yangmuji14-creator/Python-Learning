# 字典：使用键值对（key：value）来存储数据，每一个键都对应一个值，通过（key）可以快速找到对应的值（value）。
# 特点：键值对（key：value）存储,键（key）不能重复，可修改

# 字典 -- key不能重复（如果重复，后面的值和，会覆盖前面的值），key必须是不可变类型（str,int,float,tuple)
# 定义字典
# dict1 = {"王林":760,"李慕婉":608,"徐立国":580,"韩立":688}
# print(dict1)
# print(type(dict1))
#
# # key必须是不可变类型（str,int,float,tuple)，不能是（list,set,dict)
# dict2 = {0:760,1:608,2:580,3:688}
# print(dict2[1])


# -------------------字典 dict 常见操作-------------------------
# dict1 = {"王林":670,"李慕婉":608,"许立国":580,"韩立":688}
# print(dict1)
#
# # 添加 - key不存在就是添加
# dict1["海涛"] = 550
# print(dict1)
#
# # 修改 - key存在就是修改
# dict1["海涛"] = 620
# print(dict1)
#
# # 查询
# print(dict1["海涛"]) # 根据key获取value
# print(dict1.get("海涛")) # 根据key获取value
#
# print(dict1.keys()) # 获取所有key
# print(dict1.values()) # 获取所有value
# print(dict1.items()) # 获取所有的键值对 key:value
#
# # 删除
# score = dict1.pop("许立国")
# print(score)
# print(dict1)
#
# del dict1["韩立"]
# print(dict1)
#
# # 遍历
# for k in dict1.keys():
#     print(f"{k} : {dict1[k]}")
#
# for v,o in dict1.items():
#     print(f"{v} ：{o}")



# 案例
"""
●开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据，
通过控制台菜单与用户交互。具体功能如下：
1．添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
2．修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
3．删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
4．查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：×Xx，商品数量：xxx"。
5．退出购物车
"""


# 创建字典 -- 结构：shopping_cart = {"Meat80":{"price":6999,"num":2}},{"鼠标”：{...}}
shopping_cart = {}
menu = """
########## 购物车系统 ###########
#        1.添加购物车           #
#        2.修改购物车           #
#        3.删除购物车           #
#        4.查询购物车           #
#        5.退出购物车           #
###############################
"""




while True:
    # 1.菜单
    print("欢迎使用购物车管理系统")
    print(menu)


    # 2.用户执行操作
    choice = int(input("请选择要执行的操作(1-5)："))

    match choice:
        case 1:  # 添加购物车
            goods_name = input("请输入商品名称：")
            goods_price = float(input("请输入商品价格："))
            goods_num = int(input("请输入商品数量："))

            # 如果商品存在，则不执行添加，提示信息
            if goods_name in shopping_cart:
                print("该商品已存在，请重新选择~")
            else:
                shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
                print("商品添加完成！")
        case 2:  # 修改购物车
            goods_name = input("请输入要修改的商品名称：")
            if goods_name not in shopping_cart:
                print("商品不存在，请重新选择 ~")
                continue
            goods_price = float(input("请输入商品最新的价格："))
            goods_num = int(input("请输入商品最新的数量："))
            shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
            print("商品修改完成！")

        case 3:  # 删除购物车
            goods_name = input("请输入要删除的商品名称：")
            if goods_name not in shopping_cart:
                print("商品不存在，请重新选择 ~")
            else:
                del shopping_cart[goods_name]
            print("商品删除完成！")

        case 4:  # 查询购物车
            for m, n in shopping_cart.items():
                print(f"商品名称：{m}\t 商品价格：{n['price']}\t 商品数量:{n['num']}")
        case 5:  # 退出购物车
            break
        case _:  # 匹配其他所有情况
            print("非法操作，不支持！！！")
