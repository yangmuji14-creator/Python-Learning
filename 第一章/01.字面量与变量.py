# print(100) # 整数（int）
# print(3.14) # 浮点数（float）
# print(True) # 布尔（bool）
# print(False) # 布尔（bool）
# print("hello") #字符串（str）
# print("-------------------") #字符串（str）
# print(None)# 空值（None Type）
#
#
# # 布尔类型本质也是整数类型（True = 1；False = 0）
# print(True + 1) # 2
# print(False - 1) # -1
#
#
# # 变量 ------>python是动态类型语言，一个变量是可以储存不同变量的数据的（但是在项目开发中，推荐变量只存储一种类型的数据）
# num = 1114.4
# print(num)
#
# num = num + 1
# print(num)
#
# num = "OK"
# print(num)
#
# num = True
# print(num)


#案例
base = 20.7 #基础播放量
incr = 50 #新增播放量
print("未来第一个月的播放量：",base + incr)
print("未来第一个月的播放量：",base + incr*2)


#案例---升级（一次性定义多个变量）
base,incr = 20.7,50 #基础播放量
print("未来第一个月的播放量：",base + incr)
print("未来第一个月的播放量：",base + incr*2)
