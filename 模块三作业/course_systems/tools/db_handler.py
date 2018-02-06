import pickle
import os
from settings import USERS_PATH


class Mypickle:

    def dump_to_file(self, obj, filename):
        # 将对象保存到文件
        with open(filename, 'ab') as f:
            pickle.dump(obj, f)

    def update_to_file(self, obj, filename):
        # 修改文件中的对象
        f_r = open(filename, 'rb')
        new_file = filename + '.bak'
        f_w = open(new_file, 'wb')
        try:
            while True:
                data = pickle.load(f_r)
                if data.name == obj.name:
                    pickle.dump(obj, f_w)
                else:
                    pickle.dump(data, f_w)
        except:
            f_r.close()
            f_w.close()
        finally:
            os.remove(filename)
            os.renames(new_file, filename)

    def show_from_file(self, filename):
        # 读取文件内对象
        with open(filename, 'rb') as f:
            school_list = []
            while True:
                try:
                    school_list.append(pickle.load(f))
                except:
                    break
        return school_list

    def save_to_users(self, user, pwd='123', role='3'):
        with open(USERS_PATH, 'a') as f:
            student_data = '\n%s,%s,%s' % (user, pwd, role)
            f.write(student_data)
