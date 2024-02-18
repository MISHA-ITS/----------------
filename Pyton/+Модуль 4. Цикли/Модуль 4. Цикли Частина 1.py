# Завдання 1

number1 = int(input("\tEnter your first number: "))
number2 = int(input("\tEnter your last number: "))
print (f"\tAll numbers in the range from {number1} to {number2} are multiples of seven:", end=" ")
i=number1
n=0
while i<=number2:
  if i%7==0:
    n+=1
    print (i, end=", ")
  i+=1
if n==0:
  print ("no numbers!!!")

# Завдання 2

number1 = int(input("\tEnter your first number: "))
number2 = int(input("\tEnter your last number: "))

print (f"\n -\tall numbers in the range from {number1} to {number2}:", end=" ")
for i in range (number1, number2+1):
  print (i, end=", ")

print (f"\n -\tall numbers in the range from {number2} to {number1}:", end=" ")
for i in range (number2, number1-1,-1):
  print (i, end=", ")

print (f"\n -\tall numbers in the range from {number1} to {number2} are multiples of seven:", end=" ")
n=0
for i in range (number1, number2+1):
  if i%7==0:
    print (i, end=", ")
    n+=1
if n==0:
  print ("no numbers!!!", end="")

n=0
for i in range (number1, number2+1):
  if i%5==0:
    n+=1
print (f"\n -\tnumber of numbers that are multiples of 5 in the range from {number1} to {number2}: {n}.")

# Завдання 3

number1 = int(input("\tEnter your first number: "))
number2 = int(input("\tEnter your last number: "))
for i in range (number1, number2+1):
  if i%3==0 and i%5==0:
    print ("Fizz Buzz", end=", ")
  elif i%3==0:
    print ("Fizz", end=", ")
  elif i%5==0:
    print ("Buzz", end=", ")
  else:
    print (i, end=", ")