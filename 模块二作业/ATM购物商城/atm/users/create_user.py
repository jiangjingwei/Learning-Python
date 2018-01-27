import json
import datetime
# print(datetime.date.today() + datetime.timedelta(days=365))

user_dic = {
    'username': 'aa',
    'password': '123',
    'status': 0,
    'credit_card': [
        {
            'bank_credit_name': '招商银行young',
            'account': '9527',
            'pay_passwd': '123',
            'salary': 12000,
            'credit_status': 0,
            'create_date': str(datetime.date.today()),
            'expire_date': str(datetime.date.today() + datetime.timedelta(days=365)),
            'service_tax': 0.5,
        },
    ],

}


user_file = user_dic['username'] + '.json'
with open(user_file, 'w') as f:
    f.write(json.dumps(user_dic))