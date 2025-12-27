class Person:
    __name = "Ankit"

    def __hello(self):
        print("Hello person!")

    def welcome(self):
        self.__hello()

p1 = Person()

print(p1.welcome())
