#include <iostream>
#include <ctime>
using namespace std;

int main()
{
	//1  Питати користувача про пароль, продовжувати запитувати, доки він не введе правильний пароль.
	
	string password = "PA$$W0RD";
    string word;
    while (true) {
        cout << "Enter password: ";
        cin >> word;
        if (word == password) {
            cout << "W E L L C O M E" << endl;
            break;
        }
        else {
            cout << "Incorrect password! Try again." << endl;
        }
    }
	
	//2  Знайти суму парних чисел від 1 до 50 за допомогою циклу while.
	
	int num = 1, sum = 0;
    cout << "Even numbers from 1 to 50: ";
    while (num <= 50) {
        if (num % 2 == 0) {
        cout << num << " ";
        sum += num;
        }
        num++;
    }
    cout << "\nThe sum of even numbers from 1 to 50 is equal to " << sum << endl;
	
	//3  Визначити кількість цифр у введеному користувачем числі.
	
	int number, digits = 0;
    cout << "Enter your number: ";
    cin >> number;
    while (number != 0)
    {
        digits++;
        number /= 10;
    }
    cout << "Number of digits in your number " << digits << endl;
	
	//4  Вивести всі дільники введеного користувачем числа.
	
	int j = 1, usernum;
    cout << "Enter your number: ";
    cin >> usernum;
    cout << "Divisors of your number: ";
    while (j <= usernum) {
        if (usernum % j == 0) {
        cout << j << " ";
        }
        j++;
    }
    cout << endl;
	
	//5  Зчитувати числа від користувача, доки він не введе 0, і вивести їх суму.
	
	int numb, n = 0;
    while (true) {
        cout << "Enter your number: ";
        cin >> numb;
        if (numb != 0) {
            n += numb;
        }
        else {
            cout << "Sum of numbers = " << n << endl;
            break;
        }
    }
	
	//6  Визначити, чи є введене користувачем число паліндромом.
	
	int digit;
    cout << "Enter your digit:";
    cin >> digit;
    int old_digit = digit, new_digit = 0;
    while (digit > 0) {
        int tmp = digit % 10;
        new_digit = new_digit * 10 + tmp;
        digit /= 10;
    }
    if (new_digit == old_digit)
        cout << "Your digit is a palindrom." << endl;
    else
        cout << "Your digit not is a palindrom." << endl;
	
	//7  Обчислити середнє арифметичне чисел, введених користувачем, доки він не введе від'ємне число.
	
	int numbe, nm = 0, c = 0;
    while (true) {
        cout << "Enter your number: ";
        cin >> numbe;
        if (numbe >= 0) {
            nm += numbe;
            c++;
        }
        else {
            cout << "Arithmetic mean of your numbers = " << nm / c << endl;
            break;
        }
    }
	
	//8  Реалізувати гру "вгадай число" за допомогою циклу while.
	
	int user_number, tr = 0;
    srand(time(0));
    int i = rand() % 500;
    while (i != user_number) {
        cout << "Enter your number from 1 to 500: ";
        cin >> user_number;
        if (user_number < 0 || user_number > 500) {
            cout << "Invalid value!!!" << endl;
            continue;
        }
        tr ++;
        if (i < user_number && user_number != 0) {
            cout << "Less" << endl;
        }
        else if (i > user_number && user_number != 0) {
            cout << "More" << endl;
        }
        else if (user_number == 0) {
            cout << "Good buy!" << endl;
            return 1;
        }
        else {
            cout << "You guessed it in " << tr << " tries!" << endl;
        }
    }
	
	//9  Знайти суму факторіалів чисел від 1 до 10.
	
	int count = 1, fact = 1, sm = 0;
    while (count <= 10)
    {
        fact *= count;
        cout << "Factorial of number " << count << " is equal to " << fact<< endl;
        sm += fact;
        count++;
    }
    cout << "The sum of factorials of numbers from 1 to 10 is equal to " << sm << endl;
	
	//10 Вивести кожну цифру введеного користувачем числа у зворотньому порядку.
	
    string str_num;
    cout << "Enter your number: ";
    cin >> str_num;
    int k = str_num.length();
    cout << "Your reversed number: ";
    while (k >= 0) {
        cout << str_num[k];
        k--;
    }
}