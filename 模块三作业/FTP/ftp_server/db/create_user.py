import json
import hashlib

m = hashlib.md5()
m.update(b'123')
md5 = m.hexdigest()

info = {
    'alex': {'passwd': md5, 'home_path': '', 'disk_size': ''},
    'jack': {'passwd': md5, 'home_path': '', 'disk_size': ''},
}

with open('users', 'w') as f:
    f.write(json.dumps(info))