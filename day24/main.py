with open("./text.txt","r") as file:
    read = file.read()
    print(read)
# file = open("text.txt")
# print(file.read())
# file.close()

# print(file)
hs=15
with open("text.txt","w") as file:
    file.write(str(hs))