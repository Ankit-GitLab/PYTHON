marks = {}

x = int(input("Enter phy marks : "))
marks.update({"phy" : x})
y = int(input("Enter chem marks : "))
marks.update({"chem" : y})
z = int(input("Enter math marks : "))
marks.update({"math" : z})

print(marks)
