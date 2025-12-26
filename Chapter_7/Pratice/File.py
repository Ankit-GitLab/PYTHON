with open("Chapter_7\Pratice/pratice.txt", "r") as f:
   data = f.read()

new_data = data.replace("java", "python")
print(new_data)

with open("Chapter_7\Pratice/pratice.txt", "w") as f:
    f.write(new_data)
