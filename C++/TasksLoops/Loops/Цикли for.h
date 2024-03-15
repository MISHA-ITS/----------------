#include <iostream>

using namespace std;

int main() {
    /*1.Вивести на екран числа від 1 до 10*/
	
	for (size_t i=1; i<=10; i++) {
        cout << i << " ";
    }
	cout << endl;
	
	/*2.Просумувати числа від 1 до 100 і вивести результат.*/
    
    int sum = 0;
    for (size_t i=1; i<=100; i++) {
        sum += i;
    }
    cout << "Sum = " << sum << endl;
    
    /*3.Вивести парні числа від 2 до 20.*/
    
	for (size_t i=1; i<=20; i++) {
        if (i % 2 == 0) {
            cout << i << " ";
		}
    }
    cout << endl;
    
	/*4.Вивести таблицю множення для введеного користувачем числа*/
	
    int n;
    cout << "Enter your number: ";
    cin >> n;
    for (size_t i=1; i<=10; i++) {
        cout << "\t" << n << " * " << i << " = " << n * i << endl;
    }
	
	//5.Знайти суму квадратів чисел від 1 до 5.
    
    int summ = 0;
    for (size_t i=1; i<=5; i++) {
        summ += i*i;
    }
    cout << "The sum of the squares of the numbers from 1 to 5 = " << summ << endl;
	    
    //6.Вивести факторіал введеного користувачем числа.
    
    int num, fact=1;
    cout << "Enter your number: ";
    cin >> num;
    for (size_t i=1; i<=num; i++) {
        fact *= i;
    }
    cout << "Factorial of number " << num << " is equal to " << fact << endl;
	
	//7.Знайти суму всіх простих чисел від 1 до 50.
	
	int s = 0;
    cout << "All prime numbers from 1 to 50: ";
    for (size_t i = 1; i <= 50; i++) {
        int count = 0;
        for (size_t j = 2; j <= i / 2; j++) {
            if (i % j == 0) {
                count++;
                break;
            }
        }
        if (count == 0 && i != 1) {
            cout << i << ", ";
            s += i;
        }
    }
    cout << "their sum is equal to " << s  << endl;
	
	//8.Вивести числа Фібоначчі до n, де n - введене користувачем число.
	
	int numb, prev = 0, curr = 1, next;
    cout << "Enter your number: ";
    cin >> numb;
    if (numb < 0) {
        cout << "Enter a non-negative number." << endl;
        return 1;
    }
    cout << "Fibonacci numbers to " << numb << ": ";
    cout << prev << " " << curr << " ";
    for (size_t i = 2; i <= numb; i++) {
        next = prev + curr;
        if (next > numb) {
            break;
        }
        cout << next << " ";
        prev = curr;
        curr = next;
    }
    cout << endl;
	
	//9.Визначити, чи є введене число простим.
	
	int number, count=0;
    cout << "Enter number more than zero: ";
    cin >> number;
    if (number <= 0) {
        cout << "Number must be more than zero!!!" << endl;
        return 1;
    }
    for (size_t i=2; i<number; i++) {
        if (number % i == 0) {
            ++ count;
        }
    }
    if (count == 0 && number != 1) {
        cout << "Your number is prime." << endl;
    }
    else {
        cout << "Your number is not prime." << endl;
    }
	
	//10.Вивести числа від 10 до 1 у зворотному порядку.
	
	{
		for (size_t i = 10; i >= 1; i--)
		cout << i << " ";
	}
	cout << endl;
	
	//11.Визначити суму перших 10 чисел Фібоначчі.
    
	int fib_sum = 0, prv = 0, crr = 1, nxt;
	cout << "The sum of the first 10 Fibonacci numbers: ";
    for (size_t i = 0; i < 10; i++) {
        cout << crr << " ";
        fib_sum += crr;
        nxt = prv + crr;
        prv = crr;
        crr = nxt;
    }
    cout << "is equal to " << fib_sum << endl;
	
	//12.Вивести кожну літеру слова за допомогою циклу for.
    
    string word;
    cout << "Enter the word: ";
    cin >> word;
    for (size_t i = 0; i < word.length(); ++i) {
        cout << "\"" << word[i] << "\", ";
    }
    cout << endl;
	
	//13.Знайти суму всіх чисел від 1 до 50, які діляться або на 3, або на 5or.
    
    int sm = 0;
    cout << "All numbers from 1 to 50 that are divisible by 3 or 5: ";
    for (size_t i = 1; i <= 50; ++i) {
        if (i % 3 == 0 || i % 5 == 0) {
            cout << i << ", ";
            sm += i;
        }
    }
    cout << "their sum is equal to " << sm << endl;
	
	//14.Вивести на екран кожну парну букву слова "HELLO".
    
    string Word = "HELLO";
    for (size_t i = 0; i < Word.length(); i += 2) {
        cout << "\"" << Word[i] << "\", ";
    }
    cout << endl;
	
	//15.Знайти суму квадратів парних чисел від 2 до 20.
    
    int sum_sqr = 0;
    for (size_t i=1; i<=20; i++) {
        if (i % 2 == 0) {
            sum_sqr += i*i;
		}
    }
    cout << "The sum of the squares of even numbers from 2 to 20 is equal to " << sum_sqr << endl;
	
	//16.Визначити, чи є введене користувачем число досконалим (рівне сумі своїх дільників, крім самого себе).
	
	int per_num, Count;
    Count=0;
    cout << "Enter your number: ";
    cin >> per_num;
    for (size_t i=1; i<per_num; i++) {
        if (per_num % i == 0) {
            Count += i;
        }
    }
    if (Count == per_num) {
        cout << "Your umber is perfect." << endl;
    }
    else {
        cout << "Your umber is not perfect." << endl;
    }
	
	//17.Вивести всі прості числа від 10 до 50.
	
	cout << "All prime numbers from 1 to 50: ";
    for (size_t i = 1; i <= 50; i++) {
        int count = 0;
        for (size_t j = 2; j <= i / 2; j++) {
            if (i % j == 0) {
                count++;
                break;
            }
        }
        if (count == 0 && i != 1) {
            cout << i << " ";
        }
    }
	cout << endl;
	
	//18.Вивести на екран зірочки у вигляді прямокутника (5x5).
	
    for (size_t i=0; i<5; i++) {
        for (size_t j=0; j<5; j++) {
            cout << " * ";
        }
        cout << endl;
    }
	
	//19.Реалізувати виведення чисел у пірамідальній формі (піраміда зі зірочок).
	
    for (size_t i = 0; i < 21; i++) {
        for (size_t j = 0; j < 21; j++) {
            if (i + j >= 20 && i >= j)
            cout << " * ";
            else
            cout << "   ";
        }
    cout << endl;
    }
	
	//20.Зчитати та вивести перші 5 рядків з файлу за допомогою циклу for.
}