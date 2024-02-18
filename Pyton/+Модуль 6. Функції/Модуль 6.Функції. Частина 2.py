import random

ListOfNums=[random.randint(1,20) for i in range(5)]
ListOfNums2=[random.randint(21,40) for i in range(5)]
print("List of integers 1:", ListOfNums)
print("List of integers 2:", ListOfNums2)



#Завдання 1

def FindProdOfList(ListOfNums):
  prod=1
  for i in ListOfNums:
    prod=prod*i
  return prod

#Перевірка:

print("\nThe product of the elements of list1:", FindProdOfList(ListOfNums))



#Завдання 2

def FindMinOfList1(ListOfNums):
  min=ListOfNums[0]
  for i in ListOfNums:
    if i<min:
      min=i
  return min

#Перевірка:

print("\nMin of list1:", FindMinOfList1(ListOfNums))



#Завдання 3

def NumOfPrimes(ListOfNums):
  count=0
  for i in ListOfNums:
    if i<2:
      continue
    for j in range(2, i):
      if i%j==0:
        break
    else:
      count+=1
  return count

#Перевірка:

print("\nThe number of primes in list 1:", NumOfPrimes(ListOfNums))



#Завдання 4

def NumOfRems(ListOfNums, num):
  count=0
  for i in ListOfNums:
    if i==num:
      ListOfNums.remove(i)
      count+=1
  return count

#Перевірка:

num = int(input("\nEnter the number to remove from the list1: "))
print("The number of deleted items in list1:", NumOfRems(ListOfNums, num))



#Завдання 5

def CombList(ListOfNums, ListOfNums2):
  return ListOfNums+ListOfNums2

#або
  
def ExtendList(ListOfNums, ListOfNums2):
  ListOfNums.extend(ListOfNums2)
  return ListOfNums

#Перевірка:

print("\nCombined list (list1 & list2):",CombList(ListOfNums, ListOfNums2))
print("Extending list1 (by list2):",ExtendList(ListOfNums, ListOfNums2))



#Завдання 6

def PowerList(ListOfNums, power):
  result=[]
  for i in ListOfNums:
    result.append(i**power)
  return result

#Перевірка:

power=int(input("\nEnter the power: "))
print("A powered list:", PowerList(ListOfNums, power))