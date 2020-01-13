class Student:
    # def __init__(self, name,program,gpa,is_on_probation):
    def __init__(self, name,program,gpa):
        self.name = name #student name is gonna be the name we passed
        self.program = program #student program is gonna be the program we passed
        self.gpa = gpa #student gpa is gonna be the gpa we passed
        # self.is_on_probation = is_on_probation

    def is_first_class(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False