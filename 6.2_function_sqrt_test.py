# 请定义一个函数quadratic(a, b, c)，接收3个参数
# 返回一元二次方程 ax2+bx+c=0ax2+bx+c=0 的两个解。
# 提示：
# 计算平方根可以调用math.sqrt()函数：
import math

def quadratic(a, b, c):
    delta = b*b-4*a*c
    # 代码复用：如果 math.sqrt(b*b-4*a*c) 在代码里出现了三次，就应该把它提取成一个变量 delta。
    # 这不仅让代码更好看，还能减少 CPU 重复计算的开销。
    if delta >= 0:
        x = (-b+math.sqrt(delta))/(2*a)
        y = (-b-math.sqrt(delta))/(2*a)
        # 运算符优先级 (Operator Precedence)：
        # 永远不要相信默认的优先级，只要涉及分母是乘法运算的，无脑加上括号 (2 * a)。
        return (x,y)
    else:
        return 0

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')