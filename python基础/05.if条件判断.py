# # if条件判断：如果分数超过688，我就去清华读书
# score =  float(input("请输入您的高考分数："))
#
# if score >= 688:
#     print("你好同学，清华大学欢迎你！")
# else:
#     print("同学还需要努力哦！")
#
# print("-----------------------------")


# 案例：结合前面学习的输入与输出及if条件判断的知识，完成b站登录功能的实现（正确账号和密码为18888888888/666888）

# #正确的账户和密码
# ok_id = 18888888888
# ok_password = 666888
#
# #输入
#
# id = int(input("请输入账号:"))
# password = int(input("请输入密码:"))
#
# #校验输出
# if id == ok_id and password == ok_password :
#     print("登录成功！欢迎您~")
# if id != ok_id :
#     print("账户错误，请检查您的账户输入是否正确")
# if password != ok_password :
#     print("密码错误，请检查密码是否输入正确")





#正确的账户和密码
# ok_id = 18888888888
# ok_password = 666888
#
# #输入
#
# id = int(input("请输入账号:"))
# password = int(input("请输入密码:"))
#
# #校验输出
# if id == ok_id and password == ok_password :
#     print("登录成功！欢迎您~")
# else:
#     print("登录失败，账号或密码错误！")
#


# 案例：根据用户输入的年龄，判断这一年是闰年还是平年（非整百年份，且能被四整除的是闰年；整百年份（如1900，2000）必须被400整除才是闰年）
#
# year = int(input("请输入需要判定的年份："))
#
# # 如果是非整百年份，且能被4整除 就是闰年；整百年份，能够被400整除 也是闰年
# if (year % 100 != 0 and year % 4 ==0) or (year % 400 == 0):
#     print(f"{year}是闰年")
# else:
#     print(f"{year}是平年")

# 需求1：根据用户输入的数字，判断该数字是奇数还是偶数
# 需求2：根据用户输入的年龄，判断该用户是否已经成年（>=18,成年；否则，未成年）
# 需求3：根据用户输入的数字，判断该数据是正数还是负数（不考虑0）
# 需求4：根据用户输入的考试分数，判断该分数是否及格（大于等于60就是及格了）

#需求1
# num = int(input("请输入要判断的数字："))
# if num % 2 == 0 :
#     print(f"{num}为偶数")
# else :
#     print(f"{num}为奇数")

#需求2
# age = int(input("请输入你的年龄："))
# if age >= 18 :
#     print("已成年")
# else :
#     print("未成年")

# 需求3
# num2 = float(input("请输入要判断的数字:"))
# if num2 >= 0 :
#     print(f"{num2}是正数")
# else:
#     print(f"{num2}是负数")

# 需求4
# score = float(input("请输入考试分数："))
# if score >= 60 :
#     print("恭喜你，及格了")
# else:
#     print("未及格，继续加油！")



# if....elseif....else 案例 : 根据用户输入的数字，判断数字是正数，还是负数，还是0
# num3 = float(input("请输入数字："))
#
# if num3 > 0 :
#     print(f"{num3} 是 正数")
#
# elif num3 < 0 :
#     print(f"{num3} 是 负数")
#
# else :
#     print(f"{num3} 是 ‘0’")


#案例 根据输入用户名，密码进行登录系统。
    # 用户名，密码为 admin/666888 或 root/547527 或 zhangsan/123456，则输出登录成功
    # 否则就提示用户名或密码错误

#正确账户和密码
# ok_account_1 = "admin"
# ok_account_2 = "root"
# ok_account_3 = "zhangsan"
#
# ok_password_1 = "666888"
# ok_password_2 = "547527"
# ok_password_3 = "123456"
# #用户输入账户密码
# account = input("请输入账号：")
# password = input("请输入密码：")
#
# #比较输出
# if ((account == ok_account_1 and password == ok_password_1)
#     or (account == ok_account_2 and password == ok_password_2)
#     or (account == ok_account_3) and (password == ok_password_3)):
#     print("登录成功！")
#     print("欢迎回来~~")
# else :
#     print("账户或密码错误，请检查后重试！")



# 案例修改
#正确账户和密码
# ok_account_1 = "admin"
# ok_account_2 = "root"
# ok_account_3 = "zhangsan"
#
# ok_password_1 = "666888"
# ok_password_2 = "547527"
# ok_password_3 = "123456"
# #用户输入账户密码
# account = input("请输入账号：")
# password = input("请输入密码：")
#
# #比较输出
# if account == ok_account_1 and password == ok_password_1 :
#     print("登录成功！")
#     print("欢迎回来~~")
# elif account == ok_account_2 and password == ok_password_2 :
#     print("登录成功！")
#     print("欢迎回来~~")
# elif account == ok_account_3 and password == ok_password_3 :
#     print("登录成功！")
#     print("欢迎回来~~")
# else :
#     print("登录失败，请检查后重试！")



"""""
案例练习  三角形的类型判断：根据输入的三个边长（正整数），判断是等边三角形，普通三角形，还是不能构成三角形
1.构成三角形的条件：两边之和大于第三边
2.三角形判定规则：
    三个边相等：等边三角形
    两个边相等：等腰三角形
    三个都不相等：普通三角形
"""



# # 输入
# a = int(input("请输入三角形的第一条边"))
# b = int(input("请输入三角形的第二条边"))
# c = int(input("请输入三角形的第三条边"))
#
# #比较输出
# if a + b <= c or b + c <= a or c + a <= b:
#     print("此图形不是三角形")
# elif a == b == c:
#     print("此图形为等边三角形")
# elif a == b or b == c or c == a:
#     print("此图形为等腰三角形")
# else:
#     print("此图形为普通三角形")
#


# # 输入
# a = int(input("请输入三角形的第一条边"))
# b = int(input("请输入三角形的第二条边"))
# c = int(input("请输入三角形的第三条边"))
#
# #比较输出
# if a + b <= c or b + c <= a or c + a <= b:
#     print("此图形不是三角形")
# elif a == b == c:
#     print("此图形为等边三角形")
# elif a == b or b == c or c == a:
#     print("此图形为等腰三角形")
# else:
#     print("此图形为普通三角形")

# 案例 北京市居民年度用电电费计算：根据输入的用电度数，计算电费：
# 北京市居民电费采用阶梯电价计价方式，所谓阶梯电价是指按照用户消费的电量分段定价，用电价格随用电量增加
# 呈阶梯状逐级递增的一种电价定价机制。
# ·阶梯电价规则：
# ：第一档：2880度以下，电费单价0.4883元/度
# ：第二档：2880-4800度，电费单价0.5383元/度
# ·第三档：4800度以上，电费单价0.7883元/度


#范围 电费
# a = 2880
# b = 4800
# am = 0.4883
# bm = 0.5383
# cm = 0.7883
# # 输入
# power = int(input("请输入您的用电量："))
#
# # 小于2800度
# if power <= a:
#     num1 = power * am
#
# # 2880-4800度
# elif 2880 < power <= 4800:
#     num1 = (a * am) + (power - a) * bm
#
# # 4800度以上
# else:
#     num1 = (a * am) + ((b - a) * bm) + ((power - b) * cm)
#
# # 输出
# print(f"您家里这个月电费为：{num1}")



