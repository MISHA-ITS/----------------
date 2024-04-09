#include <iostream>
using namespace std;

void FillArr(int arr[], int size)
{
	for (int i = 0; i < size; i++)
	{
		arr[i] = rand() % 100 - 50;
	}
}

void Show(int arr[], int size)
{
	cout << "Array of numbers: ";
	for (int i = 0; i < size; i++)
	{
		cout << arr[i] << " ";
	}
	cout << endl;
}

void FindNumbers(int arr[], int size)
{
	int pos = 0, neg = 0, zero = 0;
	for (int i = 0; i < size; i++)
	{
		if (arr[i] > 0) {
			pos++;
		}
		else if (arr[i] < 0) {
			neg++;
		}
		else {
			zero++;
		}
	}
	cout << "  - number of positive elements: " << pos << ";" << endl;
	cout << "  - number of negative elements: " << neg << ";" << endl;
	cout << "  - number of zero elements: " << zero << "." << endl;
}

int main()
{
    srand(time(NULL));
	const int SIZE = 20;
	int arr[SIZE];
	FillArr(arr, SIZE);
	Show(arr, SIZE);
	FindNumbers(arr, SIZE);
}