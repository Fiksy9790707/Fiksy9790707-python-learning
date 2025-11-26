# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：

# def mul(x, y):
#     return x * y

# # 测试
# print('mul(5) =', mul(5))
# print('mul(5, 6) =', mul(5, 6))
# print('mul(5, 6, 7) =', mul(5, 6, 7))
# print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
# if mul(5) != 5:
#     print('mul(5)测试失败!')
# elif mul(5, 6) != 30:
#     print('mul(5, 6)测试失败!')
# elif mul(5, 6, 7) != 210:
#     print('mul(5, 6, 7)测试失败!')
# elif mul(5, 6, 7, 9) != 1890:
#     print('mul(5, 6, 7, 9)测试失败!')
# else:
#     try:
#         mul()
#         print('mul()测试失败!')
#     except TypeError:
#         print('测试成功!')

# def mul(*arg):
#     result = 1
#     for i in arg:
#         result = result * i
#     return result
# 逻辑陷阱：题目要求“接收一个或多个数”

#     你的写法：def mul(*arg):

#     问题：这种写法允许不传任何参数（即 mul()）。如果你调用 mul()，你的代码会返回 1。

#     测试失败原因：最后的测试代码里写了 try... except TypeError。它期望 mul() 报错（即不允许空参数），但你的代码不报错，所以测试会输出 'mul()测试失败!'。

#     修正：使用 def mul(x, *args):。这样必须传入第一个参数 x，剩下的参数才给 args。如果没有参数，Python 会自动抛出 TypeError。
def mul(x, *args):
    result = x
    # 只需要遍历剩下的 args 即可
    for i in args:
        result = result * i
    return result

# 测试
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('mul(5)测试失败!')
elif mul(5, 6) != 30:
    print('mul(5, 6)测试失败!')
elif mul(5, 6, 7) != 210:
    print('mul(5, 6, 7)测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('mul(5, 6, 7, 9)测试失败!')
else:
    try:
        mul()
        print('mul()测试失败!')
    except TypeError:
        print('测试成功!')
