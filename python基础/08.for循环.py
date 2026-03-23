# for循环：遍历输入的字符串

# msg = input("请输入需要遍历的字符串：")
#
# for a in msg: # s 表示遍历出来的元素 ； msg 表示遍历的数据
#     print(a)
#
# else:
#     print("遍历完成！")

"""
range 语句：
    用法1：range(end) -> 获取一个从0开始，到end结束的数字序列（不包含end本身）
    >> range(5)获取的数据就是 0,1,2,3,4

    用法2：range(start,end) -> 获取一个从start开始，到end结束的数字序列（不含end本身）
    >> range(2,8)获得的数据就是 2,3,4,5,6,7,

    用法3：range(start,end,step) -> 获取一个从start开始，到end结束的数字序列，step步长（不含end本身）
    >> range(0,10,2)获取到数据就是 0,2,4,6,8

"""

"""
案例：1.计算1-100之间所有奇数之和
     2.计算100-500之间所有3倍数的数字之和
"""
#
# #案例1
# num = 0
#
#
# for i in range(1,101):
#     if i % 2 != 0:
#         num += i
#
# else:
#     print(f"1 - 100之间所有奇数之和为：{num}")
#
# #案例改进
# num_1 = 0
#
# for a in range(1,101,2):
#     num_1 += a
#
# else:
#     print(f"1 - 100之间所有奇数之和为：{num_1}")
#
#
# #案例2
# num_2 = 0
#
#
# for b in range(100,501):
#     if b % 3 == 0:
#         num_2 += b
#
# else:
#     print(f"100 - 500之间所有三的倍数之和为：{num_2}")
#
# #案例2改进
# num_3 = 0
#
# for c in range(102,500,3):
#     num_3 += c
#
# else:
#     print(f"100 - 500之间所有三的倍数之和为：{num_3}")
#

#
# #嵌套循环
#
# #长度
# a = int(input("请输入长方形的长度："))
# #宽度
# b = int(input("请输入长方形的宽度："))
#
#
# for o in range(b): # 控制行
#     for i in range(a): # 控制列
#         print("*",end="  ")
#     print()



# 案例：打印99乘法表
# for i in range(1,10): # 外层循环 - 控制行
#     for j in range(1,i+1): # 内层循环 - 列
#         print(f"{j} × {i} = {j * i}",end = "\t")
#     print()

"""
需求1：根据输入的直角边长,打印等腰直角三角形（如下为直角边为3 的等腰直角三角形）
* 
* *   
* * *



需求2:根据输入的数字，打印对应的数字金字塔
1
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4 5 6 

需求3：打印国际象棋 的棋盘

"""


#需求1：
# l = int(input("请输入一条直角边长："))
#
# for a in range(l):
#     for b in range(a + 1):
#         print("*",end="\t")
#     print()


#需求2：
# num = int(input("请输入数字："))
#
# for a in range(1,num + 1):
#     for b in range(1,a + 1):
#         print(b,end="\t")
#     print()


#需求3：
# size = 8
#
# for a in range(size):
#     for b in range(size):
#         if (a + b) % 2 == 0:
#             print("■",end = "\t")
#
#         else:
#             print("□",end = "\t")
#     print()




