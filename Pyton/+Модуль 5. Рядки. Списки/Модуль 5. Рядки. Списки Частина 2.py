#Завдання 1

exp=input("\tEnter your arithmetic expression: ")
for i in exp:
  if i in '+-*/':
    operator=i
    break
numbers=exp.split(operator)
if operator=="+":
  print(f"Your sum is equal to {int(numbers[0])+int(numbers[1])}.")
elif operator=="-":
  print(f"Your difference is equal to {int(numbers[0])-int(numbers[1])}.")
elif operator=="*":
  print(f"Your product is equal to {int(numbers[0])*int(numbers[1])}.")
else:
  if int(numbers[1])!=0:
    print(f"Your quotient is equal to {int(numbers[0])/int(numbers[1])}.")
  else:
    print("Error: division by zero!!!")

#Завдання 2

import random

minvalue=int(input("\tEnter the minimum value: "))
maxvalue=int(input("\tEnter the maximum value: "))
k=int(input("\tEnter the number of elements: "))
list=[random.randint(minvalue,maxvalue) for i in range(k)]
print(f"\n\tList: {list}.")
print(f"\n -\tthe maximum element of the list: {max(list)};")
print(f" -\tthe minimum element of the list: {min(list)};")
n=0
for i in list:
  if i<0:
      n+=1
print(f" -\tthe number of negative list elements: {n};")
n=0
for i in list:
  if i>0:
    n+=1
print(f" -\tthe number of positive list elements: {n};")
n=0
for i in list:
  if i==0:
    n+=1
print(f" -\tthe number of zeros in the list: {n}.")