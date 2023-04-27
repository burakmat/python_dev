lines=int(input("Enter number of lines for pattern:"))
for i in range(lines):
	print(" "*(lines-i-1)+"#"+" "*2*i+"#")