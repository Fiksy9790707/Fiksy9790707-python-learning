# 假设我们用一组tuple表示学生名字和成绩：
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字排序：
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# def by_name(t):
#     pass
# L2 = sorted(L, key=by_name)
# print(L2)
# 再按成绩从高到低排序：
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# def by_score(t):
#     pass
# L2 = sorted(L, key=by_score)
# print(L2)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]
def by_score(t):
    return t[1]

L2 = sorted(L, key=by_name)
print(L2)
L3 = sorted(L, key=by_score)
print(L3)
# List 适合存“同类事物”的集合（比如一堆学生）。

# Tuple 适合存“一个事物”的多个属性（比如一个学生的名字和分数）。

# 用 Tuple 是为了暗示：“这俩数据是一对儿，别把它们拆散了，也别轻易改它们。”