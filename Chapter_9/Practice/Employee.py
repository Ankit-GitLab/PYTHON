class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
        
    def showDetails(self):
        print("role = ",self.role)
        print("dept = ",self.dept)
        print("salary = ",self.salary)

e1 = Employee("accountant", "Finance", "60,000")
#e1.showDetails()

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Software Engineer", "IT", 60000)

engg1 = Engineer("Ankit", 19)
engg1.showDetails()
