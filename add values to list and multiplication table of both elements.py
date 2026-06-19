# list=[1,2,3,4]
# for i in list:
#     print(i)
#     for j in range(1,11):
#         print("{} x {} = {}".format(i,j,i*j))


n=int(input("enter the how mant val you want to enter:"))
if n<=0:
    print("invalid input")
else:
    lst=[]
    for i in range(1,n+1):
        n1=int(input("enter the values into the lst:"))
        lst.append(n1) 
    else:
        print("elements in the list are:{}".format(lst))
        # print("------------------------------------------")
        for n in lst:
            if n<=0:
                print("invalid input")
            else:
                print("--------------------------------------")
                print("multiplication table of {} is ".format(n))
                print("---------------------------------------------")
                for i in range(1,11):
                     print("\t{} X {} = {} ".format(n,i,n*i))


                     



# n=int(input("enter the end value:"))
# for i in range(1,n+1):
#     print("************************************************************************************")
#     print("\tMULTIPLICATION TABLE OF {} IS ".format(i))
#     print("************************************************************************************")
#     for j in range(1,10):
#         print("\t{} X {} = {} ".format(i,j,i*j))
# # else:
# #     print("hello "*30)