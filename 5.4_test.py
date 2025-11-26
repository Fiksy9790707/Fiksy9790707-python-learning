# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

#     低于18.5：过轻
#     18.5-25：正常
#     25-28：过重
#     28-32：肥胖
#     高于32：严重肥胖

# 用if-elif判断并打印结果：
height = input (r"请输入你的身高(单位:m)")
weight = input (r"请输入你的体重(单位:kg)")

weight = float(weight)
height = float(height)

# bmi = weight / height^2
# 在 Python 中，^ 符号并不是“次方（幂运算）”，而是 按位异或（Bitwise XOR） 运算。
# 因为 height 是浮点数（float），2 是整数，Python 不知道怎么对一个小数做一个位运算，所以报错了。

bmi = weight / (height * height)

if bmi < 18.5:
    print ("过轻")
elif bmi < 25:
    print ("正常")
elif bmi < 28:
    print ("过重")
elif bmi < 32:
    print ("肥胖")
else:
    print ("严重肥胖")
    
