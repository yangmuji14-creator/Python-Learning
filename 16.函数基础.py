# 注意：函数定义的时候不会执行，只有在调用函数的时候，函数体的逻辑才会执行。
# 函数必须先定义，后调用。
# 函数中通过缩进来描述所属关系。
# 函数定义


# def out_line():
#     print("--------------------------------------")
#     print("--------------------------------------")
#     return 0
#
#
# # 函数调用
# out_line()


# 函数的参数与返回值
# 函数1：计算圆的面积
# def circle_area(r):
#     area = 3.14 * r * r
#     return  area
#
# r = float(input("请输入圆的半径："))
# print(f"圆的面积为：{circle_area(r)}")
#
#
# 函数2：计算长方形的面积 --- a * b
# def area_of_rectangle(a,b):
#     """
#     根据长方形的长度与宽度，计算长方形的面积
#     :param a: 长度
#     :param b:宽度
#     :return:长方形的面积
#     """
#     area = a * b
#     return area
#
# a = float(input("请输入长方形的长："))
# b = float(input("请输入长方形的宽："))
#
# print(f"长方形的面积为：{area_of_rectangle(a,b)}")
#
#
# # 函数3:计算圆的面积，周长 -- 半径 ----> 如果返回值有多个，多个返回值之间逗号分隔 ----> 多个返回值会封装到元组之中
# def cirale_area_len(r):
#     """
#     通过圆的半径来计算圆的面积与周长
#     :param r: 半径
#     :return: 圆的面积与周长
#     """
#     return round(3.14 * r ** 2,1),round(2 * 3.14 * r,1)
#
# al = cirale_area_len(10)
# print(al)
#
# m,n = cirale_area_len(10)
# print(m)
# print(n)


