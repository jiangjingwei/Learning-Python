import pickle
user_dict = [
    {"username": "a123", "password": "123123", "role": "a"},
    {"username": "s123", "password": "123123", "role": "s"},
    {"username": "t123", "password": "123123", "role": "t"},
]

with open('users.text', 'wb') as f:
    data = pickle.dumps(user_dict)
    f.write(data)