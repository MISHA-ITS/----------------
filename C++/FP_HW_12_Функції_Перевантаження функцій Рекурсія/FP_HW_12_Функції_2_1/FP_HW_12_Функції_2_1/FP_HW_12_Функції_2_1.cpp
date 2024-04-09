#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;

void FillMatrix(int **arr, int size)
{
	for (int i = 0; i < size; i++)
	{
		for (int j = 0; j < size; j++)
		{
			arr[i][j] = rand() % 10;
		}
	}
}

void DFillMatrix(double **arr, int size)
{
	for (int i = 0; i < size; i++)
	{
		for (int j = 0; j < size; j++)
		{
			arr[i][j] = rand() % 10;
		}
	}
}

void FillMatrix(char **arr, int size)
{
	for (int i = 0; i < size; i++)
	{
		for (int j = 0; j < size; j++)
		{
			arr[i][j] = rand() % 10;
		}
	}
}

void ShowMatrix(int **arr, int size)
{
	for (int i = 0; i < size; i++)
	{
		for (int j = 0; j < size; j++)
		{
			cout << setw(3) << arr[i][j] << " ";
		}
		cout << endl;
	}
	cout << endl;
}

void ShowMatrix(double **arr, int size)
{
	for (int i = 0; i < size; i++)
	{
		for (int j = 0; j < size; j++)
		{
			cout << setw(3) << arr[i][j] << " ";
		}
		cout << endl;
	}
	cout << endl;
}

void ShowMatrix(char **arr, int size)
{
	for (int i = 0; i < size; i++)
	{
		for (int j = 0; j < size; j++)
		{
			cout << setw(3) << arr[i][j] << " ";
		}
		cout << endl;
	}
	cout << endl;
}

void MinMaxDiagonal(int **arr, int size, int& min, int& max) {
	min = arr[0][0]; 
	max = arr[0][0];
	for (int i = 1; i < size; ++i) {
		if (arr[i][i] < min) {
			min = arr[i][i];
		}
		if (arr[i][i] > max) {
			max = arr[i][i];
		}
	}
	cout << "Minimal element on the main diagonal: " << min << endl;
	cout << "Maximum element on the main diagonal: " << max << endl;
}

void MinMaxDiagonal(double **arr, int size, double& min, double& max) {
	min = arr[0][0];
	max = arr[0][0];
	for (int i = 1; i < size; ++i) {
		if (arr[i][i] < min) {
			min = arr[i][i];
		}
		if (arr[i][i] > max) {
			max = arr[i][i];
		}
	}
	cout << "Minimal element on the main diagonal: " << min << endl;
	cout << "Maximum element on the main diagonal: " << max << endl;
}

void MinMaxDiagonal(char **arr, int size, char& min, char& max) {
	min = arr[0][0];
	max = arr[0][0];
	for (int i = 1; i < size; ++i) {
		if (arr[i][i] < min) {
			min = arr[i][i];
		}
		if (arr[i][i] > max) {
			max = arr[i][i];
		}
	}
	cout << "Minimal element on the main diagonal: " << min << endl;
	cout << "Maximum element on the main diagonal: " << max << endl;
}

void SortRows(int **arr, int size) {
	for (int i = 0; i < size; ++i) {
		sort(arr[i], arr[i] + size);
	}
}

int main()
{
	srand(time(NULL));
	const int SIZE = 5;
	int** arr = new int* [SIZE];
	for (int i = 0; i < SIZE; ++i) {
		arr[i] = new int[SIZE];
	}
	FillMatrix(arr, SIZE);
	cout << "Square matrix:" << endl;
	ShowMatrix(arr, SIZE);
	int min, max;
	MinMaxDiagonal(arr, SIZE, min, max);
	cout << endl;
	SortRows(arr, SIZE);
	cout << "Sorted matrix by rows:" << endl;
	ShowMatrix(arr, SIZE);
}