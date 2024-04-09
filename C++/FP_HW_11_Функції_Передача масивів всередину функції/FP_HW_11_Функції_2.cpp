#include <iostream>

using namespace std;

void fillarr(int arr[], int size)
{
	for (int i = 0; i < size; i++)
	{
		arr[i] = rand() % 100;
	}
}

void Show(int arr[], int size)
{
	for (int i = 0; i < size; i++)
	{
		cout << arr[i] << ", ";
	}
}

int LinearSearch(int arr[], int size, int key1)
{
	for (int i = 0; i < size; i++)
	{
		if (key1 == arr[i]) {
			return i;
		}
	}return 0;
}

int BinarySearch(int arr[], int size, int key2)
{
	int B = 0, E = size - 1;
	while (true)
	{
		int p = (B + E) / 2;
		if (key2 > arr[p])
		{
			B = p + 1;
		}
		else if (key2 < arr[p])
		{
			E = p - 1;
		}
		else if (key2 = arr[p])
		{
			return p;
		}
		else if (B + E)
		{
			return 0;
		}
		return 0;
	}
}

int binaryToDecimal(int binaryNumber) {
	int decimalNumber = 0;
	int base = 1;
	while (binaryNumber > 0) {
		int lastDigit = binaryNumber % 10;
		binaryNumber /= 10;
		decimalNumber += lastDigit * base;
		base *= 2;
	}
	return decimalNumber;
}

int main()
{
	srand(time(NULL));
	const int SIZE = 100;
	int arr[SIZE];
	fillarr(arr, SIZE);
	cout << "Array: ";
	Show(arr, SIZE);
	cout << endl;
	if (LinearSearch(arr, SIZE, 20))
	{
		cout << "\nLinear search: your element is on position " << LinearSearch(arr, SIZE, 20) + 1 << "." << endl;
	}
	else
	{
		cout << "Linear search: your alement not in array!" << endl;
	}
	cout << endl;
	if (BinarySearch(arr, SIZE, 40))
	{
		cout << "Binary search: your element is on position " << BinarySearch(arr, SIZE, 40) + 1 << endl;
	}
	else
	{
		cout << "Binary search: your alement not in array!" << endl;
	}
	cout << endl;
	int binaryNumber;
	cout << "Enter a number in binary: ";
	cin >> binaryNumber;
	int decimalNumber = binaryToDecimal(binaryNumber);
	cout << endl;
	cout << "A binary number " << binaryNumber << " in the decimal system : " << decimalNumber << endl;
}

