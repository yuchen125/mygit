Course_list = []

class School(object):
    def __init__(self, school_name):
        self.school_name = school_name
        self.students_list = []
        self.teachers_list = []
        global Course_list

    def hire(self, obj):
        self.teachers_list.append(obj.name)
        print("我们现在聘请了一个新老师{0}".format(obj.name))

    def enroll(self, obj):
        self.students_list.append((obj.name))
        print("我们又有了一个新学员{0}".format(obj.name))

class Grade(School):
    def __init__(self, school_name, grade_code, grade_course):
        super().__init__(school_name)
        self.code = grade_code
        self.course = grade_course
        self.numbers = []
        Course_list.append(self.course)

        print("我们现在有了{}的{}的{}".format(self.school_name, self.code, self.course))

    def course_info(self):
        print("课程大纲{}是day01,day02,day03".format(self.course))


Python = Grade("北京", 3, "Python")
Linux = Grade("成都", 1, "Linux")


class School_member(object):
    def __init__(self, name, age, sex, role):
        self.name = name
        self.age = age
        self.sex = sex
        self.role = role
        self.course_list = []

        print("我叫{}，我是一个{}".format(self.name, self.role))

stu_num_id = 0
class Students(School_member):
    def __init__(self, name, age, sex, role, course):
        super().__init__(name, age, sex, role)
        global  stu_num_id
        stu_num_id += 1
        stu_id = course.school_name + 'S' + str(course.code) + str(stu_num_id).zfill(2)
        # zfill 填充的作用，当只有一位数是前面填充0， 只能对str类型做操作

        self.id = stu_id
        self.mark_list = {}

    def study(self, course):
        print("我来这里学习{}课，我的学号是{}".format(course.course,self.id))

    def pry(self, course):
        print("我交1000块，给{}".format(course.course))
        self.course_list.append(course.course)

    def praise(self, obj):
        print("{}觉得{}真棒".format(self.name, obj.name))

    def mark_check(self):
        for i in self.mark_list.items():
            print(i)

    def out(self):
        print("我离开了")


tea_num_id = 0
class Teachers(School_member):
    def __init__(self, name, age, sex, role, course):
        super().__init__(name, age, sex, role)
        global tea_num_id
        tea_num_id += 1
        tea_id = course.school_name + 'T' + str(course.code) + str(tea_num_id).zfill(2)
        self.id = tea_id

    def teach(self,course):
        print("我来这里讲{}门课，我的ID是{}".format(course.course,self.id))

    def record_mark(self, Date, course, obj, level):
        obj.mark_list['Day' + Date] = level

a = Students("小张",18,"M","student",Python)
Python.enroll(a)
a.study(Python)
a.pry(Python)

b = Students("小王", 22, "F", "student", Python)
Python.enroll(b)
b.study(Python)
b.pry(Python)

c = Teachers("小周", 30, 'M', "teacher", Python)
Python.hire(c)
c.teach(Python)
c.record_mark("1", Python, a, "A")
c.record_mark("1", Python, b, "B")
c.record_mark("2", Python, a, "B")
c.record_mark("2", Python, b, "A")
print("小王查看了自己的课程")
print(b.course_list)
print("小王查看了自己的成绩")
b.mark_check()
print("小王退出了")
b.out()
print("给好评")
a.praise(c)
