from math import prod
import random

ListOfNums=[random.randint(1,20) for i in range(5)]
ListOfNums2=[random.randint(21,40) for i in range(5)]
print("List of integers 1:", ListOfNums)
print("List of integers 2:", ListOfNums2)

#Завдання 1

def FindProdOfList1(ListOfNums):
  Prod=1
  for i in ListOfNums:
    Prod=Prod*i
  return Prod

#або

def FindProdOfList2(ListOfNums):
  return prod(ListOfNums)

#або

def FindProdOfList3(ListOfNums):
  return lambda ListOfNums: prod(ListOfNums)

#Перевірка:

# print(ListOfNums)
print("\nThe product of the elements of list 1 (var.1):", FindProdOfList1(ListOfNums))
print("The product of the elements of list 2 (var.2):", FindProdOfList2(ListOfNums))
print("The product of the elements of list 3 (var.3):", FindProdOfList3(ListOfNums))

#Завдання 2

def FindMinOfList1(ListOfNums):
  Min = ListOfNums[0]
  for i in ListOfNums:
    if i < Min:
      Min = i
  return Min

#або

def FindMinOfList2(ListOfNums):
  return min(ListOfNums)

#або

def FindMinOfList3(ListOfNums):
  return lambda ListOfNums: min(ListOfNums)

#Перевірка:

# ListOfNums=[random.randint(1,100) for i in range(10)]
# print(ListOfNums)
print("\nMin of list (var.1):", FindMinOfList1(ListOfNums))
print("Min of list (var.2):", FindMinOfList2(ListOfNums))
print("Min of list (var.3):", FindMinOfList3(ListOfNums))

#Завдання 3

def NumOfPrimes(ListOfNums):
  count = 0
  for i in ListOfNums:
    if i < 2:
      continue
    for j in range(2, i):
      if i % j == 0:
        break
    else:
      count += 1
  return count

#Перевірка:

# ListOfNums=[random.randint(1,10) for i in range(10)]
# print("\nList of integers:", ListOfNums)
print("\nThe number of primes in this list 1:", NumOfPrimes(ListOfNums))

#Завдання 4

def NumOfRems(ListOfNums, num):
 count = 0
 for i in ListOfNums:
     if i == num:
          ListOfNums.remove(i)
          count += 1
 return count

#Перевірка:

# ListOfNums=[random.randint(1,10) for i in range(10)]
# print("\nList of integers:", ListOfNums)
num = int(input("\nEnter the number to remove from the list1: "))
print("The number of deleted items in list1:", NumOfRems(ListOfNums, num))

#Завдання 5

def CombList(ListOfNums, ListOfNums2):
    return ListOfNums + ListOfNums2

#Перевірка:

# ListOfNums = [random.randint(1,10) for i in range(5)]
# ListOfNums2 = [random.randint(1,20) for i in range(10)]
# print("\nList 1: ", ListOfNums)
# print("List 2: ", ListOfNums2)
print("\nCombined list (list1 & list2): ", CombList(ListOfNums, ListOfNums2))

#Завдання 6

def PowerList(ListOfNums, power):
 result=[]
 for i in ListOfNums:
   result.append(i**power)
 return result
  
#Перевірка:

# ListOfNums = [random.randint(1,10) for i in range(5)]
# print("\nList of integers:", ListOfNums)
power = int(input("\nEnter the power: "))
print("A powered list 1:", PowerList(ListOfNums, power))