import json
info = {
    'alex': {'passwd': '123', 'home_path': '', 'disk_size': ''},
    'jack': {'passwd': '123', 'home_path': '', 'disk_size': ''},
    'tom': {'passwd': '123', 'home_path': '', 'disk_size': ''},
    'eric': {'passwd': '123', 'home_path': '', 'disk_size': ''},
    'hurry': {'passwd': '123', 'home_path': '', 'disk_size': ''},
}

with open('users', 'w') as f:
    f.write(json.dumps(info))