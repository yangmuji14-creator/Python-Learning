# 1.导入模块
# import utils.my_fun
#
# utils.my_fun.log_separator1()



# from utils import my_fun
# my_fun.log_separator1()
# my_fun.log_separator2()
# my_fun.log_separator3()

# from utils.my_fun import log_separator1
# from utils.my_fun import log_separator1 as log1
# log_separator1()
# log1()

# 注意：如果要通过from utils import * 导入所有模块，需要__int__.py 文件中添加__all__ = []
# from utils import *
# my_fun.log_separator1()
# print(my_var.NAME)


# 2.导入模块中的功能
from utils.my_var import NAME,PI
from utils.my_fun import log_separator1 as log1

print(NAME)
print(PI)
log1()