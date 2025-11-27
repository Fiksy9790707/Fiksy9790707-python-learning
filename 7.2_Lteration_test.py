# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：

def findMinAndMax(L):
    

    if len(L) == 0:
        return (None, None)
    else:
        max = L[0]
        min = L[0]
    # 注意：i 直接就是列表里的元素（值），不是下标！
    # for i in L:
    #     if max < L[i]:
    #     max = L[i]
    #     elif min > L[i]:
    #     min = L[i]
    #     else:
    #         pass
    # return (min, max)
    for i in L:
        if i > max:
            max = i
        elif i < min:
            min = i

    return (min, max)
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
