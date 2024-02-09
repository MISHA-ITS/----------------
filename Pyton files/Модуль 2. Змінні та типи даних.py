# https://github.com ще не опанував (((


# Завдання 1

number1=int(input("Enter your frrst number: "))
number2=int(input("Enter your second number: "))
number3=int(input("Enter your third number: "))
sum=number1+number2+number3
mul=number1*number2*number3
print(f"Sum of numbers: {sum}.")
print(f"Multiplication of numbers: {mul}.")

# Завдання 2

userName=input("Enter your name: ")
print(f"Hello {userName}", end=",")
profit=float(input(" enter your monthly salary ($ per month): "))
payment=float(input("enter your monthly payment for the bank loan ($ per month): "))
arrears=float(input("enter your arrears for communal services ($ per month): "))
expenses=(payment+arrears)
balance=profit-expenses
print(f"{userName}, your monthly expenses are {expenses}$, and your total balance after these payments is {balance}$.")

# Завдання 3

d1=float(input("Please, enter the first diagonal: "))
d2=float(input("Enter the second diagonal: "))
area=(d1*d2)/2
print(f"The area of your rhombus is equal: ({d1} * {d2}) / 2 = {area}.")