import random

#Завдання 1

def FindSumOfList1(ListOfNums):
  Sum = 0
  for i in ListOfNums:
    Sum = Sum + i
  return Sum

#або

def FindSumOfList2(ListOfNums):
  return sum(ListOfNums)

#або

def FindSumOfList3(ListOfNums):
  return lambda ListOfNums: sum(ListOfNums)

#Перевірка:

ListOfNums=[random.randint(1,100) for i in range(10)]
print(ListOfNums)
print(FindSumOfList1(ListOfNums))
print(FindSumOfList2(ListOfNums))
print(FindSumOfList3(ListOfNums))

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

ListOfNums=[random.randint(1,100) for i in range(10)]
print(ListOfNums)
print(FindMinOfList1(ListOfNums))
print(FindMinOfList2(ListOfNums))
print(FindMinOfList3(ListOfNums))

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

ListOfNums=[random.randint(1,10) for i in range(10)]
print("List of integers:", ListOfNums)
print("The number of primes in this list:", NumOfPrimes(ListOfNums))

#Завдання 4

def NumOfRems(ListOfNums, num):
 count = 0
 for i in ListOfNums:
     if i == num:
          ListOfNums.remove(i)
          count += 1
 return count

#Перевірка:

ListOfNums=[random.randint(1,10) for i in range(10)]
print("List of integers:", ListOfNums)
num = int(input("Enter the number to remove from the list: "))
print("The number of deleted items in this list:", NumOfRems(ListOfNums, num))

#Завдання 5

def CombList(list1, list2):
    return list1 + list2

#Перевірка:

list1 = [random.randint(1,10) for i in range(5)]
list2 = [random.randint(1,10) for i in range(5)]
print("List 1: ", list1)
print("List 2: ", list2)
print("Combined list: ", CombList(list1, list2))

#Завдання 6

def PowerList(ListOfNums, power):
 result = []
 for i in ListOfNums:
   result.append(i**power)
 return result
  
#Перевірка:

ListOfNums = [random.randint(1,10) for i in range(5)]
print("List of integers:", ListOfNums)
power = int(input("Enter the power: "))
print("A new list containing the obtained results:", PowerList(ListOfNums, power))