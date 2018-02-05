import pickle
import os


class Mypickle:

    def __init__(self, filename):
        self.filename = filename

    def dump_data(self, obj):
        with open(self.filename, 'ab') as f:
            pickle.dump(obj, f)

    def load_data(self):
        with open(self.filename, 'rb') as f:
            while True:
                try:
                    yield pickle.load(f)
                except:
                    break


    def edit_data(self, obj):
        with open(self.filename, 'rb') as f, open(self.filename + '.bak', 'wb')as f_w:
            while True:
                try:
                    data = pickle.load(f)
                    print(data, obj)
                    if obj.city == data.city:
                        pickle.dump(obj, f_w)
                    else:
                        pickle.dump(data, f_w)
                except:
                    break

            os.rename(self.filename + '.bak', self.filename)
            # os.rename(self.filename + '.bak', self.filename)

