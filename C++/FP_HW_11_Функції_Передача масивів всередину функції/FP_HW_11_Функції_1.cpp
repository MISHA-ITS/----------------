#include <iostream>
#include <locale>
#include <io.h>
#include <fcntl.h>
#define SPADE L"\u2660"
#define CLUB L"\u2663"
#define HEART L"\u2665"
#define DIAMOND L"\u2666"
using namespace std;

int P = 1, sum = 0, count = 0;

void findPower(int a, int b)
{
    for (int i = 0; i < b; i++)
    {
        P *= a;
    }
    cout << "The value of the number " << a << " to the " << b << " power is " << P << ".\n\n";
}

void findSum(int a, int b)
{
    if (a <= b) {
        for (int i = a + 1; i < b; i++) {
            sum += i;
        }
    }
    else {
        for (int i = b + 1; i < a; i++) {
            sum += i;
        }
    }
    cout << "The sum of numbers from the range between " << a << " and " << b << " is " << sum << ".\n\n";
}

void isPerfect(int num)
{
    int k = 0;
    for (int i = 1; i < num; i++) {
        if (num % i == 0) {
            k += i;
        }
    }
    if (k == num) {
        cout << "Your umber is perfect.\n" << endl;
    }
    else {
        cout << "Your umber is not perfect.\n" << endl;
    }
}

void printCard(wchar_t* suit, char value)
{
    (void)_setmode(_fileno(stdout), _O_U16TEXT);
    wcout << " ______________________ " << endl;
    wcout << "| " << value << suit << "                   |" << endl;
    for (int i = 0; i < 16; i++)
    {
        wcout << "|";
        for (int j = 1; j < 23; j++)
        {
            wcout << " ";
        }
        wcout << "|" << endl;
    }
    wcout << "|                    " << value << suit << "| " << endl;
    wcout << " ---------------------- " << endl;
    _setmode(_fileno(stdout), _O_TEXT);
}

void isLucky(string num)
{
    if (num.length() != 6) {
        cout << "Error! The number must be six digits." << endl;
    }
    else {
        if ((num[0] - '0') + (num[1] - '0') + (num[2] - '0') == (num[3] - '0') + (num[4] - '0') + (num[5] - '0')) {
            cout << "Number is lucky." << endl;
        }
        else {
            cout << "Number is not lucky." << endl;
        }
    }
}
int main()
{
    findPower(5, 3);
    findSum(-5, -9);
    isPerfect(496);
    setlocale(LC_ALL, "");
    printCard((wchar_t*)DIAMOND, 'Q');
    isLucky("125521");
}