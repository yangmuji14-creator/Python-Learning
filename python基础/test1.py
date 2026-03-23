"""
1. 流程控制练习：
编写一段程序，要求用户从键盘输入一个分数（0-100）。

如果分数大于等于 90，输出 "优秀"；

如果分数在 60 到 89 之间，输出 "合格"；

如果分数低于 60，输出 "不合格"。
"""


# score = float(input("请输入分数（0-100)："))
# if score < 0 or score > 100:
#     print("超出输入范围，输入的数在0-100之间")
# elif score < 60:
#     print("不合格")
# elif 60 <= score <= 89:
#     print("合格")
# elif score >= 90:
#     print("优秀")


"""
2. 组合数据类型与函数练习：
定义一个函数 get_max_min(numbers)，接受一个包含多个整数的列表作为参数。函数需要返回该列表中的最大值和最小值。
（示例输入：[5, 12, 1, 8]，示例输出：(12, 1)）
"""

# def get_max_min(*numbers):
#     min_num = min(numbers)
#     max_num = max(numbers)
#     return max_num,min_num


"""
📋 考核题目：房贷还款模拟计算器
1. 任务背景
为了考察学生对 Python 流程控制（条件语句、循环语句）以及基础算术运算的掌握程度 ，请编写一个模拟银行房贷利息计算的程序。
2. 核心输入需求
程序启动后，应依次提示用户输入以下三个信息：
贷款总额：单位为“万元”，支持小数（如：85.5） 。
贷款年限：单位为“年”，整数（如：20） 。
客户等级：字符串类型，用户需输入 A、B 或 C 。
3. 业务逻辑要求（利率判定）
程序需要根据输入的“客户等级”来自动匹配年利率 ：
A 等级：年利率固定为 4.0%。
B 等级：年利率固定为 4.5%。
C 等级：年利率固定为 5.0%。
注意：如果用户输入了 A、B、C 以外的内容，程序应提示“等级输入有误”并结束。
4. 计算公式
总利息 = 贷款总额 × 年利率 × 贷款年限。
月供（元） = (贷款总额 + 总利息) ÷ (贷款年限 × 12) × 10000（注：最后乘以 10000 是为了将“万元”转换为“元”）。
5. 输出规范
计算完成后，程序需要清晰地打印出以下结果 ：
匹配到的年利率（百分比形式，如 4.0%）。
计算出的总利息（保留两位小数）。
计算出的平均月供（保留两位小数）。
"""

# 函数
def total_interest(total,year,rate):
    """
    计算总利息
    :param total:贷款总额（万元）
    :param year: 贷款年限
    :param grade: 用户等级（A,B,C）
    :return: 总利息
    """
    total_interest = total * rate * years
    return round(total_interest,2)

def month_payment(total,all_interest,years):
    """
    计算月供
    :param total: 贷款总额（万元）
    :param all_interest: 总利息
    :param years: 贷款年限
    :return:月供
    """
    month_payment = (total + all_interest) / (years * 12) * 10000
    return round(month_payment,2)

# 1.输入
total = float(input("请输入贷款总额（万元）："))
years = int(input("请输入贷款年限："))
grade = input("请输入用户等级(A,B,C)：")

rate_a = 0.04
rate_b = 0.045
rate_c = 0.05


match grade:
    case "A" | "a":
        total_interest1 = total_interest(total,years,rate_a)
        print(f"年利率为：{rate_a}")
        print(f"总利息为：{total_interest1}")
        print(f"月供为：{month_payment(total,total_interest1,years)}")

    case "B" | "b":
        total_interest2 = total_interest(total, years, rate_b)
        print(f"年利率为：{rate_b}")
        print(f"总利息为：{total_interest2}")
        print(f"月供为：{month_payment(total, total_interest2, years)}")

    case "C" | "c":
        total_interest3 = total_interest(total, years, rate_c)
        print(f"年利率为：{rate_c}")
        print(f"总利息为：{total_interest3}")
        print(f"月供为：{month_payment(total, total_interest3, years)}")

    case _:
        print("等级输入有误,请重新输入！")










