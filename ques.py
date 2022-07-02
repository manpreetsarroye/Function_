# In computer programming, a function is a named section of a code that
#  performs a specific task. This typically involves taking some input, manipulating the input and returning an output.04-Sept-2020

QUESTION 1
# # def message():
# #     print("hello python")
# # message()

# # # #QUESTION 2
# # def add():
# #     a=int(input("enter no.1"))
# #     b=int(input("enter no.2"))
# #     c=a+b
# #     print("Addition=",c)
# # # add()

# # # #QUESTION 3
# # def sub():
# #     a=int(input("enter bigger no.then secound no."))
# #     b=int(input("enterv smaller no. then pre no."))
# #     c=a-b
# #     print("subractiion=",c)
# # sub()

# # # #QUESTION 4
# # #THIS QUESTION IS WITH ARGUMENTS
# # def add(a,b):
# #     c=a+b
# #     print("Addition=",c)
# # a=int(input("enter no."))
# # b=int(input("enter second no."))
# # add(a,b)

# #SAME AS QUESTION 4
# def add(a,b):
#     c=a+b
#     print("Addition=",c)
# add(5,10)

# #QUESTION 6 ODD EVEN WITHOUT ARGUMENT
# def oddeve():
#     a=int(input("enter no."))
#     if a%2==0:
#         print("even")
#     else:
#         print("odd")
# oddeve()

# #SAME QUESTION BUT WITH ARGUMENT
# def oddeve(a):
#     if a%2==0:
#         print("even")
#     else:
#         print("odd")
# a=int(input("enter no."))
# oddeve(a)

# def sum():
# 	a=[1,2,5,8,9,3,4]
# 	i=0
# 	odd=0
# 	even=0
# 	while i<len(a):
# 		if a[i]%2==0:
# 			even=even+a[i]
# 		else:
# 			odd=odd+a[i]
# 		i+=1
# 	print('even=',even)
# 	print('odd=',odd)
# # sum()

# def add():
# 	a=int(input('enter no.'))
# 	b=int(input('enter no.'))
# 	c=a+b
# 	print('addition=',c)
# add()
# print('programme completed sucessfully')
# def add(a,b):
#     c=a+b
#     return(c)
# a=int(input("enter no."))
# b=int(input("enter no."))
# z=add(a,b)
# print("Addition=",z)
# def add(a,b):
#     c=a+b
#     print("addition=",c)
# add(5,6)
# def add(a,b=5):
#     c=a+b
#     print("Addition=",c)
# add(10)
# def interest(prin,rate,time)
#     i=(prin+time*rate)/100
#     print("Interest=",i)
# # interest(5000,10,2)
# interest(time=2,prin=5000,rate=10)
# numbers = [3, 5, 7, 34, 2, 89, 2, 5]
# def big():
#     c=max(numbers)
#     print("max no.=",c)
# def ask_question():
#     print("ek baar")
# ask_question()
# print("NavGurukul")

# def say_hello():
#  print("Hello!")
#  print("Aap kaise ho?")

# say_hello()
# print("Python is awesome")
# say_hello()
# print("Hello…")
# say_hello()
# reverse_list = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
# def rev():
#     reverse_list.reverse()
#     print("Reverse list=",reverse_list)
# rev()
# def accending():
#     unorder_list.sort()
#     print("SORTED LIST=",unorder_list)
# accending()
# def sum():
#     i=0
#     total_sum=0
#     while i<len(numbers):
#         total_sum=total_sum+numbers[i]
#         i+=1
#     print("sum=",total_sum)
# sum()
# def welcome():
#  print("Welcome to function")
# welcome()
# list = [8, 6, 4, 8, 4, 50, 2, 7]
# def minimum():
#     small=min(list)
#     print("Minimum no.=",small)
# minimum()
# def sum():
#  print(12+13)
# sum()\
# def isEven():
#  if(12%2==0):
#   print("Even Number")
#  else:
#   print("Old Number")
# isEven()
# def say_hello_people(name_x, name_y, name_z, name_a):
#  print("Namaste ", name_x) # hindi mein
#  print("Alah hafiz ", name_y) # urdu mein
#  print("Bonjour ", name_z) # french mein
#  print("Hello ", name_a) # english mein
# say_hello_people("Imitiyaz", "Rishabh", "Rahul", "Vidya")
# say_hello_people("Steve", "Saswata", "Shakrundin", "Rajeev")
# def icecream(*flavours):
#  for flavour in flavours:
#   print("i love"+flavour)

# icecream("chocolate", "butterscotch","vanilla","strawberry")
# def attendance(name,status="absent"):
#  print(name,"is",status," today")

# attendance("kartik","present")
# attendance("sonu")
# attendance("vishal","present")
# attendance("umesh")
# def say_hello_language(name, language):
#  if language == "hindi":
#   print("Namaste ", name)
#   print("Aap kaise ho?")
#  elif language == "punjabi":
#   print("Sat sri akaal ", name)
#   print("Tuhada ki haal hai?")
#  else:
#   print("Hello ", name)
#   print("How are you?")
# say_hello_language("Rishabh", "punjabi")
# say_hello_language("Armaan", "english")
# say_hello_language("Abhishek", "french")
# say_hello_language("Kavay", "hindi")
# default argument
# def greet(*names):
#  for name in names:
#   print("Welcome", name)


# greet("Rinki", "Vishal", "Kartik", "Bijender")
# def info(name, age ='5'):
#    print(name + " is " + age + " years old")

# info("Sonu")
# info("Sana", "17")
# info("Umesh", "18")
# def sum(a,b):
# 	res=[]
# 	i=0
# 	while i<len(a):
# 		res.append(a[i]+b[i])
# 		i=i+1
# 	print(res)
# a=[50, 60, 10] 
# b=[10, 20, 13]
# sum(a,b)
# def check_number(a,b):
#     if a%2==0 and b%2==0:
#         print("dono even hai")
#     else:
#         print("dono even nhi hai")
# a=int(input("enter no."))
# b=int(input("enter no."))
# check_number(a,b)
# def studentDetails(name,currentMilestone,mentorName):
#  print("Hello " , name, "your" , currentMilestone, "concept " , "is clear with the help of ", mentorName)


# studentDetails("Nilam","loop","Ayushi")
# def function_print_line(name):
#     print("mera naam"+" "+name+" "+"hai")
# function_print_line("rishabh")
# print("mai navgurukul ka co-founder hu")