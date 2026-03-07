# 1.定义类是，类名的命名规范：
#       · 大驼峰命名法,UserInfo,UserAccount
# 2.__dict__ 是python中用户自定义类实例的一个特殊属性，用于以字典形式存储对象的属性。



# class Car:
#     # __init__ 方法时初始化的方法，会在对象创建时自动调用，可以在该方法中为对象设置对应的属性
#     # self：是第一个参数，表示当前索创建出来的示例对象
#     def __init__(self,c_color,c_brand,c_name,c_price):
#         self.color = c_color
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#         print("Car,类型的对象初始化完毕，对象属性已经加载完毕")
#
#
# # 创建对象
# c1 = Car("红色","BMW","X7","800000")
# print(c1.__dict__)
#
# c2 = Car("黑色","BMW","M4","1100000")
# print(c2.__dict__)


# ------------------------------ 定义实例 ---------------------------
# class Car:
#     def __init__(self,c_color,c_brand,c_name,c_price:int):
#         self.color = c_color
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#         print("Car,类型的对象初始化完毕，对象属性已经加载完毕")
#
#     # 定义实例方法
#     def running(self):
#             print(f"{self.brand} {self.name} 正在高速行驶中.....")
#
#     def total_cost(self,discount,rate=0.1) -> float:
#             total_cost = self.price * discount + self.price * rate
#             return total_cost
#
#
# # 测试
# c1 = Car("RED","BMW","M4",1200000)
#
# # 调用对象中的方法
# c1.running()
#
# total = c1.total_cost(0.9,0.2)
# print(total)



# ------------------------------------- 定义类 魔法方法 --------------------
# class Car:
#     def __init__(self,c_color,c_brand,c_name,c_price:int):
#         self.color = c_color
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#         print("Car,类型的对象初始化完毕，对象属性已经加载完毕")
#
#
#     def running(self):
#             print(f"{self.brand} {self.name} 正在高速行驶中.....")
#
#     def total_cost(self,discount,rate=0.1) -> float:
#             total_cost = self.price * discount + self.price * rate
#             return total_cost
#
#     # 魔法方法
#     def __str__(self):
#         return f"{self.color} {self.brand} {self.name} {self.price}"
#
#     def __eq__(self,other):
#         return self.color == other.color and self.brand == other.brand and self.name == other.name and self.price == other.price
#
#     def __lt__(self,other):
#         return self.price < other.price
#
#
# # 测试
# c1 = Car("RED","BMW","M4",1200000)
# print(c1)
#
# c2 = Car("RED","BMW","M4",1200000)
# print(c2)


# print(c1 == c2)
# print(c1 < c2)









# --------------------------实例属性 与 类属性 -------------------------------
class Car:
    # 类属性
    wheel = 4
    tax_rate = 0.1

    def __init__(self,c_color,c_brand,c_name,c_price:int):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        print("Car,类型的对象初始化完毕，对象属性已经加载完毕")


    def running(self):
            print(f"{self.brand} {self.name} 正在高速行驶中.....")

    def total_cost(self,discount,rate=0.1) -> float:
            total_cost = self.price * discount + self.price * rate
            return total_cost

    # 魔法方法
    def __str__(self):
        return f"{self.color} {self.brand} {self.name} {self.price}"

    def __eq__(self,other):
        return self.color == other.color and self.brand == other.brand and self.name == other.name and self.price == other.price

    def __lt__(self,other):
        return self.price < other.price


# 测试
c1 = Car("RED","BMW","M4",1200000)
print(c1)
print(c1.wheel) # 通过实例对象，查找属性时，会先查找实例属性；实例属性不存在，再查找类属性


# c2 = Car("RED","BMW","M4",1200000)
# print(c2)






