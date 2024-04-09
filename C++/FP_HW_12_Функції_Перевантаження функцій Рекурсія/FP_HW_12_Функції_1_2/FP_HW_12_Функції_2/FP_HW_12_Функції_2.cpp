#include <iostream>
using namespace std;

void fillarr(int arr[], int size)
{
	for (size_t i = 0; i < size; i++)
	{
		arr[i] = rand() % 10;
	}
}

void show(int arr[], int size) {
	for (size_t i = 0; i < size; i++)
	{
		cout << arr[i] << " ";
	}
}

double avg(int arr[], int size) {
	double a = arr[0];
	for (int i = 1; i < size; i++)
	{
		a += arr[i];
	}
	a = a / size;
	return a;
}

int main()
{
	srand(time(NULL));
	const int SIZE = 10;
	int arr[SIZE];
	fillarr(arr, SIZE);
	show(arr, SIZE);
	cout << endl;
	cout << "Arithmetic average of array elements: " << avg(arr, SIZE) << ".";
}

