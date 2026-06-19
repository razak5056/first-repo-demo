# start_value=int(input("enter the start value:"))
# end_value=int(input("enter the end value:"))

# for i in range(2,21):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i,end=" ")


n=int(input("enter the vlaue:"))
i=1
while i <=n:
    j=2
    while j < i:
        if i%j == 0:
            print(i,"is not a prime number")
            break

        j=j+1
    else:
        print(i,"is a prime number")
    i=i+1

