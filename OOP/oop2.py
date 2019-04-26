class Student():
    name = 'yue yue'
    age = 18

    # 注意say的写法，参数有一个self
    def say(self):
        self.name = 'ming ming'
        self.age = 20
        print("My name is {0}".format(self.name))
        print("My age is {0}".format(__class__.age))

    def v(self):
        print(__class__.name)
        print(__class__.age)
        print('hello')


class A():
    name = 'tuling'
    age = 16

    def __init__(self):
        self.name = 'aaaa'
        self.age = 200

    def say(self):
        print(self.name)
        print(self.age)


class B():
    name = 'bbbb'
    age = 90


# 此时，系统会默认吧a作为第一个参数传入函数
a = A()
a.say()

# 此时，self被a替换
A.say(a)

# 此时，传入的是实例B，因为B具有name和age属性，所以不会报错
A.say(B)

# 以上代码，利用了鸭子模型
# print(Student.name)
# print(Student.age)
#
# print('*' * 20)
#
# print(id(Student.name))
# print(id(Student.age))
#
# print('*' * 20)
# s = Student()
# s.age = 20
# s.name = 'li si'
# print(s.__dict__)
# for k, v in s.__dict__.items():
#     print('{} : {}'.format(k, v))

# y = Student()
# print(y.say())
