# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：

L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = []
# for i in L1:
#     if isinstance(i, str) == 1:
#         i = str.lower(i)
#         L2.append(i)

L2 = [i.lower() for i in L1 if isinstance(i, str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
