# __all__是一个模块级别的特殊变量，用于指定from 模块名 import * 时会导入那些功能（*通配了哪些功能）
# 注意：__all__控制的是 from...import * 时，要导入的功能，并不会影响直接导入具体的功能（如：from...import 功能)
__all__ = ['log_separator1','log_separator2','log_separator3']

# 常量（不会发生变化的数据；常量的名称为全部大写）
PI = 3.1514926
NAME = "黑马※涛哥"


# 函数
def log_separator1():
    print("-" * 20)

def log_separator2():
    print("*" * 30)

def log_separator3():
    print("-" * 40)

def log_separator4():
    print("-" * 50)

# 测试
# __name__ : python中的内置变量，表示的当前模块的名字（直接运行当前模块，__name__ 的值为 "__main__" ; 当前模块被导入时，__name__的值就是模块名
# 执行当前文件，则会执行如下代码；如果当前模块被导入，如下代码则不执行
if __name__ == '__main__':
    log_separator1()