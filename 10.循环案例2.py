"""
1，系统随机生成一个随机数
--->   可以使用random（import random）
              random_number = random.randint(1,100)
2.用户根据提示猜数字，并将所猜的数字输入系统
3．如果猜错，系统给出提示是猜大了，还是猜小了，然后继续输入猜的数字
4．如果猜对，系统自动退出，游戏结束
"""

import random
random_number = random.randint(1,100)

while True:
    num = int(input("请输入一个数字（1-100）："))

    if num > random_number:
        print("猜大了")
    elif num < random_number:
        print("猜小了")
    elif num == random_number:
        print("恭喜你，猜对啦！")
        break


"""
需求1：将1-1000之间（含1000）所有的5的倍数的数字累加起来。
需求2：统计字符串"akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"字符串中有多少个a和k。
"""

# 需求1 ：
# num = 0
# for a in range(0,1001,5):
#     num += a
#
# else:
#     print(f"1-1000之间（含1000）所有的5的倍数的数字累加之和为：",num)
#
# # 需求2
# x_a = 0
# x_k = 0
# for b in "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd":
#     if b == "a":
#         x_a += 1
#
#     elif b == "k":
#         x_k += 1
#
# else:
#     print(f"含有{x_a}个“a")
#     print(f"含有{x_k}个”k")

