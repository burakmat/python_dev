a="aaBcDeF"
print(a.lower())
print(a.upper())
print(a.rjust(10,"'"))
print(a.ljust(10,"'"))
print(a.center(10,"2"))
print(a.center(10,"2").strip("2"))
print(a.startswith("a",1)) #checks out if the first letter is same with the input entered (and so on if integer entered) and gives a boolean value
print(a.endswith("eF"))
print(type(a.count("a",1,2))) #checks out whether there is a given string in variable for a given interval(optional)
print(a.find("a",0,5)) #finds the position of the given str in given interval(optional)
print("{}".format(a))
