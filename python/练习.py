class Person():
    # name是共有的成员
    name = "tuling"
    # __age就是私有成员
    __age = 18


p = Person()
# name是公有变量
print(p.name)
# __age是私有变量
# print(p.age)
# name mangling技术
print(Person.__dict__)
print(p._Person__age)