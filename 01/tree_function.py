def tree():
    global rows
    rows = int(input("Enter the lenght of tree you want: "))
    for i in range(0,rows):
        star_per_row = (1+(2*i))*"*"
        print((rows-i-1)*" "+star_per_row+(rows-i-1)*" ")
tree()
def log():
    for i in range(2):
        print(" "*(rows-2)+"***"+" "*(rows-1))
log()