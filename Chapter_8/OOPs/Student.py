class Student:
    
    #default constructors
    def __init__(self):
        pass

    
    #parameterized constructors
    college_name = "Saitm"
    name = "Ankit"#class attr

    def __init__(self, name, marks):
        self.name = name #obj attr > class attr
        self.marks = marks
        print("adding new student in Database....")

s1 = Student("Ankit kumar",97)
print(s1.name, s1.marks,s1.college_name)


s2 = Student("Ravi",79)
print(s2.name, s2.marks, s2.college_name)