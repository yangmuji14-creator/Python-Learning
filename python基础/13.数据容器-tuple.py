# 元组：
# 特点：
# ·可以储存不同类型的元素
# ·元素可以重复,有序,不可修改（支持引索访问,切片）

# ·count()：统计某元素在元组中出现的次数
# ·index()：查找某个元素组中的索引位置(第一次出现的位置)

# 元组的基本操作 - tuple

# 定义元组
# t1 = (80,95,78,76,80,85,20)
#
#
# print(t1)
# print(type(t1))
#
# # 索引访问
# print(t1[0])
# print(t1[-1])
#
# # 切片
# print(t1[0:5:1])
#
# # count() 统计元素个数
# print(t1.count(80))
#
# # index() 获取元素的索引（第一个元素的位置）
# print(t1.index(80))
#
#
# # 注意点：如果定义单元素的元组，单个元素之后需要加上逗号，比如（100，）
# t2 = ()
# print(t2)
# print(type(t2))
#
#
# t3 = (100,)
# print(t3)
# print(type(t3))


# 元组-组包与解包
# 组包（packing）：将多个值合并到一个容器（元组，列表）中。
# 解包（Unpacking）：将容器（元组，列表）解开成独立的元素，分别赋值给多个变量
#
# t1 = (5,7,9,1)
# t2 = 5,7,9,1
#
# # 基础解包（比变量的数量和容器的元素个数一致）
# a,b,c,d = t1
# print(a,b,c,d)
# #  * 拓展解包（* 手机剩余所有元素，封装列表list中）
# x, *y, z = t2  # x为5，y为[7,9], z为1
# s, *o = t2   #s为[7,9,1]
# *o, e = t2   #o为[5,7,9],e为1
#


# # 案例1：现有两个变量，分别为：a = 10，b = 20，现需要将这两个变量交换，然后输出到控制台
# a = 10
# b = 20
#
# a,b = b,a
# print(a)
# print(b)
#
#
# # 案例2：现有三个变量：分别为：a = 100，b = 200，c = 300，现需要将这三个变量进行交换，将a,b,c的值风别赋值给c,a,b,并将其输出到控制台。
# a = 100
# b = 200
# c = 300
# # 元组的组包与解包
# c,a,b = a,b,c,
# print(a)
# print(b)
# print(c)

"""
案例：根据提供的学生成绩单，完成如下需求：
1.计算每个学生的总分、各科平均分，然后一并输出出来。
2．统计各科成绩的最低分、最高分、平均分，并输出。
3.查找成绩优秀（平均分大于90）的学生，并输出。
"""

students = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周轶", 95, 96, 89),
    ("S006", "王卓", 76, 82, 77),
    ("S007", "红蝶", 89, 91, 94),
    ("S008", "徐立国", 75, 69, 82),
    ("S009", "许木", 86, 89, 98),
    ("S010", "适天", 66, 59, 72)
)

# 1.计算每个学生的总分、各科平均分，然后一并输出出来。
# 方式一：
# for s in students: # ("S001", "王林", 85, 92, 78)
#     total_score = s[2] + s[3] +s[4]
#     average_score = total_score / 3
#     print(f"学号：{s[0]}\t 姓名：{s[1]}\t 总分：{total_score}\t 各科平均分：{average_score:.1f}")
# print()

# 方式二:元组解包
for id,name,cna,math,eng in students: # ("S001", "王林", 85, 92, 78)
    total_score = cna + math + eng
    average_score = total_score / 3
    print(f"学号：{id}\t 姓名：{name}\t 总分：{total_score}\t 各科平均分：{average_score:.1f}")
print()


# 2．统计各科成绩的最低分、最高分、平均分，并输出。
chinese_score = [s[2] for s in students]
math_score = [s[3] for s in students]
english_score = [s[4] for s in students]

print(f"语文最低分：{min(chinese_score)}\t 最高分：{max(chinese_score)}\t 平均分：{sum(chinese_score) / len(chinese_score)}\t")
print(f"数学最低分：{min(math_score)}\t 最高分：{max(math_score)}\t 平均分：{sum(math_score) / len(math_score)}\t")
print(f"英语最低分：{min(english_score)}\t 最高分：{max(english_score)}\t 平均分：{sum(english_score) / len(english_score)}\t")

print()
# 3.查找成绩优秀（平均分大于90）的学生，并输出。
print("优秀学生名单：")
for s in students:
    average_score = (s[2] + s[3] + s[4]) / 3
    if average_score > 90:
        print(f"学号：{s[0]}\t 姓名：{s[1]}\t 平均分：{average_score:.1f}")