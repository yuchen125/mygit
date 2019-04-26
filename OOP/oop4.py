# 多继承的例子
#子类可以直接拥有父亲的属性和方法，私有属性和方法除外
# class Fish():
#     def __init__(self, name):
#         self.name = name
#
#     def swim(self):
#         print("I'm swimming......")
#
# class Bird():
#     def __init__(self, name):
#         self.name = name
#
#     def fly(self):
#         print("I'm flying......")
#
# class Person():
#     def __init__(self, name):
#         self.name = name
#
#     def work(self):
#         print("Working......")
# # 多继承的例子
# class SuperMan(Person, Bird, Fish):
#     def __init__(self, name):
#         self.name = name
# # 多继承的例子
# class SwimMain(Person, Fish):
#     def __init__(self, name):
#         self.name = name
# s = SuperMan("kinney")
# print(s.fly())
# print(s.swim())
# # 单继承的例子
# class Student(Person):
#     def __init__(self, name):
#         self.name = name
# stu = Student("Kinney")
# stu.work()

# 构造函数的例子
# class Person():
#     # 对Person类进行实例化的时候
#     # 姓名要确定
#     # 年龄得确定
#     # 地址肯定有
#     def __init__(self):
#         self.name = "none"
#         self.age = 18
#         self.address = "xi'an"
#         print("666")
# # 实例化一个人
# p = Person()
# print(p)
class a():
    pass
s = a()
print(dir(s))
print("*"*20)
print(dir(a))