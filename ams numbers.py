lower_number=int(input("enter the lower number:"))
upper_number=int(input("enter the upper number:"))
for i in range(lower_number,upper_number+1):
    l1=len(str(i))
    sum=0
    temp=i
    while temp>0:
        d=temp%10
        sum=sum+d**l1
        temp=temp//10
    if i!=sum:
         print("{} is not a amstrong number...".format(i))
    else:
         print("{} is a amstrong number...".format(i))
         