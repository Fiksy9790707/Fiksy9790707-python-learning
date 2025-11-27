# 利用切片操作，实现一个trim()函数
# 去除字符串首尾的空格，注意不要调用str的strip()方法：

# def trim(s):
#     if s[0] == ' ':
#         s = s[1:]
#     if s[-1] == ' ':
#         s = s[0:-1]
#     return s

# # 测试:
# if trim('hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello') != 'hello':
#     print('测试失败!')
# elif trim('  hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello  world  ') != 'hello  world':
#     print('测试失败!')
# elif trim('') != '':
#     print('测试失败!')
# elif trim('    ') != '':
#     print('测试失败!')
# else:
#     print('测试成功!')
# 1. 概念混淆：空字符串 vs 空格
#     你的代码：if s[0] == '':
#     错误点：'' 是空字符串（长度为0），而 ' ' 才是空格（长度为1）。
#     在 Python 中，取出一个字符（如 s[0]），它永远不可能是空字符串。如果是空格，它应该等于 ' '。
# 2. 逻辑漏洞：只切了一次 (if vs while)
#     你的代码用的是 if。
#     后果：如果字符串开头有 两个 空格（例如 ' hello'），if 只会把第一个空格切掉，剩下 ' hello'，任务没完成。
#     修正：必须用 while 循环，只要发现开头是空格，就一直切，直到开头不是空格为止。
# 3. 致命报错：越界 (IndexError)
#     场景：如果输入是空字符串 ''，或者全是空格 ' '（切完之后变为空）。
#     后果：当你尝试访问 s[0] 或 s[-1] 时，因为字符串长度为 0，Python 会直接报错：IndexError: string index out of range。
def trim(s):
    # 必须先判断 len(s) > 0，否则空字符串取 s[0] 会报错
    while len(s) > 0 and s[0] == ' ':
        s = s[1:]  # 切掉第一个字符

    while len(s) > 0 and s[-1] == ' ':
        s = s[:-1] # 切掉最后一个字符
        
    return s

# 测试代码保持不变
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')