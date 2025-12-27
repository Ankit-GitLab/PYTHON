class Complex:
    #Constructor of class
    def __init__(self,real,img):
        self.real = real
        self.img = img

    # to print the complex number
    def showNumber(self):
        print(self.real,"i +",self.img,"j")

    # add two complex number using the dunder function
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

    # subratact two complex number using the dunder function
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)

#object of the Complex class
num1 = Complex(1,3)
num1.showNumber()

#print the complex number
num2 = Complex(-2,8)
num2.showNumber()

#add the complex number call from there
num3 = num1 + num2
num3.showNumber()

#subratact the complex number call from there
num3 = num1 - num2
num3.showNumber()