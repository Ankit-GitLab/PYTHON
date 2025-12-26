class Student:
    
    #parameterized constructors
    college_name = "Saitm"


    def __init__(self, name, marks):
        self.name = name #obj attr > class attr
        self.marks = marks

    def welcome(self):
        print("Welcome, Ankit",self.name)
    
    def get_marks(self):
        return self.marks



s1 = Student("Ankit kumar",97)
s1.welcome()
print(s1.get_marks())
