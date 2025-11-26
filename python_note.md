
# Python 学习笔记：List, Tuple, Dict 与核心机制

## 1. 字典 (Dict) 的 Key 为什么不能是 List？

**报错示例：**
```python
key = [1, 2, 3]
d = {}
d[key] = 'value' 
# 报错: TypeError: unhashable type: 'list'
````

### 核心原理：可哈希 (Hashable)

  * **Dict 的底层原理**：字典本质是**哈希表 (Hash Table)**。Python 需要通过计算 Key 的哈希值 (`hash(key)`) 来定位数据存储的内存地址。
  * **List 是可变的 (Mutable)**：列表的内容随时可能改变（比如 `append`）。如果列表变了，它的哈希值也会变。
  * **后果**：如果你用列表做 Key，一旦列表被修改，你就再也找不到存进去的数据了。为了防止这种逻辑崩坏，Python 禁止用 List 做 Key。

### 解决方案

使用 **Tuple (元组)**。元组是**不可变 (Immutable)** 的，创建后不能修改，因此它的哈希值是固定的，可以放心当作字典的 Key。

```python
key = (1, 2, 3)  # 把 [] 换成 ()
d[key] = 'value' # 成功
````

-----

## 2\. 列表排序：`sort()` vs `sorted()`

### `list.sort()`

  * **行为**：**原地修改 (In-place modification)**。
  * **返回值**：`None`。
  * **内存视角**：直接修改内存中原本的那个列表，不创建新副本。

**新手陷阱：**

```python
a = [3, 1, 2]
b = a.sort() 
print(b) # 输出 None (因为 sort 没有返回值)
print(a) # 输出 [1, 2, 3] (a 本身被改了)
````

### `sorted(list)`

  * **行为**：**创建新列表**。
  * **返回值**：排好序的全新列表。
  * **内存视角**：原列表保持不变，另外开辟内存存结果。

<!-- end list -->

```python
a = [3, 1, 2]
b = sorted(a)
print(b) # [1, 2, 3]
print(a) # [3, 1, 2] (原封不动)
````

-----

## 3\. 字符串 (String) 的不可变性

虽然 `list.sort()` 是原地修改，但字符串的方法（如 `replace`）行为完全不同。

**示例：**

```python
s = 'abc'
s.replace('a', 'A') 
print(s) # 输出 'abc' —— 竟然没变！
````

### 核心原理：不可变对象 (Immutable)

  * 字符串在 Python 中一旦创建，**永远无法被修改**。
  * `s.replace('a', 'A')` 并不是修改了 `s`，而是在内存里**新创建**了一个 `'Abc'` 对象并返回。
  * 如果你不把结果赋值给变量，这个操作就没有任何意义。

**正确写法：**

```python
s = s.replace('a', 'A') # 必须重新赋值接住它
````

-----

## 4\. 结构化模式匹配 (Python 3.10+)

当我们看到类似 `case ['gcc', file1, *files]:` 的语法时，这是 Python 的 **Match Case** 语法（类似 switch，但更强大）。

```python
command = ['gcc', 'main.c', '-O2', '-Wall']

match command:
    # 匹配条件：列表以 'gcc' 开头，且至少有 2 个元素
    case ['gcc', file1, *files]:
        print(file1)  # 提取第 2 个元素 -> 'main.c'
        print(files)  # 提取剩余所有元素 -> ['-O2', '-Wall']
````

  * `*files` 表示**解包 (Unpacking)**，将剩余的元素打包成一个新的列表。

-----

## 5\. 补充：其他新手易错点

  * **没有 `n++`**：Python 不支持自增运算符。
      * ❌ `n++`
      * ✅ `n += 1`
  * **`input()` 类型**：`input()` 永远返回**字符串**。
      * 如果要进行数学运算，必须手动转换：`float(input(...))` 或 `int(input(...))`。


```
