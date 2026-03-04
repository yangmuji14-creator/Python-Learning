"""
开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
1．添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
4
2．修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
3．删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
4．查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
5．列出所有学生：遍历所有学生信息并输出。
6，统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学
员姓名。
7.退出系统。
"""

# 添加字典 -- student_info = {"name":{"chinese":100,"math":120,"english":150}}
student_info = {}

# 选择页面
menu = """
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  1.添加学生信息     2.修改学生信息     3.删除学生信息    4.查询学生信息    5.列出所有学生    6.统计班级成绩   7.退出系统  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""

while True:
    print("欢迎使用学生管理系统！")
    print(menu)
    print()
    choice = input("请选择要执行的操作(1-7)：")
    match choice:
        case "1": # 添加学生信息

            student_name = input("请输入姓名：")
            if student_name in student_info:
                print("学生已存在，请重新输入")
                continue

            student_chinese = input("请输入语文成绩：")
            student_math = input("请输入数学成绩：")
            student_english = input("请输入英语成绩：")
            print(f"学生 {student_name} 添加成功！")

            student_info[student_name] = {"chinese":student_chinese,"math":student_math,"english":student_english}

        case "2": # 修改学生信息
            student_name = input("请输入要修改的学生姓名：")
            if student_name not in student_info:
                print("学生不存在，请重新输入")
                continue
            student_chinese = input("请输入最新语文成绩：")
            student_math = input("请输入最新数学成绩：")
            student_english = input("请输入最新英语成绩：")
            print(f"学生 {student_name} 修改成功！")

            student_info[student_name] = {"chinese": student_chinese, "math": student_math, "english": student_english}
        case "3": # 删除学生信息
            student_name = input("请输入要删除的学生姓名：")
            if student_name not in student_info:
                print("学生不存在，请重新输入")
            else:
                del student_info[student_name]
            print(f"{student_name} 信息删除成功！")
        case "4": # 查询学生信息
            enter = input("请输入需要查询的学生姓名：")
            if enter not in student_info:
                print("学生不存在，请检查后再试！")
                continue
            else:
                print(f"姓名：{enter}")
                print(f"语文：{student_info[enter]['chinese']}")
                print(f"数学：{student_info[enter]['math']}")
                print(f"英语：{student_info[enter]['english']}")
                print()
        case "5": # 列出所有学生
            for name, score in student_info.items():
                print(name)
        case "6": # 统计班级成绩
            class_chinese = []
            class_math = []
            class_english = []
            for name,score in student_info.items():
                class_chinese.append(int(score['chinese']))
                class_math.append(int(score['math']))
                class_english.append(int(score['english']))
            totalScore = sum(class_chinese) + sum(class_math) + sum(class_english)
            print(f"班级总分：{totalScore},班级品均分：{totalScore / len(class_chinese)}")
            print(f"语文总分：{sum(class_chinese)},班级品均分：{sum(class_chinese) / len(class_chinese)}")
            print(f"数学总分：{sum(class_math)},班级品均分：{sum(class_math) / len(class_math)}")
            print(f"英语总分：{sum(class_english)},班级品均分：{sum(class_english) / len(class_english)}")

        case "7": # 退出系统
            break
        case _:
            print("输入错误！！")




