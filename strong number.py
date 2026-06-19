n=int(input("enter the number:"))
temp=n
sum1=0
while temp>0:
    d=temp%10
    i=1
    f=1
    while i<=d:
        f=f*i
        i=i+1
    sum1=sum1+f
    temp=temp//10
if sum1==n:
    print("The number is a strong number....")
else:
    print("The number is not a strong number....")




