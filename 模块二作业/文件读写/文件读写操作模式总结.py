'''
r   以可读方式打开文件（默认）open for reading (default)  io.UnsupportedOperation: not writable 以可读方式写入会报错
r+  可读可写，若文件不存在，报错FileNotFoundError: [Errno 2] No such file or directory: 'test.text1'
rb  bytes类型读取

w   以写入的方式打开文件，从文件开头截取open for writing, truncating the file first
w+  写读模式，先清空文件再写入新的内容，若文件不存在，则创建（没卵用） 若之间的文件有内容则清空，写入新的内容。f.read()读取不到内容
wb  bytes类型写入数据,写入的数据必须是bytes类型

a   以写入方式打开，如果文件存在，则附加到文件的结尾处。open for writing, appending to the end of the file if it exists
a   附加写方式打开，不可读
a+  附加读写方式打开  可追加方式打开，不可以读
ab  追加bytes 数据,写入的数据必须是bytes类型

b   bytes类型 binary mode
+   打开磁盘文件以进行更新（读写）open a disk file for updating (reading and writing)
x   创建一个新的文件并以写入的方式打开create a new file and open it for writing
t   文本模式（默认）text mode (default)
'''



# 不写默认r 可读模式 打印python
# with open('test.text') as f:
#
#     data = f.read()
#     print(data)




# r模式 可读模式 打印python
# with open('test.text', 'r') as f:
#
#     data = f.read()
#     f.write('haha')  # io.UnsupportedOperation: not writable 以可读方式写入会报错
#     print(data)



# r+ 可读写模式 在文件后面追加内容learing python 打印python
# with open('test.text', 'r+') as f:
#
#     data = f.read()
#     f.write('learing python')
#     print(data)


# r+  可读可写，若文件不存在，报错 FileNotFoundError: [Errno 2] No such file or directory: 'test.text1'
# r+ 会覆盖之前的内容
with open('模块二知识点总结', 'r+') as f:

    f.write('learing python bbbbbbbbbbbbbbbbbbbbbbbbbb+')



# rb bytes类型读取 打印 b'pythonlearing pythonlearing python'
# with open('test.text', 'rb') as f:
#
#     data = f.read()
#     print(data)


# w 以写入的方式打开文件 文件不存在则创建文件
# with open('test.text2', 'w') as f:
#     f.write('learing python')


# w+ 若之间的文件有内容则清空，写入新的内容。f.read()读取不到内容
# with open('test.text2', 'w+') as f:
#     data = f.read()
#     print(data)
#     f.write('learing python hahaha')


# wb  bytes类型写入数据,写入的数据必须是bytes类型
# with open('test_wb.text', 'wb') as f:
#     f.write(b'learing python hahaha')


# a  追加不存在的文件,创建文件并写入内容
# with open('test_a.text', 'a') as f:
#     f.write('learing python hahaha')


# a  追加存在的文件,在文件最后追加内容
# with open('test.text', 'a') as f:
#     f.write('learing python aaaaaa')


# a+ 可追加方式打开，不可以读
# with open('test_a1.text', 'a+') as f:
#     data = f.read()
#     print(data)
#     f.write('learing python aaaaaa')


# ab 可写方式追加bytes 数据
# with open('test_ab.text', 'ab') as f:
#     f.write(b'learing python aaaaaa')


# x 创建一个新的文件并以写入的方式打开 若文件存在则报错FileExistsError: [Errno 17] File exists: 'test_x.text'
# with open('test_x.text', 'x') as f:
#     f.write('learing python aaaaaa')


# t 文本模式 需要r/w/a 配合
# with open('test_t.text', 'wt') as f:
#     f.write('ttttt')
