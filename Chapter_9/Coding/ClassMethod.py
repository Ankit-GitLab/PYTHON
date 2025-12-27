class Person:
    name = "Ankit"

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("Ankit Sharma")

print(p1.name)
print(Person.name)
