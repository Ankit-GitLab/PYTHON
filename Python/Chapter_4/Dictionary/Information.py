info = {
    "key" : "Value",
    "name" : "Ankit",
    "subject" : ["python", "C", "HTML", "CSS", "JAVA", "DSA"],
    "tuple" : ("Dictionary","Set"),
    "age" : 19,
    "is_adult" : True,
    "marks" : 94.2
}
#print(info)
print(info["name"])
print(info["tuple"])
print(info["subject"])
print(info["marks"])

info["name"] = "Ankit sharma"
print(info["name"])

info["surname"] = "Sharma"
print(info)