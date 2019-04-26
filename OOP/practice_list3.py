class ListInfo(object):
    def __init__(self, list_val):
        self.list = list_val

    def add_key(self, key_name):
        # 添加的严肃必须是数字或者字符串
        if isinstance(key_name, (str, int)):
            self.list.append(key_name)
            print(self.list)
            return 'ok'
        return "Warning int or str"

    def get_key(self, index):
        # 判断传入的索引是否超出了列表
        if index < len(self.list) and index >= 0:
            return self.list[index]
        return "input none"

    def update_list(self, list2):
        # self.list = self.list + list2
        self.list.extend(list2)
        return  self.list

    def del_key(self):
        if len(self.list) > 0:
            return self.list.pop(-1)
        return "list is none"

list_info = ListInfo([])
print(list_info.add_key([1,2]))
print(list_info.get_key(2))
print(list_info.update_list([9,8,7]))
print(list_info.del_key())