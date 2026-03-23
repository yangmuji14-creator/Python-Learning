# 模块：就是一个python文件（.py），其中就包含了函数，变量，类，以及可执行的代码。
# 作用：提高代码复用性，降低开发门槛
# 常用语法：（导入模块的语句，一般写在py文件的开头）
#       · import 模块名 [as 别名]
#       · from 模块名 import 功能名 [as 别名]
#       · from 模块名 import *



# 1.导入模块 --> 调用方式：模块名.功能名 / 别名.功能名
# import random as rd # 模块设置别名
#
# for i in range(100):
#     print(rd.randint(1,100))
import random
# 2.导入模块中的功能 from...import.... ----> 调用方式：功能名/别名
# from random import randint # 导入模块randint
# from random import randint as rint # 命名模块randint为rint
from random import * # 导入模块全部功能


for i in range(100):
    print(randint(1,100))

