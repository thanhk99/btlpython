from student import Student
class EnStudent(Student):
    def __init__(self, name, cccd, local, phone, leangue):
        super().__init__(name, cccd, local, phone, leangue)
        self.leangue = leangue