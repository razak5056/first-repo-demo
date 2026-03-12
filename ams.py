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
    if i==sum:
         print(f"{i} is  amstrong number...")
         break
    else:
        print(f"There is no amstrong numbers between {lower_number} and {upper_number}")
      
         

