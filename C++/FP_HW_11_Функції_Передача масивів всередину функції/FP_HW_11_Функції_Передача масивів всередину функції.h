#include <iostream>

using namespace std;

int P = 1, sum = 0, count = 0;

void findPower (int a, int b)
{
    for (int i = 0; i < b; i++)
    {
        P*=a;
    }
    cout << "The value of the number " << a << " to the " << b << " power is " << P << ".\n\n";
}

void findSum (int a, int b)
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

void isPerfect (int num)
{
    for (size_t i=1; i<num; i++) {
        if (num % i == 0) {
        count += i;
        }
    }
    if (count == num) {
        cout << "Your umber is perfect.\n" << endl;
    }
    else {
        cout << "Your umber is not perfect.\n" << endl;
    }
}

void isLucky (string num)
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
    findPower (5, 3);
    findSum (-5, -9);
    isPerfect (496);
    isLucky ("125521");
}