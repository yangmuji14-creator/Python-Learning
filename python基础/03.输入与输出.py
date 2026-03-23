# 获取键盘上输入的数据 -- input(..)
# name = input("请输入你的姓名：")
# age = input("请输入你的年龄：")
# hobby = input("请输入你的爱好：")
#
# print(name + "您好\n" + "您的年龄是：" + age + "岁\n" + "您喜欢：" + hobby)
#
# print(f"{name}，您好\n 您的姓名是:{name}\n 您的年龄是:{age}\n 您喜欢:{hobby}")

# 案例：
# 总金额
# a = 10000

# 输入卡号与密码
# card = input("请输入你的卡号:")
# password = input("请输入密码:")
#
# print(f"您的卡号是: {card}\n  您的余额为: {str(a)}\n ")
#
# b = input("请输入取款金额:")
# c = a - int(b)
#
# print(f"取款成功！\n 您的余额: {c}")
# print(f"取款成功！\n 您的余额: {a - int(b)}")



# 练习：用户输入两个数，要求将两个数相加求和输出

a = input("请输入第一个数：")
b = input("请输入第二个数字：")
print(int(a) + int(b))