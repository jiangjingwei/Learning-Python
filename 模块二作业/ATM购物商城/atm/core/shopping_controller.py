from core.credit_controller import pay_shopping_car
from settings import logger_consume
products_list = [
    ('IphoneX', 8000),
    ('Tesla', 1000000),
    ('Python Book', 200),
]

shopping_car = []


def shopping_mall(user_dict):
    ''' 购物商城管理 '''
    logger_consume.info('logger_consume - {0}'.format(user_dict['user_info']['username']))
    while True:
        for index, value in enumerate(products_list):
            goods_info = '{0}. {1}  {2}￥'.format(index, value[0], value[1])
            print(goods_info)
        print('结账【p】  返回首页【q】 查看购物车【c】')
        choice = input('请输入商品的序号，添加到购物车：')
        if choice.isdigit() and 0 <= int(choice) <= len(products_list)-1:
            if user_dict['user_salary'] > products_list[int(choice)][1]:
                user_dict['user_salary'] -= products_list[int(choice)][1]
                print('账号余额为：', user_dict['user_salary'])
                shopping_car.append(products_list[int(choice)])
                logger_consume.warning('salary not enough - {0} - {1}'.format(user_dict['user_info']['username'], products_list[int(choice)]))
            else:
                print('信用卡余额不足！')
                logger_consume.warning('salary not enough - {0}'.format(user_dict['user_info']['username']))
        elif choice == 'q':
            logger_consume.info('back to home - {0}'.format(user_dict['user_info']['username']))
            break
        elif choice == 'p':
            pay_money(user_dict)
            logger_consume.info('pay_money - {0} '.format(user_dict['user_info']['username']))
        elif choice == 'c':
            logger_consume.info('check shopping_car - {0}'.format(user_dict['user_info']['username']))
            if shopping_car:
                print('---------购物车-----------')
                for i in shopping_car:
                    print(i[0])
                print('----------end-----------')
            else:
                print('【购物车暂无商品】')
        else:
            print('选择的商品不存在...')


def pay_money(user_dict):
    user_dict['shopping_car'] = shopping_car
    pay_shopping_car(user_dict)