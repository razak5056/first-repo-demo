n=int(input("enter how many values you want:"))
if n<0:
    print("{} is invalid input".format(n))
else:
    list=[]
    for i in range(1,n+1):
        n1=input("enter {} values=".format(i))
        list.append(n1)
    print("list of elements are={}".format(list))
    
