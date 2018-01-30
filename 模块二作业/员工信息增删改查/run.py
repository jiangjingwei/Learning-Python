import json
table_dic = {
    'id': [],
    'name': [],
    'age': [],
    'phone': [],
    'dept': [],
    'date': [],
}

field_index = {
    'id': 0,
    'name': 1,
    'age': 2,
    'phone': 3,
    'dept': 4,
    'date': 5,
}


def main():
    with open('staff_table.text', 'r') as f:
        for item in f.readlines():
            user_list = item.split(',')
            table_dic['id'].append(user_list[0].strip())
            table_dic['name'].append(user_list[1].strip())
            table_dic['age'].append(user_list[2].strip())
            table_dic['phone'].append(user_list[3].strip())
            table_dic['dept'].append(user_list[4].strip())
            table_dic['date'].append(user_list[5].strip())
    while True:
        cmd = input('请输入sql>>>').strip()
        if not cmd: continue
        elif cmd.split(' ')[0] in ['find', 'add', 'del', 'update']:
            controller(cmd)
        else:
            print('语法有误...')


def controller(cmd):
    if cmd.startswith('add'):
        add_user(cmd)
    elif 'where' in cmd:
        query, condition = cmd.split('where')
        result_list = parse_condition(condition)
        if query.startswith('del'):
            parse_del(result_list)
        else:
            parse_query(query, result_list)  # 处理find和update

    else:
        print('语法有误...')


def parse_del(result_list):
    for item in result_list:
        table_dic['id'].remove(item[0])
        table_dic['name'].remove(item[1])
        table_dic['age'].remove(item[2])
        table_dic['phone'].remove(item[3])
        table_dic['dept'].remove(item[4])
        table_dic['date'].remove(item[5])
    save_to_file()
    print('共删除了{0}条记录... '.format(len(result_list)))
    print('删除的数据为：{0}'.format(result_list))


def parse_query(query, result_list):
    if query.startswith('find'):
        show_field = query.split(' ')[1].strip()
        print(show_field)
        if '*' in show_field.strip():
            for item in result_list:
                print(' '.join(item))
            print('查询出{0}条记录...'.format(len(result_list)))
        elif ',' in show_field.strip():
            field = show_field.strip().split(',')
            index = []
            for i in field:
                index.append(field_index.get(i))
            for item in result_list:
                print(' '.join(list(map(lambda x: item[x], index))))
            print('查询出{0}条记录...'.format(len(result_list)))
        elif show_field is not None and show_field != '':
            index = field_index.get(show_field)
            for item in result_list:
                print(item[index])
            print('查询出{0}条记录...'.format(len(result_list)))
        else:
            print('语法有误...')
    else:
        field, value = query.split('set')[1].split('=')
        index = field_index.get(field.strip())
        for item in result_list:
            row_index = table_dic[field.strip()].index(item[index])
            table_dic[field.strip()][row_index] = value.strip()
            item[index] = value.strip()
        for i in result_list:
            print(' '.join(i))
        save_to_file()
        print('修改了以上{0}条记录...'.format(len(result_list)))


def parse_condition(condition):
    actions = {
        '>': oprate_gt,
        '<': oprate_lt,
        '=': oprate_eq,
        'like': oprate_li,
    }
    for i in actions.keys():
        if i in condition:
            result_list = actions[i](i, condition)
            if result_list:
                return result_list


def oprate_gt(i, condition):
    field = condition.split(i)[0].strip()
    field2 = condition.split(i)[1].strip()
    print('----->', field, field2)
    result_list = []
    if field in table_dic.keys():
        for index, value in enumerate(table_dic[field]):
            li = []
            if field2.isdigit() and value.isdigit():
                if int(field2) < int(value):
                    for k in table_dic.keys():
                        li.append(table_dic[k][index])
                if li:
                    result_list.append(li)
            else:
                print('条件有误...')
                break
        return result_list
    else:
        print('条件不存在...')


def oprate_lt(i, condition):
    field = condition.split(i)[0].strip()
    field2 = condition.split(i)[1].strip()
    result_list = []
    if field in table_dic.keys():
        for index, value in enumerate(table_dic[field]):
            li = []
            if field2.isdigit() and value.isdigit():
                if int(field2) > int(value):
                    for k in table_dic.keys():
                        li.append(table_dic[k][index])
                if li:
                    result_list.append(li)
            else:
                print('条件有误...')
                break
        return result_list
    else:
        print('条件不存在...')


def oprate_eq(i, condition):
    field = condition.split(i)[0].strip()
    field2 = condition.split(i)[1].strip()
    result_list = []
    if field in table_dic.keys():
        for index, value in enumerate(table_dic[field]):
            li = []
            if field2 == value:
                for k in table_dic.keys():
                    li.append(table_dic[k][index])
                if li:
                    result_list.append(li)
        return result_list
    else:
        print('条件不存在...')


def oprate_li(i, condition):
    field = condition.split(i)[0].strip()
    field2 = condition.split(i)[1].strip()

    result_list = []
    if field in table_dic.keys():
        for index, value in enumerate(table_dic[field]):
            li = []
            if field2 in value:
                for k in table_dic.keys():
                    li.append(table_dic[k][index])
                if li:
                    result_list.append(li)
        return result_list
    else:
        print('条件不存在...')


def add_user(cmd):
    add_list = cmd.split('staff_table')[-1].strip().split(',')
    if add_list[2].strip() not in table_dic['phone']:
        table_dic['id'].append(str(len(table_dic['id']) + 1))
        table_dic['name'].append(add_list[0].strip())
        table_dic['age'].append(add_list[1].strip())
        table_dic['phone'].append(add_list[2].strip())
        table_dic['dept'].append(add_list[3].strip())
        table_dic['date'].append(add_list[4].strip())
        print(table_dic)
        print('增加了1条记录...')
        # 在这里可以直接读取文件，写入新的数据，就不用再读取table_dic全部数据了
        save_to_file()
    else:
        print('手机号码不能重复')


def save_to_file():
    user_info = ''
    max_id = len(table_dic['id'])
    for index in range(max_id):
        for item in table_dic:
            user_info += table_dic[item][index]
            if item == 'date':
                continue
            user_info += ','
        user_info += '\n'
    with open('staff_table.text', 'w') as f:
        f.write(user_info)


if __name__ == '__main__':
    '''
    命令输入参考格式如下：
    update staff_table set age = 99 where dept = IT
    find * from staff_table where  dept = IT
    find name,age from staff_table where  age > 23
    find name from staff_table where where age = 23
    add staff_table Jack Jiang,26,17800000000,IT,2018-10-29
    del from staff where id = 3 
    '''
    main()