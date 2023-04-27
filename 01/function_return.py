
def is_prime(num):
    b=0
    for a in range(1, num+1):
        if num%a==0:
            b+=1
    print(id(num))
    return b


num = int(input("Enter an integer:"))

print (id(num))
#print(b) undefined error
print("True" if is_prime(num)==2 else "False")

