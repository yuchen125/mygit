# class Person():
#     def __init__(self):
#         self.name = "kinney"
#         self.age = 18
#
#     # 函数的名称可以任意
#     # 此功能，是对类变量进行读取操作的时候应该执行的函数功能
#     def fget(self):
#         print("fget")
#         return self.name
#
#     # 此功能，模拟的是对变量进行写操作的时候执行的功能
#     def fset(self, name):
#         # 所有输入的姓名以大写形式保存
#         print("fset")
#         self._name = "图灵学院：" + name
#
#     # fdel 模拟的是删除变量的时候进行的操作
#     def fdel(self):
#         pass
#     # property的四个参数顺序是固定的
#     number = property(fget, fset, fdel,"对number进行的操作")
#
# p1 = Person()
# print(p1.name)
# print(p1.number)


# # 抽象
# class Animal():
#
#     def sayHello(self):
#         pass
#
# class Dog(Animal):
#
#     def sayHello(self):
#         print("闻")
#
# class Person(Animal):
#
#     def sayHello(self):
#         print("kiss")


# 抽象类的实现

# import  abc
# # 声明一个类并且指定当前类的元类
# class Human(metaclass=abc.ABCMeta):
#
#     # 定义一个抽象的方法
#     @abc.abstractmethod
#     def smoking(self):
#         pass
#
#     # 定义类的抽象方法
#     @classmethod
#     def drink(self):
#         pass
#
#     # 定义静态抽象方法
#     @staticmethod
#     def play():
#         pass

# # 自己组装一个类
# # 组装类例子 1
# class A():
#     pass
#
# def say(self):
#     print("Saying......")
#
# print(say(9))
# A.say = say
#
# a = A()
# print(a.say())


# # 组装类例子 2
# from types import MethodType
#
# class A():
#     pass
#
# def say(self):
#     print("Saying......")
#
# a = A()
# a.say = MethodType(say, A)
# print(a.say())
# help(MethodType)


# # 利用type造一个类
#
# # 先定义类应该具有的成员函数
# def say(self):
#     print("Saying.......")
#
# def talk(self):
#     print("Talking......")
#
# # 用type来创建一个类
# A = type("AName",(object,),{"class_say":say,"class_talk":talk})
# # 然后可以像正常访问一样使用类
# a = A()
# print(a.class_say())


# 元类是类
# 元类写法是固定的，他必须继承于type
# 元类一般是以MateClass结尾
class KinneyMetaClass(type):
    # 注意以下写法
    def __new__(cls, name, bases, attrs):
        # 自己的业务处理
        print("哈哈，我是元类呀")
        attrs['id'] = '9527'
        attrs['addr'] = '西安'
        return type.__new__(cls, name ,bases, attrs)

# 元类定义完就可以使用，使用注意写法
class Teacher(object,metaclass=KinneyMetaClass):
    pass

t = Teacher()
print(t.id)