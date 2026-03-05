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


# 函数的嵌套调用
# 嵌套调用遵循栈结构，最后被调用的函数最先返回LIFO（Last In First Out，后进先出）
# def function_a():
#     print("a ... before")
#     function_b()
#     print("a ... after")
#
# def function_b():
#     print("b ... before")
#     function_c()
#     print("b ... after")
#
# def function_c():
#     print("c ... ")
#
# function_a()
#
# print("函数调用完毕 ~ ")


"""
案例：
1．定义一个函数：根据传入的底和高计算三角形面积的函数（三角形面积=底*高/2）。
2.定义一个函数：计算传入的字符串中元音字母的个数（元音字母为aeiouAEIOU）。
3.定义一个函数：计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分（保留1位小数），
并返回。
"""
# 1．定义一个函数：根据传入的底和高计算三角形面积的函数（三角形面积=底*高/2）。
def triangle_area(a,h):
    """
    通过三角形的底和高计算三角形的面积
    :param a: 底
    :param h: 高
    :return: 三角形的面积
    """
    return a * h / 2

# 2.定义一个函数：计算传入的字符串中元音字母的个数（元音字母为aeiouAEIOU）。
def search_aeiou(x):
    """
    计算传入的字符串中元音字母的个数
    :param x: 元音字母
    :return: 元音字母个数
    """
    num = 0
    for a in x:
        if a in "aeiouAEIOU":
            num += 1
    return num


# 3.定义一个函数：计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分（保留1位小数）
def max_min_average(students_score):
    """
    计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分
    :param students_score: 学生成绩表
    :return: 最高分，最低分，平均分
    """
    score_1 = []
    if type(students_score) == dict:
        for score in students_score.values():
            score_1.append(float(score))

    elif type(students_score) == list:
        for i in students_score:
            score_1.append(i)

    return max(score_1), min(score_1), round(sum(score_1) / len(score_1),1)

s_list = [120,555,444,858,696,666,234,152,165,265,333,65,444,555,89,120]
max_score,min_score,average_score = max_min_average(s_list)
print(f"最高分：{max_score} 最低分：{min_score} 平均分：{average_score}")