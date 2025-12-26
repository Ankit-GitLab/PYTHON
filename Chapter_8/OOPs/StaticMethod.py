class Student:

    
    #parameterized constructors
    def __init__(self, name, marks):
        self.name = name #obj attr > class attr
        self.marks = marks

    @staticmethod
    def hello():
        print("Hello, Ankit")
        

s1 = Student("Ankit kumar",97)
print(s1.name, s1.marks)
s1.hello()


