def check_for_word():
    word = "learning"
    with open("Chapter_7/Pratice/pratice.txt", "r") as f:
        data = f.read()
        if(word in data):
             print("Found")
        else:
             print("Not found")

check_for_word()
     