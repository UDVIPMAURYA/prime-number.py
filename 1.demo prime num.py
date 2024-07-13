num=int(input("enter any num :"))
c=0
for i in range (2,num+1):
    if (num%i==0):
        c=c+1
if (c==1):
    print (num," is prime num .")
else:
    print (num," is not a prime num. ")
        