import datetime
import time
import os
import json
from settings import BASE_DIR, logger_operation
from core import shopping_controller

flag = True


def credit_cards(user_dict):
    ''' 信用卡管理 '''
    while flag:
        welcome_msg = '''
        ----------------信用卡中心--------------
        1. 添加账户
        2. 冻结账户
        3. 解冻账户
        4. 提现
        5. 转账
        6. 还款
        7. 结账购物车
        b. 返回首页
        '''
        print(welcome_msg)
        credit_controller(user_dict)


def credit_controller(user_dict):

    global flag
    actions = {
        '1': add_account,
        '2': freeze_account,
        '3': unfreeze_account,
        '4': withdraw,
        '5': transfer,
        '6': repayment,
        '7': pay_shopping_car,
        'b': flag,
    }
    choice = input('请输入选项：')
    if choice.isdigit() and 0 < int(choice) < len(actions):
        actions[choice](user_dict)
    elif choice == 'b':
        flag = False
    else:
        print('输入的选项不存在...')


def add_account(user_dict):
    bank_credit_name = input('请输入银行名称：')
    account = input('请输入账户：')
    pay_passwd = input('请输入密码：')
    salary = input('请输入额度')
    credit_dict = {
        'bank_credit_name': bank_credit_name,
        'account': account,
        'pay_passwd': pay_passwd,
        'salary': salary,
        'create_date': str(datetime.date.today()),
        'expire_date': str(datetime.date.today() + datetime.timedelta(days=365)),
        'credit_status': 0,
        'service_tax': 0.5,
    }
    user_dict['user_info']['credit_card'].append(credit_dict)
    print('添加账户成功...')
    logger_operation.info('add_account {0}'.format(account))


def freeze_account(user_dict):
    account = input('输入要冻结的账户')
    pay_passwd  = input('请输入密码：')
    for i in user_dict['user_info']['credit_card']:
        if i['account'] == account and i['pay_passwd'] == pay_passwd:
            if i['credit_status'] == 0:
                i['credit_status'] = 1
                print('已冻结该账户', i['account'])
                logger_operation.info('freeze_account {0}'.format(user_dict['user_info']['username']))
            else:
                print('账户已冻结...')
                logger_operation.info('freeze_account already {0}'.format(user_dict['user_info']['username']))
                continue
        else:
            print('账户或密码错误...')
            logger_operation.info('account wrong {0}'.format(user_dict['user_info']['username']))
            continue


def unfreeze_account(user_dict):
    account = input('输入要解冻的账户')
    pay_passwd = input('请输入密码：')
    for i in user_dict['user_info']['credit_card']:
        if i['account'] == account and i['pay_passwd'] == pay_passwd:
            if i['credit_status'] == 1:
                i['credit_status'] = 0
                print('已解冻该账户', i['account'])
                logger_operation.info('unfreeze_account {0}'.format(user_dict['user_info']['username']))
            else:
                print('账户已解冻...')
                logger_operation.info('unfreeze_account already {0}'.format(user_dict['user_info']['username']))
        else:
            print('账户或密码错误...')
            logger_operation.info('account wrong {0}'.format(user_dict['user_info']['username']))


def withdraw(user_dict):
    account = input('输入要提现的账户')
    pay_passwd = input('请输入密码：')
    for i in user_dict['user_info']['credit_card']:
        if i['account'] == account and i['pay_passwd'] == pay_passwd:
            if i['credit_status'] == 0:
                withdraw_money = input('请输入要提现的金额(手续费0.01)：')
                if withdraw_money.isdigit() and int(withdraw_money) > 0:
                    if i['salary'] * i['service_tax'] > int(withdraw_money):
                        i['salary'] *= 1-i['service_tax']
                        i['salary'] -= int(withdraw_money)
                        print('提现成功')
                        logger_operation.info('withdraw sucess - {0} - {1}'.format(user_dict['user_info']['username'], int(withdraw_money)))
                    else:
                        print('不能提现，余额为：{0}￥'.format(i['salary']))
                        logger_operation.info('withdraw fail {0}'.format(user_dict['user_info']['username']))
                else:
                    print('输入有误...')
            else:
                print('账户已冻结...无法提现')
                logger_operation.info('withdraw fail freeze_account already {0}'.format(user_dict['user_info']['username']))

        else:
            print('账户或密码错误...')


def transfer(user_dict):
    username = input('请输入需要转账的用户名')
    user_file = BASE_DIR + '/users/' + username + '.json'
    if os.path.isfile(user_file):
        with open(user_file, 'r') as f_r:
            user_data = json.loads(f_r.read())
            money = input('请输入需要转入的金额：')
            if money.isdigit() and int(money) < user_dict['user_info']['credit_card'][0]['salary']:
                user_data['credit_card'][0]['salary'] += int(money)
                user_dict['user_info']['credit_card'][0]['salary'] -= int(money)
                with open(user_file, 'w') as f_w:
                    f_w.write(json.dumps(user_data))
                    print('转账成功...')
                    logger_operation.info(
                        'transfer success - {0} - {1} '.format(user_dict['user_info']['username'], money))
            else:
                print('输入有误...')
    else:
        print('对方账号不存在...')
        logger_operation.info('transfer wrong account - {0}'.format(user_dict['user_info']['username']))


def repayment(user_dict):
    account = input('输入要还款的账户')
    pay_passwd = input('请输入密码：')
    for i in user_dict['user_info']['credit_card']:
        if i['account'] == account and i['pay_passwd'] == pay_passwd:
            if i['credit_status'] == 0:
                withdraw_money = input('请输入要还款的金额：')
                if withdraw_money.isdigit() and int(withdraw_money) > 0:

                    i['salary'] += int(withdraw_money)
                    print('还款成功，账户余额为：{0}￥6'
                          ''.format(i['salary']))
                    logger_operation.info('repayment success - {0} - {1}'.format(user_dict['user_info']['username'], withdraw_money))
                else:
                    print('输入有误...')
            else:
                print('账户已冻结...无法还款')
                logger_operation.info('repayment fail freeze_account already - {0}'.format(user_dict['user_info']['username']))
        else:
            print('账户或密码错误...')


def pay_shopping_car(user_dict):
    if user_dict['shopping_car'] is not None:
        print('请选择以下任意一张信用卡账户结账：')
        for index, value in enumerate(user_dict['user_info']['credit_card']):
            print('{0}. 银行：[{1}]-账户：[{2}]-余额：[{3}]'.format(index, value['bank_credit_name'], value['account'], value['salary']))
        choice = input('请选择信用卡：')
        if choice.isdigit() and int(choice) < len(user_dict['user_info']['credit_card']):
            total_pay = 0
            for i in user_dict['shopping_car']:
                total_pay += i[1]
            if user_dict['user_info']['credit_card'][int(choice)]['salary'] > total_pay:
                user_dict['user_info']['credit_card'][int(choice)]['salary'] -= total_pay
                print('购买成功， 剩余{0}￥'.format(user_dict['user_info']['credit_card'][int(choice)]['salary']))
                logger_operation.info('pay_shopping_car success  - {0}- {1}'.format(user_dict['user_info']['username'], str(total_pay)))
            else:
                print('账户余额不足...')
                logger_operation.info('salary not enough  {0}'.format(user_dict['user_info']['username']))
    else:
        print('购物车暂无商品,正在前往购物商城...')
        time.sleep(3)
        shopping_controller.shopping_mall(user_dict)
        logger_operation.info('ATM to shopping_mall  {0}'.format(user_dict['user_info']['username']))