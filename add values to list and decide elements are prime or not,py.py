n=int(input("enter how  many elements you want to add to the list:"))
if n<=0:
    print("invalid input")
else:
    list=[]
    print("=======================================================")
    for i in range(1,n+1):
        val=int(input("enter the values to the list:"))
        list.append(val)
    else:
        print("list of values are={}".format(list))
        for n in list:
            if n<=0:
                print("{} is invalid input".format(n))
            else:
                result=False
                for i in range(2,n):
                    if n%i==0:
                        result=True
                        break
                        # lst50.append(n) 
                # else:
                #     print("the list of even numbers are=".format(lst50))      
                if result:
                    print("{} is not prime number".format(n))
                    
                else:
                    print("{} is a prime number".format(n))




                 
             
            

