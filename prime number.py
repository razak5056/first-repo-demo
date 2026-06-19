# n=int(input("Enter the number:"))
# if n<=1:
#     print("================================")
#     print(" you entered Invalid input")
# else:
#     result=False
#     print("=============================")
#     for i in range(2,n):
#         if n%i==0:
#             result=True
#             break
#     if result:
#         print("\t{} is not a prime number".format(n))
#     else:
#         print("\t{} is a primr number".format(n))
# print("================================")
n=5
p=1
while n>0:
    p=p*n    
    n=n-1
print(p)
