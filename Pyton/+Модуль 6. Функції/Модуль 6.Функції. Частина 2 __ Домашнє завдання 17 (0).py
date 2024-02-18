import random

#�������� 1

def FindSumOfList1(ListOfNums):
  Sum = 0
  for i in ListOfNums:
      Sum = Sum + i
  return Sum

#���

def FindSumOfList2(ListOfNums):
  return sum(ListOfNums)

#���

def FindSumOfList3(ListOfNums):
  return lambda ListOfNums: sum(ListOfNums)

#��������:

ListOfNums=[random.randint(1,100) for i in range(10)]
print(ListOfNums)
print(FindSumOfList1(ListOfNums))
print(FindSumOfList2(ListOfNums))
print(FindSumOfList3(ListOfNums))

#�������� 2

def FindMinOfList1(ListOfNums):
  Min = ListOfNums[0]
  for i in ListOfNums:
    if i < Min:
      Min = i
  return Min

#���

def FindMinOfList2(ListOfNums):
  return min(ListOfNums)

#���

def FindMinOfList3(ListOfNums):
  return lambda ListOfNums: min(ListOfNums)

#��������:

ListOfNums=[random.randint(1,100) for i in range(10)]
print(ListOfNums)
print(FindMinOfList1(ListOfNums))
print(FindMinOfList2(ListOfNums))
print(FindMinOfList3(ListOfNums))