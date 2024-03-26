#include <iostream>
#include <ctime>

using namespace std;

int main()
{
	//Завдання 1. В одновимірному масиві, заповненому випадковими числами, визначити мінімальний і максимальний елементи.
	
    srand(time(NULL));
    const int SIZE = 12;
    int arr[SIZE], min = 0, max = 0;
    cout << "Array: ";
    for (size_t i = 0; i < SIZE; i++) {
        arr[i] = rand() % 200 - 100;
        cout << arr[i] << ", ";
    }
    for (size_t i = 0; i < SIZE; i++)
    {
        if (arr[i] > max) {
            max = arr[i];
        }
        else if (arr[i] < min) {
            min = arr[i];
        }
    }
    cout << "\nmin value = " << min << ", ";
    cout << "max value = " << max << endl;
    cout << endl;
	
	//Завдання 2. Користувач вводить прибуток фірми за рік (12 місяців). Потім користувач вводить діапазон (наприклад, 3 і 6 — пошук між третім і шостим місяцем). Необхідно визначити місяць, у якому прибуток був максимальним, і місяць, у якому прибуток був мінімальним, з урахуванням обраного діапазону.
	
    int array[SIZE] = {};
    cout << "Enter profit of the firm for each month: " << endl;
    for (size_t i = 0; i < SIZE; ++i) {
        cout << "\t- for the " << i + 1 << " month: ";
        cin >> array[i];
    }
    cout << endl;

    int first, last;
    cout << "Enter the first month of the period: ";
    cin >> first;
    cout << "Enter the last month of the period: ";
    cin >> last;
    cout << endl;
    
    int mx = array[first - 1], mn = array[first - 1];
    int mxm = first, mnm = first;
    for (size_t i = first; i <= last; ++i) {
        if (array[i - 1] > mx) {
            mx = array[i - 1];
            mxm = i;
        }
        else if (array[i - 1] < mn) {
            mn = array[i - 1];
            mnm = i;
        }
    }
    cout << "Max profit was in " << mxm << " month - " << mx << endl;
    cout << "Min profit was in " << mnm << " month - " << mn << endl;
	
	//Завдання 3. В одновимірному масиві, що складається з N дійсних чисел, обчислити:
	
	//Суму від'ємних елементів;
	
	srand(time(NULL));
    int N;
    cout << "\nEnter the number of random real numbers to make up the array: ";
    cin >> N;
    int ar[N];
    cout << "\n\tArray: ";
    for (size_t i = 0; i < N; i++) {
        ar[i] = rand() % 20 - 10;
        cout << ar[i] << ", ";
    }
    
    int sum_ne = 0;
    for (size_t i = 0; i < N; i++){
    if (ar[i] < 0) {
        sum_ne += ar[i];
        }
    }
    cout << "\n - sum of negative elements: " << sum_ne << endl;
    
	//Добуток елементів, що розташовані між min і max елементами;
	
    int min_e = 0, max_e = 0, i_min_e, i_max_e;
    for (size_t i = 0; i < N; i++) {
        if (ar[i] > max_e) {
            max_e = ar[i];
            i_max_e = i;
        }
        else if (ar[i] < min_e) {
            min_e = arr[i];
            i_min_e = i;
        }
    }
	
    int prod_e = 1;
    if (i_max_e > i_min_e && i_max_e - i_min_e != 1) {
        for (size_t i = i_min_e +1; i < i_max_e; i++) {
            prod_e *= ar[i];
        }
    }
    else if (i_max_e < i_min_e && i_min_e - i_max_e != 1) {
        for (size_t i = i_max_e +1; i < i_min_e; i++) {
            prod_e *= ar[i];
        }
    }
    else {
        prod_e = 0;
    }
    cout << " - product of elements located between min and max elements: " << prod_e << endl;
    
	//Добуток елементів з парними номерами;
	
    int prod_even = ar[1];
    for (size_t i = 2; i < N; i++){
        if (i % 2 != 0) {
            prod_even *= ar[i];
        }
    }
    cout << " - product of elements with even numbers: " << prod_even << endl;
	
	//Суму елементів, що розташовані між першим і останнім від'ємними елементами.
    
    int sum_bne = 0, fne = 0, lne = 0;
	for (size_t i = 0; i < N; i++){
    if (ar[i] < 0) {
        fne = i;
        break;
        }
    }

    for (size_t i = 0; i < N; i++){
    if (arr[i] < 0) {
        lne = i;
        }
    }
    
    for (size_t i = fne + 1; i < lne; i++){
        sum_bne += arr[i];
    }
    cout << " - sum of elements located between the first and last negative elements: " << sum_bne << ".";
}