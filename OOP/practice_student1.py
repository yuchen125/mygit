class Student(object):
    def __init__(self, name, age, scores):
        self.name = name
        self.age = age
        self.scores = scores

    def get_name(self):
        return  self.name

    def get_age(self):
        return self.age

    def get_course(self):
        return max(self.scores)

kinney = Student("kinney", 18, [80, 90, 95])
print(kinney.get_name())
print(kinney.get_age())
print(kinney.get_course())