# 类型注解：类型注解是python中的一种语法特性，用于明确标识变量，函数参数和返回值的数据类型，从而使代码更清晰，更安全，更易于维护。
# 定义变量
# a = 695
# score = 98.5
# hobby = "python"
# flag = True
# pic = None
#
# names = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
# phones = {"12555665555","18844446666"}
# options = {"count":0,"total":0}
# goods = ("手机",5999,1)
#
#
#
# # 定义变量 - 指定类型注解
# a2: int = 695
# score2: float = 98.5
# hobby2: str = "python"
# flag2: bool = True
# pic2: None = None
#
# names2: list[str] = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
# phone2: set[str] = {"12555665555","18844446666"}
# options2: dict[str,int] = {"count":0,"total":0}
# goods2: tuple[str,int,int]= ("手机",5999,1)
#
#
# names2.append("A")
# names2.append(10010)


"""
类型注解的写法：
    ·变量：数据类型（如 a: int)

为什么要使用类型注解，有什么好处呢？
·   代码介个更清晰，代码逻辑更安全，易于维护
·   更准确的代码自动提示
·   提前发现代码潜在问题

如果对变量直接赋值，变量运算等场景，python会自动进行类型推断
python是动态类型语言，添加的类型注解只是提示，并不是强制约束！！！
"""


