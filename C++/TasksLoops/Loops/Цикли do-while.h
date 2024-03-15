#include <iostream>

using namespace std;

int main()
{
	//1 Питати користувача про введення числа, доки він не введе парне число
	
	int number;
    do
    {
        cout << "Enter your number: ";
        cin >> number;
    }while (number % 2 != 0);
    cout << "Good buy!";
	
	//2 Знайти суму непарних чисел від 1 до 25 за допомогою циклу do-while.
	
	int num = 1, sum = 0;
    cout << "\nOdd numbers from 1 to 25: ";
    do {
        if (num % 2 != 0) {
            sum += num;
            cout << num << " ";
        }
        num++;
    }while (num <= 25);
    cout << "\nThe sum of odd numbers from 1 to 25 is equal " << sum;
	
	//або простіше
	
	num = 1, sum = 0;
    do {
        sum += num;
        num += 2;
    }while (num <= 25);
    cout << "\nThe sum of odd numbers from 1 to 25 is equal " << sum << endl;
	
	//3 Вивести таблицю множення для введеного користувачем числа за допомогою циклу do-while.
	
	int n, k = 1;
    cout << "Enter your number: ";
    cin >> n;
    do {
        cout << n << " * " << k << " = " << k * n << endl;
        k++;
    }while (k <= 10);
	
	//4 Питати користувача про введення пароля, доки він не введе правильний пароль.
	
	string pass = "PA$$W0RD", uspass;
    do {
        cout << "Enter password: ";
        cin>> uspass;
    }while (uspass != pass);
    cout << "W E L L C O M E" << endl;
	
	//5 Вивести числа Фібоначчі до n за допомогою циклу do-while, де n - введене користувачем число.
	
	int numb, prev = 0, curr = 1, next;
    cout << "Enter your number: ";
    cin >> numb;
    if (numb < 0) {
        cout << "Enter a non-negative number." << endl;
        return 1;
    }
    cout << "Fibonacci numbers to " << numb << ": ";
    cout << prev << " " << curr << " ";
    do {
        next = prev + curr;
        if (next > numb) {
            break;
        }
        cout << next << " ";
        prev = curr;
        curr = next;
    } while (true);
    cout << endl;
}