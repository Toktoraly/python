class Teacher():
    since = ""
    def __init__ (self,since):
        self.since = since
class Student():
    sinces = []
    def set_since(self,predmet):
        self.sinces.append(predmet)
        return self.get_since()

    def get_since(self):
        return ", ".join(self.sinces)

teacher1 = Teacher("math")
teacher2 = Teacher("fizik")
teacher3 = Teacher("it")

student = Student()
student.set_since(teacher1.since)
student.set_since(teacher2.since)
student.set_since(teacher3.since)

print(student.get_since())
print(student.sinces)class Teacher():
    since = ""
    def __init__ (self,since):
        self.since = since
class Student():
    sinces = []
    def set_since(self,predmet):
        self.sinces.append(predmet)
        return self.get_since()

    def get_since(self):
        return ", ".join(self.sinces)

teacher1 = Teacher("math")
teacher2 = Teacher("fizik")
teacher3 = Teacher("it")

student = Student()
student.set_since(teacher1.since)
student.set_since(teacher2.since)
student.set_since(teacher3.since)

print(student.get_since())
print(student.sinces)