# -------------------------- 函数 - 变量的作用域 -------------------------------------
# 全局变量：在函数外部 或 函数的内部都是可以访问的；
# num = 100
#
# # 定义函数
# def circle_area(r):
#     # 局部变量：只能在函数内部使用
#     pi = 3.14
#     area = pi * r * r
#
#
#     # global : global关键字用于明确告诉python解释器，在函数中要使用全局变量，使得可以在函数中修改内部全局变量的值。
#     # 注意：在基于global声明全局变量时，先要声明，再使用
#     #      尽量避免在函数中使用全局变量，因为会使代码难以维护和调试
#     #      考虑使用函数参数和返回值来传递数据，而不是依赖全局变量
#     #      global主要用在程序的状态，配置和计数器等场景中
#     global num
#     num = 10000
#     print("num = ",num) # 10000
#
#     return area
#
#
# # 调用函数
# c_area = circle_area(10)
# print(c_area)
#
# print("num = ",num)



# ------------------------- 函数 - 传参方式 ----------------------------------
# 定义函数
# def reg_stu(name,age,gender,city):
#     print(f"注册成功，姓名：{name},年龄：{age},性别：{gender},城市：{city}")
#     return {"name":name,"age":age,"gender":{gender},"city":city}
#
#
# # 1.位置参数：调用函数时根据函数自定义时的位置来传递数据。
# # 要求：调用函数时参数顺序与定义函数时参数顺序完全一致
# stu = reg_stu("张三","18","男","北京")
# print(stu)
#
#
# # 2.关键字参数：调用函数时以函数定义时形参名称作为关键字，以 "键=值" 的形式来传递参数（不要求顺序）。
# # 要求：如果位置参数与关键字参数混用，关键字参数必须在位置参数之后（关键字参数之间，没有顺序要求）
# stu = reg_stu(name="王林",age="28",gender="男",city="北京")
# print(stu)
#
#
# stu = reg_stu(age="21",name="丽萨",city="湖南",gender="女")
# print(stu)
#
# # 排序方式三：位置参数 + 关键字参数
# stu = reg_stu("丽萨","21",city="湖南",gender="女")
# print(stu)


# ---------------------------------- 函数 - 默认参数 ---------------------------------------
# 定义：默认参数也称为缺省参数，用于在定义函数时，为参数提供默认值，调用函数时，可以不传递有默认值的参数。
# 注意：1.默认参数必须放在没有默认值的参数列表的后面，一函数在定义时仕可以设置多个默认参数的。
#      2.函数调用时，如果为默认参数传递了值，则会修改默认的参数值；如果没有传递该参数，则直接使用默认值。

# 定义函数
# def reg_stu(name,age,gender="男",city="北京"):
#     print(f"注册成功，姓名：{name},年龄：{age},性别：{gender},城市：{city}")
#     return {"name":name,"age":age,"gender":{gender},"city":city}
#
# # 调用函数
# stu = reg_stu("王林",20)
# print(stu)
#
# stu = reg_stu("李敏",18,"女")
# print(stu)
#
# stu = reg_stu("韩立",22,city="上海")
# print(stu)
#


# ---------------------------------- 函数 - 不定长参数（位置参数 *args --> 元组） ---------------------------------------
# 定义：不定长参数也可叫做可变参数，用于函数定义及调用时参数个数不确定（0个或多个）的场景。
# 需求：更具传入数据，计算这批数据的最小值，最大值，平均值
# def cale_date(*args):
#     min_date = min(args)
#     max_date = max(args)
#     avg_date = sum(args) / len(args)
#     return min_date,max_date,round(avg_date,1)
#
# # 调用函数
# print(cale_date(2,7,9,10,45,88,65,99,85,120,155,164,4448,5,7,44))



# ---------------------------------- 函数 - 不定长参数（关键字参数 **kwargs --> 字典） ---------------------------------------
# 注意：1.参数是以 "键=值" 形式传递的关键字参数，这些 "键=值" 参数都会被kwargs接受，并封装为一个字典类型
#      2.kwargs只是约定俗成的变量名，并不是关键字，这里可以使用仍和合法的变量名（如：**options—）
def cale_date(*args,**kwargs):
    """
    更具传入数据，计算这批数据的最小值，最大值，平均值
    :param args: 不定长位置参数，需要计算这批数据
    :param kwargs: 不定长关键字参数
        round:保留小数个数
        print：是否输出
    :return:
    """
    min_date = min(args)
    max_date = max(args)
    avg_date = sum(args) / len(args)

    if kwargs.get("round") is not None:
        avg_date = round(sum(args) / len(args),kwargs.get('round'))

    if kwargs.get("print"):
        print(f"最大值：{max_date},最小值:{min_date},平均值：{avg_date}")

    return min_date,max_date,avg_date

# 调用函数
print(cale_date(2,7,9,10,45,round=3,print=True))
print(cale_date(2,7,9,10,45,88,65,99,85,120,155,164,4448,5,7,44,round=2,print=False))