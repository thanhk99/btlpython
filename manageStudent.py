class ManageStudent :
    def __init__(self):
        self.studentList = []
    def addStudent(self, student):
        self.studentList.append(student)
    def removeStudent(self, student):
        self.studentList.remove(student)
    def showStudent(self):
        for student in self.studentList:
            print(student)