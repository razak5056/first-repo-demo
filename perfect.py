# n=int(input("Enter the number:"))
# sum=0
# print(f"The divisibles of {n} are:")
# for i in range(1,n):
#     if n%i == 0:
#         print(i)
#         sum=sum+i
# if sum == n:
#     print(f"{n} is a perfect number")
# else:
#     print(f"{n} is not a perfect number")




# n1=int(input("Enter the start number:"))
# n2=int(input("Enter the end number:"))
# sum=0
# for i in range(n1,n2+1):
#     for j in range(1,i):
#         if i%j == 0:
#             sum=sum+j


# word=input("Enter the word:")
# v=["a","e","i","o","u"]

# for i in word:
#     for j in v:
#         if i == j :
#             res="yes,word contains vowel"
# print(res)


# outer=['a','b']
# inner=[1,2,3]
# i=0
# while i<len(outer):
#     j=0
#     while j<len(inner):
#         print(outer[i],inner[j])
#         j=j+1
#     i=i+1


# chars=['x','y']
# nums=[1,2,3]
# i=0
# while i<len(chars):
#     j=0
#     while j<len(nums):
#         print(chars[i],nums[j])
#         j=j+1
#     i=i+1


# def std_marks():
#     i=1
#     while i<=5:
#         std_name=input("Enter the student name:")
#         python_marks=int(input("enter the marks in python:"))
#         java_marks=int(input("Enter the marks in java:"))
#         ml_marks=int(input("Enter the marks in machine learning:"))
#         if python_marks>=75 and java_marks>=75 and ml_marks>=75 :
#             print(f"{std_name} passed in the examination")
#         else:
#             print(f"{std_name} faild in the examination")
#         total_marks=python_marks+java_marks+ml_marks
#         print(f"{std_name}s  total marks are {total_marks}")
#     i=i+1
# std_marks()



# stdno=int(input("enter the student number :"))
# stdname=input("enter the student name:")
# while True:
#     cm=int(input("enter the marks in cm:"))
#     if cm>=0 and cm<=100:
#         break
#     print("Invalid marks")
# while True:
#     cppm=int(input("enter the marks in cpp:"))
#     if cppm>=0 and cppm<=100:
#         break
#     print("Invalid marks")
# while True:
#     pythonm=int(input("enter the marks in python:"))
#     if pythonm>=0 and pythonm<=100:
#         break
#     print("Invalid marks")
# total_marks_std=cm+cppm+pythonm
# percentage=(total_marks_std/300)*100
# if cm<40 or cppm<40 or pythonm<40:
#     grade="FAIL IN THE EXAM"
# elif total_marks_std<=300 and total_marks_std>=250:
#     grade="PASSED WITH DISTICTION"
# elif total_marks_std<=249 and total_marks_std>=200:
#     grade="PASSED WITH FIIRST CLASS"
# elif total_marks_std<=199 and total_marks_std>=150:
#      grade=" PASSED WITH SECOND CLASS"
# elif total_marks_std<=149 and total_marks_std>=120:
#     grade="PASSED WITH THIRD CLASS"
# print("===========================")
# print("STUDENT MARKS MEMO")
# print("===========================")
# print(f"STUDENT NUMBER:{stdno}")
# print(f"STUDENT NAME:{stdname}")
# print(f"MARKS IN C:{cm}")
# print(f"MARKS IN CPP:{cppm}")
# print(f"MARKS IN PYTHON:{pythonm}")
# print(f"PER OF THE STUDENT IS:{percentage}")
# print(f"STUDENT IS:{grade}")




