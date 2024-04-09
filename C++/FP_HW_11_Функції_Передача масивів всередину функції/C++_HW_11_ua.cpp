#include <iostream>

using namespace std;

template<typename T>
T findMax(T arr[], int size) {
    T max = arr[0];
    for (int i = 1; i < size; ++i) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}

template<typename T>
T findMin(T arr[], int size) {
    T min = arr[0];
    for (int i = 1; i < size; ++i) {
        if (arr[i] < min) {
            min = arr[i];
        }
    }
    return min;
}

template<typename T>
void bubbleSort(T arr[], int size) {
    for (int i = 0; i < size - 1; ++i) {
        for (int j = 0; j < size - i - 1; ++j) {
            if (arr[j] > arr[j + 1]) {
                T temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

int main() {
    int intArr[] = { 3, 1, 4, 1, 5, 9, 2, 6 };
    double doubleArr[] = { 3.14, 2.71, 1.618, 0.577, 2.718 };

    cout << "The maximum of the entire array: " << findMax(intArr, 8) << endl;
    cout << "The minimum of the entire array: " << findMin(intArr, 8) << endl;
    cout << "The maximum of a floating-point array: " << findMax(doubleArr, 5) << endl;
    cout << "The minimum of a floating-point array: " << findMin(doubleArr, 5) << endl;

    bubbleSort(intArr, 8);
    bubbleSort(doubleArr, 5);

    cout << "Sorted array of integers : ";
    for (int i = 0; i < 8; ++i) {
        cout << intArr[i] << " ";
    }
    cout << endl;

    cout << "Sorted array of floating point numbers: ";
    for (int i = 0; i < 5; ++i) {
        cout << doubleArr[i] << " ";
    }
    cout << endl;
}