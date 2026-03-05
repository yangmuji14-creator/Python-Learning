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
def reg_stu(name,age,gender,city):
    print(f"注册成功，姓名：{name},年龄：{age},性别：{gender},城市：{city}")
    return {"name":name,"age":age,"gender":{gender},"city":city}


# 1.位置参数：调用函数时根据函数自定义时的位置来传递数据。
# 要求：调用函数时参数顺序与定义函数时参数顺序完全一致
stu = reg_stu("张三","18","男","北京")
print(stu)


# 2.关键字参数：调用函数时以函数定义时形参名称作为关键字，以 "键=值" 的形式来传递参数（不要求顺序）。
# 要求：如果位置参数与关键字参数混用，关键字参数必须在位置参数之后（关键字参数之间，没有顺序要求）
stu = reg_stu(name="王林",age="28",gender="男",city="北京")
print(stu)


stu = reg_stu(age="21",name="丽萨",city="湖南",gender="女")
print(stu)

# 排序方式三：位置参数 + 关键字参数
stu = reg_stu("丽萨","21",city="湖南",gender="女")
print(stu)





