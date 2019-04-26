# 继承的语法
# 在python中任何类都有一个共同的父类叫object
class Person():
    _name = 'none'
    __age = 0

    def sleep(self):
        print("sleep...")


# 父类写在括号中
class Teacher(Person):
    name = 'ww'
    pass


t = Teacher()
print(t._name)
# class Animel():
#     def __init__(self):
#         print("Animel")
#
#
# class PaxingAni(Animel):
#     name = '11'
#     def __init__(self, name):
#         print("pa xing dong wu {}".format(name))
#
#
# class Dog(PaxingAni):
#     # __init__就是构造函数
#     # 每次实例化的时候，第一个被自动的调用
#     # 因为主要工作是进行初始化，所以得名
#     def __init__(self):
#         print("I like a dog.")
#
#
# # 实例化的时候，括号内的参数需要跟构造函数的参数匹配
# # 实例化的时候自动调用了Dog的构造函数
# # 因为找到了构造函数，则不再查找父类的构造函数
# kaka = Dog()
# print(kaka)


# 猫没有构造函数
# class Cat(PaxingAni):
#     pass
#
#
# # 此时应该自动调用构造函数，因为Cat没有构造函数，所以查找父类构造函数
# # 在PaxingAni中查到了构造函数，则停止向上查找
# miao = Cat('zhangsan')
# print(Cat.__mro__)
# print(miao)