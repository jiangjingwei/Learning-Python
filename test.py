name = [-1, 'rain', -1, 'jack', -1, 'peiqi', -1, 'black_girl', -1, 2, -1, 4, 2, 5, -1, 2]

count = 0
index = 0
for i in name:


    if i == 2:
        count += 1

    if count == 2:
        print(index)
        break

    index += 1

if __name__ == '__main__':
    print(len('文件不存在'.encode('utf-8')))