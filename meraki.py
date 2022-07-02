# # MERAKI QUESTION6=PART=1
# def calculator(number_x,number_y,operation):
#     if operation=="add":
#         print(number_x+number_y)
#     elif operation=="subtract":
#         print(number_x-number_y)
#     elif operation=="multiply":
#         print(number_x*number_y)
#     elif operation=="divide":
#         print(number_x/number_y)
# number_x=int(input(" enter number: "))
# number_y=int(input(" enter number: "))
# operation=input(" enter operation: ")
# calculator(number_x,number_y,operation)
# calculator
# # scope of variable
# # python inner function
# def first_function():
#  s = 'I love India'
#  def second_function():
#   print(s)  
#  second_function()
# first_function()
# def first_function():
#  s = 'I love India'
#  def second_function():
#   s = "MY NAME IS JACK"
#   print(s)  
#  second_function()
#  print(s) 
 
# first_function()
# #MERAKI QUESTION 9
# def showNumber(limit):
#     i=0
#     while i<=limit:
#         if i%2==0:
#             print(i,"even")
#         else:
#             print(i,"odd")
#         i+=1
# limit=int(input("enter number:"))
# showNumber(limit)
# def vote(age):
#     if age>=18:
#         print("you are eligible")
#     else:
#         print("not eligible")
# age=int(input("enter your age:"))
# vote(age)
# #MERAKI QUESTION 8
# def num(first,second,third):
#     sum=first+second+third
#     avg=sum/3
#     print("sum of three numbers=",sum)
#     print("average of three numbers=",avg)
# first=int(input("enter first number"))
# second=int(input("enter second number"))
# third=int(input("enter third numner"))
# num(first,second,third)
# #MERAKI QUESTION 10
# def number(limit):
#     i=0
#     sum=0
#     while i<=limit:
#         if i%3==0 or i%5==0:
#             sum=sum+i
#         i+=1
#     print("sum",sum)
# limit=int(input("enter number:"))
# number(limit)

# def myMax(list1):
#     max = list1[0]
#     for x in list1:
#         if x > max :
#              max = x
#     return max
# a = [3, 5, 7, 34, 2, 89, 2, 5]
# print("Largest element is:", max(a))
list1 = [1,2, 3, 4,5]
def sumOfList(list, size):
   if (size == 0):
     return 0
   else:
     return list[size - 1] + sumOfList(list, size - 1)
  
  
total = sumOfList(list1, len(list1))
 
print("Sum of all elements in given list: ", total)




