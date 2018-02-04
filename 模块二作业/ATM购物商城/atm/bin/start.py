from core.auth import login
from core.shopping_controller import shopping_mall
from core.credit_controller import credit_cards
from db.db_file import save_to_file


@login
def service_start(user_dict):
    ''' 程序的入口 '''
    while True:
        home_info = '''
        ----------------首页-----------------
        1. 购物商城
        2. 信用卡管理
        3. 保存并退出
        '''
        print(home_info)
        actions = {
            '1': shopping_mall,
            '2': credit_cards,
            '3': save_to_file,
        }
        choice = input('请输入选项：')
        if choice.isdigit() and 0 < int(choice) <= len(actions):
            actions[choice](user_dict)

        else:
            print('输入的选项不存在，请重新输入...')
