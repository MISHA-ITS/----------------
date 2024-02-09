# Завдання 1

while True:
  number1 = int(input("\tEnter your first number: "))
  number2 = int(input("\tEnter your last number: "))

  if number1==number2:
    print("Please, enter different numbers!!!")
    continue
  
  n=0
  c=0
  print ("\n\tEven numbers range:", end=" ") 
  for i in range (number1, number2+1):
    if i%2==0:
      print (i, end=", ")
      n+=i
      c+=1
  print (f"\n -\ttheir sum is equal: {n}, \n -\ttheir average arithmetic value is equal: {n}/{c}={n/c}.")

  n=0
  c=0
  print ("\n\tOdd numbers range:", end=" ") 
  for i in range (number1, number2+1):
    if i%2!=0:
      print (i, end=", ")
      n+=i
      c+=1
  print (f"\n -\ttheir sum is equal: {n}, \n -\ttheir average arithmetic value is equal: {n}/{c}={n/c}.")

  i=number1
  n=0
  с=0
  print ("\n\tRange numbers are multiples of nine:", end=" ") 
  while i<=number2:
    if i%9==0:
      n += i
      с += 1
      if с!=0:
        print (i, end=",")
    i += 1
  if с!=0:
    print (f"\n -\ttheir sum is equal: {n}, \n -\ttheir average arithmetic value is equal: {n}/{c}={n/c}.")
    break
  else:
    print ("no numbers!")
    break

# Завдання 2

l=int(input("Enter your line length: "))
while True:
  if l<=0:
    l=int(input("The length must be greater than zero!!! Please, enter a positive number: "))
    continue
  else:
    s=input("Enter your symbol: ")
    for i in range (0, l):
      print (s)
  break

# Завдання 3

while True:
  number=int(input("Enter your number:"))
  if number==7:
    print ("Good bye!")
    break
  elif number>0:
    print ("Number is positive.")
  elif number<0:
    print ("Number is negative.")
  else:
    print ("Number is equal to zero.")

# Завдання 4

number=int(input("\tEnter your first number: "))
sum=number
min=number
max=number
while True:
  if number==7:
    print ("Good bye!")
    break
  else:
    print(f"-\tthe maximum number: {max};\n-\tthe minimum number: {min};\n-\tthe sum of the numbers: {sum}.")
  number=int(input("\n\tNext number: "))
  if number>max:
    max=number
  elif number<min:
    min=number
  sum+=number