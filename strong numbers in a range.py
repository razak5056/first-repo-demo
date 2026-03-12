n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
for i in range(n1,n2+1):
    sum1=0
    while i>0:
       dit=i%10
       j=1
       f=1
       while j<=dit:
          f=f*j
          j=j+1
       sum1=sum1+f
       i=i//10
    print(sum1)

    



