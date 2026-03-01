# while 循环 ：打印10遍“人生苦短，我用python~”
# i = 0
# while i < 10:
#     print(f"人生苦短，我用python~{i}")
#     i += 1
# else:
#     print("循环正常结束！")
#


# 案例：计算1-100之间所有偶数的累加之和
a = 0
i = 0
while i < 100:
    i += 2
    a += i
else:
    print(f"1-100中所有偶数累加之和为和为{a}")


#案例改进
total = 0 #记录累加值和
i_1 = 0 #循环开始数字

while i_1 <= 100:
    if i_1 % 2 == 0:
        total += i_1
    i_1 += 1

else:
    print(f"累加之和为:{total}")

