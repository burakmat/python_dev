sec=int(input("Enter number of seconds:"))
n=sec//86400
sec-=n*86400
m=sec//3600
sec-=m*3600
k=sec//60
sec-=k*60
print("{} day(s), {} hour(s), {} minute(s), and {} second(s).".format(n,m,k,sec))