"""
需求：根据输入的用户名密码执行登录操作，具体要求如下：
1.正确的用户名和密码为admin/666888、zhangsan/123456、taoge/888666
2．输入用户名和密码进行登录，直到登录成功，程序结束运行；如果登录失败，则继续输入用户名和密码进行登录
3．输入的用户名和密码不能为空！
4．登录成功：输出“登录成功，进入B站首页~”
5．登录失败：输出“用户名或密码错误，请重新输入！”
"""


# while TRUE -->  一直循环
# break:只能够出现在循环中，表示结束，跳出当前循环（break跳出循环时，while后面的else中的代码将不会执行）
# continue:只能够出现在循环中，表示中断本次循环，直接进入下一次循环


# while True:
#
# # 输入
#     username = input("请输入您的用户名：")
#     password = input("请输入密码：")
#
#
#     if username == "" or password == "":
#         print("输入的用户名和密码不能为空！")
#         continue
#
#     if username == "zhangsan" and password == "123456":
#         print("登录成功，进入B站首页~")
#         break
#
#     elif username == "正确的用户名和密码为admin" and password == "666888":
#         print("登录成功，进入B站首页~")
#         break
#
#     elif username == "taoge" and password == "888666":
#         print("登录成功，进入B站首页~")
#         break
#
#     else:
#         print("用户名或密码错误，请重新输入！")



"""
需求：用户名密码登录，正确的用户名密码为admin/666888、zhangsan/123456、taoge/888666，5次登录机会，输入错误五次，不允许再操作了。
"""
b = 0
while b < 5:

    #输入
    username = input("请输入用户名:")
    password = input("请输入密码:")

    if username == "" or password == "":
        print("输入的用户名和密码不能为空！")
        b -= 1
        continue

    if username == "admin" and password == "666888":
        print("登录成功！欢迎回家~")
        break

    if username == "zhangsan" and password == "123456":
        print("登录成功！欢迎回家~")
        break

    if username == "taoge" and password == "888666":
        print("登录成功！欢迎回家~")
        break

    else:
        print("用户名或密码错误，请重新输入")
else:
    print("五次机会已用完，请稍等再重试！")