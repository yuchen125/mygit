class DitClass(object):
    def __init__(self, dict):
        self.dict = dict

    def del_dict(self, key):
        # 判断key是否在字典里
        if key in self.dict.keys():
            self.dict.pop(key)
            return "delete successfully"
        else:
            return "key not in dict"

    def get_dict(self, key):
        if key not in self.dict.keys():
            return "not found"
        else:
            return self.dict[key]

    def get_list(self):
        return [key for key in self.dict.keys()]
        # return list(self.dict.keys())

    def update_dict(self,dict2):
        # self.dict = dict(self.dict, **dict2)
        self.dict.update(dict2)
        # return [values for values in self.dict.values()]
        return list(self.dict.values())
d = DitClass({'a':1,'b':2,'c':3})
print(d.update_dict({'d':4,'e':5}))
