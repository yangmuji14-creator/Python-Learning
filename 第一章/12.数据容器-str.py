#---------------字符串-----------------
# 介绍：字符串是字符的容器，一个字符串中可以存放任意数量的字符。如："Python" 'Python' """"Python""
# 特点：不可变性（无法修改），有序性，可迭代性。
# 字符串中的每一个字符元素都有其对应的下标（引索），通过元素对应的引索，就可以获取到对应的元素。
from sympy.testing.runtests import split_list

# 字符串 基本操作 ---> 不可变的（无法修改）
# s = "Hello-Python"
#
# print(s[4]) # 正向索引
# print(s[-8]) # 反向索引
#
# # 可迭代性
# for i in s:
#     print(i)
#
# # 切片
# print(s[0:5:1])
# print(s[0:5])
# print(s[:5])
#
#
# print(s[6:12:1])
# print(s[6:12:])
# print(s[6:])
#
#
# # 步长 ----> 正数：从后往前截取 ； 负数，从前往后截取
# print(s[-1:-7:-1])
# print(s[::-1])

"""
# -----------------字符串的常用方法--------------------------
s = "Hello-Python-Hello-World"

# find() 查找指定字符串第一次出现的索引位置
index = s.find("-")
print(index)

#count() 统计字符在指定字符串中出现的次数
c = s.count("o")
print(c)

#upper() 转为大写
su = s.upper()
print(su)

#lower() 转为小写
sl = s.lower()
print(sl)

#split() 将字符串按指定字符切割 - 列表
slist = s.split(" ")
print(slist)

# strip() 去除字符串两端的空格
ss = s.strip
print(ss)

#replace() 将字符串中的指定子串替换为新的内容
sr = s.replace("-","_")
print(sr)

#startswith()/endswith() 判断字符串是否是以指定的字符串开头/结尾，返回布尔值
print(s.startswith("Hello"))
print(s.endswith("Python"))
"""

# ---------------------------字符串案例--------------------------
# 案例1：邮箱格式验证：用户输入一个邮箱，验证邮箱格式是否正确（包含一个@和至少一个.），如果输入正确，输出“邮箱格式正确”，否则输出“邮箱格式错误”


# # 用户输入邮箱 --> 方式一
# email = input("请输入邮箱：")
#
# #验证一个@，和至少一个.
# if email.count("@") == 1 and email.count(".") >= 1 and email.find("@") < email.rfind("."):
#     print("邮箱格式正确")
# else:
#     print("邮箱格式错误")
#


# 方式2---> in 运算符 --> 判断子字符串是否存在字符串中，存在，返回True; 否则，返回False
# 用户输入邮箱
# email = input("请输入邮箱：")
#
# #验证一个@，和至少一个.
# if email.count("@") == 1 and "." in email:
#     print("邮箱格式正确")
# else:
#     print("邮箱格式错误")


"""
1.输入一个字符串，判断该字符串是否为回文（两边对称）
· 黄山落叶松叶落山黄
· 上海自来水来自海上
2.将用户输入的10个字符串，反转后完全转换为大写，然后记录在列表中最后将列表内容，遍历输出出来。
"""

# 习题一：
# str = input("请输入字符串：")
# if str[:] == str[::-1]:
#     print(f"‘{str}’ 是 回文字符串")
# else:
#     print(f"‘{str}’ 不是 回文字符串")


# 习题二：
text = []

# 输入
for a in range(1,11):
    b = input(f"请输入第{a}个字符串：")
    text.append(b.upper())
text1 = text[::-1]

for c in text1:
    print(c)


