# # 常见数据类型
# print("hello")
# print(type("hello"))
#
# print(type(12)) #int
# print(type(1.23)) #float
# print(type(True)) #bool
# print(type(False)) #bool
# print(type(None)) #NoneType
#
# a = 2
# print(type(a)) # int
#
#
# # 常见数据类型 ----> isinstance(数据,类型) --> 判定数据是否是指定类型，如果是:True,否则:False
# num = 10
# print(isinstance(num,int))
# print(isinstance(num,float))
# print(isinstance(num,complex))
# from numpy import msg

# # 字符串
# # 定义字符串的三种方式
# s1 = 'hello'
# s2 = "hello"
# s3 = """
# Hello:
#     欢饮大家进入python课程的学习
#     大家记得一键三连哦！
# """ # 三引号可以定义多行内容
# print(s1)
# print(s2)
# print(s3)
#
# print(type(s1))
# print(type(s2))
# print(type(s3))
#
#
# # 定义字符串 ---> It's very good
# # 转义字符 \' \" \n \t(制表符---Tab键)
# msg = 'It\'s very good'
# print(msg)
#
# msg2 = "It's very good"
# print(msg2)
#
# msg3 = "Hello的意思就是\"你好\""
# print(msg3)
#


# # 字符串拼接
# s1 = "人生苦短" "我用python" ",OK"
# print(s1)
#
# msg1 = "人生苦短"
# msg2 = "我用python"
# print("某某说:" + msg1 + "，" + msg2)


# # 案例：----> str(int数字) ---> 将int类型的数字转为字符串
# name = "涛哥"
# age = 18
# pro = "软件工程"
# hobby = "Python,Java"
# print("大家好，我是" + name + "今年" + str(age) + ",学习的专业是" + pro + ",爱好" + hobby)


# # 字符串格式化 --> %s占位符
# name = "涛哥"
# age = 18
# pro = "软件工程"
# hobby = "Python,Java"
# print("大家好我是 %s,今年 %d，学习的专业是 %s，爱好%s" %(name,age,pro,hobby))


# 字符串格式化 --> %s占位符
name = "涛哥"
age = 18
pro = "软件工程"
hobby = "Python,Java"
print(f"大家好我是{name} ,今年 {age}，学习的专业是 {pro}，爱好{hobby}")