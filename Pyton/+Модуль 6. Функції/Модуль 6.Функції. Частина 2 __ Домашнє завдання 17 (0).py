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