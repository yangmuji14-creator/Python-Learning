# 字典：使用键值对（key：value）来存储数据，每一个键都对应一个值，通过（key）可以快速找到对应的值（value）。
# 特点：键值对（key：value）存储,键（key）不能重复，可修改

# 字典 -- key不能重复（如果重复，后面的值和，会覆盖前面的值），key必须是不可变类型（str,int,float,tuple)
# 定义字典
# dict1 = {"王林":760,"李慕婉":608,"徐立国":580,"韩立":688}
# print(dict1)
# print(type(dict1))
#
# # key必须是不可变类型（str,int,float,tuple)，不能是（list,set,dict)
# dict2 = {0:760,1:608,2:580,3:688}
# print(dict2[1])


# -------------------字典 dict 常见操作-------------------------
dict1 = {"王林":670,"李慕婉":608,"许立国":580,"韩立":688}
print(dict1)

# 添加 - key不存在就是添加
dict1["海涛"] = 550
print(dict1)

# 修改 - key存在就是修改
dict1["海涛"] = 620
print(dict1)

# 查询
print(dict1["海涛"]) # 根据key获取value
print(dict1.get("海涛")) # 根据key获取value

print(dict1.keys()) # 获取所有key
print(dict1.values()) # 获取所有value
print(dict1.items()) # 获取所有的键值对 key:value

# 删除
score = dict1.pop("许立国")
print(score)
print(dict1)
