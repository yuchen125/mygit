# 属性案例
# 创建Student类，描述学生
# 学生具有Student,name属性
# 但name格式并不统一
# 可以用增加一个函数，然后自动调用的方式，但很蠢
# class Student():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#         #不想修改代码
#         self.setName(name)
#
#     #介绍下自己
#     def intro(self):
#         print("Hi, my name is {0}".format(self.name))
#
#     def setName(self, name):
#         self.name = name.upper()
#
# s1 = Student("kinney", 19)
# s2 = Student("teacher", 24)
# s1.intro()
# s2.intro()

# property 案例
# 定义一个Person类，具有name,age属性
# 对于任意输入的姓名，我们希望都用大写方式保存
# 年龄，我们希望内部统一用整数保存
# x = property(fget, fset, fdel, doc)


import  math
class Person():
    # 函数的名称可以任意
    # 此功能，是对类变量进行读取操作的时候应该执行的函数功能
    def fget(self):
        return self._number

    # 此功能，模拟的是对变量进行写操作的时候执行的功能
    def fset(self, number):
        # 所有输入的姓名以大写形式保存
        self._number = math.floor(number)

    # fdel 模拟的是删除变量的时候进行的操作
    def fdel(self):
        self._number = "nonenumber"

    number = property(fget, fset, fdel,"对number进行的操作")

p1 = Person()
p1.number = 12.3
print(p1.number)
help(property)


# # __call__ 举例
# class A():
#     def __init__(self, name = 0):
#         print("哈哈,我被调用了")
#
#     def __call__(self, *args, **kwargs):
#         print("我被调用了again")
#
# a = A()
# print(a())

# # __str__举例
# class A():
#     def __init__(self, name = 0):
#         print("哈哈,我被调用了")
#
#     def __call__(self, *args, **kwargs):
#         print("我被调用了again")
#
#     def __str__(self):
#         return "图灵学院"
#
# a = A()
# print(a)

# # __getatter__
#
# class A():
#     name = "kinney"
#     age = 18
#     def __getattr__(self, name):
#         print("么找到")
#         print(name)
#
# a = A()
# print(a.name)
# print(a.e)

# # __setattr__案例
# class Person():
#     def __init__(self):
#         pass
#
#     def __setattr__(self, name, value):
#         print("设置属性：{0}".format(name))
#         # 用下列语句会陷入死循环
#         # self.name = value
#         #此种情况，为了避免死循环，规定统一调用父类魔法函数
#         super().__setattr__(name, value)
#
# p = Person()
# print(p.__dict__)
# p.age = 18
# print(p)

# # __gt__案例
# class Student():
#     def __init__(self, name):
#         self._name = name
#
#     def __gt__(self, other):
#         print("哈哈：{0}会比{1}大吗？".format(self, other))
#         return self._name > other._name
#
#     def __str__(self):
#         return self._name
#
# stu1 = Student("one")
# stu2 = Student("two")
# print(stu1 > stu2 )

# # 三种方法的案例
# class Person():
#     # 实例方法
#     def eat(self):
#         print(self)
#         print("Eating......")
#
#     # 类方法
#     # 类方法的第一个参数，一般命名为cls，区别于self
#     @classmethod
#     def play(cls):
#         print(cls)
#         print("Playing......")
#
#     # 静态方法
#     # 不需要用第一个参数表示自身或者类
#     @staticmethod
#     def say():
#         print("Saying......")
#
# kinney = Person()
#
# # 实例方法
# print(kinney.eat())
# # 类方法
# print(Person.play())
# print(kinney.play())
# # 静态方法
# print(Person.say())
# print(kinney.say())