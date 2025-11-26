args = ['gcc', 'hello.c', 'world.c']
# args = ['clean']
# args = ['gcc']

match args:
    # 如果仅出现gcc，报错:
    case ['gcc']:
        print('gcc: missing source file(s).')
    # 出现gcc，且至少指定了一个文件:
    case ['gcc', file1, *files]:
        print('gcc compile: ' + file1 + ', ' + ', '.join(files))
        print(file1)
        print(','.join(files))
    #     *files (解包/Unpacking)：
    # 那个星号 * 是关键。它的意思是**“剩下的所有元素”**。
    # 列表里从第 3 个元素开始，一直到最后的所有内容，都会被装进一个新的列表，赋值给变量 files。
    # 如果列表只有 2 个元素，files 就会是一个空列表 []。
    # 仅出现clean:
    case ['clean']:
        print('clean')
    case _:
        print('invalid command.')
# case _表示其他所有情况。