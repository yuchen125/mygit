class SecInfo(object):
    def __init__(self, my_set):
        self.sett = my_set

    def add_setinfo(self,keyname):
        self.sett.add(keyname)
        return self.sett

    def get_intersection(self, set2):
        if isinstance(set2, set):
            self.sett = self.sett.intersection(set2)
            return  self.sett
        return "no set"
        # return self.sett & set2

    def get_union(self, set2):
        if isinstance(set2, set):
            return self.sett | set2
        return "no set"

    def del_difference(self, set2):
        if isinstance(set2, set):
            return  self.sett - set2
        return "no set"

s = SecInfo({1,2,4})
print(s.add_setinfo(9))
print(s.get_intersection([1]))
print(s.get_union('1'))
print(s.del_difference(1))