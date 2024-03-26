//Завдання 1. Написати програму, яка виводить на екран лінію заданим символом, вертикальну або горизонтальну, причому лінія може виводитися швидко, нормально і повільно. Спілкування з користувачем організувати через меню.

#include <iostream>
#include <ctime>

using namespace std;

int main() {

    char symbol;
    int length, speed, choice;

    do {
        cout << "Menu:" << endl;
        cout << "1. Print horizontal line" << endl;
        cout << "2. Print vertical line" << endl;
        cout << "3. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Enter symbol: ";
                cin >> symbol;
                cout << "Enter length: ";
                cin >> length;
                cout << "Select speed (1 - fast, 2 - normal, 3 - slow): ";
                cin >> speed;
                for (int i = 0; i < length; ++i) {
                    cout << symbol;
                    if (speed == 1) {
                        clock_t delay = 100 * CLOCKS_PER_SEC / 1000; // 100 milliseconds
                        clock_t start_time = clock();
                        while (clock() < start_time + delay);
                    } else if (speed == 2) {
                        clock_t delay = 500 * CLOCKS_PER_SEC / 1000; // 500 milliseconds
                        clock_t start_time = clock();
                        while (clock() < start_time + delay);
                    } else if (speed == 3) {
                        clock_t delay = CLOCKS_PER_SEC; // 1 second
                        clock_t start_time = clock();
                        while (clock() < start_time + delay);
                    }
                }
                cout << endl;
                break;
            case 2:
                cout << "Enter symbol: ";
                cin >> symbol;
                cout << "Enter length: ";
                cin >> length;
                cout << "Select speed (1 - fast, 2 - normal, 3 - slow): ";
                cin >> speed;
                for (int i = 0; i < length; ++i) {
                    cout << symbol << endl;
                    if (speed == 1) {
                        clock_t delay = 100 * CLOCKS_PER_SEC / 1000; // 100 milliseconds
                        clock_t start_time = clock();
                        while (clock() < start_time + delay);
                    } else if (speed == 2) {
                        clock_t delay = 500 * CLOCKS_PER_SEC / 1000; // 500 milliseconds
                        clock_t start_time = clock();
                        while (clock() < start_time + delay);
                    } else if (speed == 3) {
                        clock_t delay = CLOCKS_PER_SEC; // 1 second
                        clock_t start_time = clock();
                        while (clock() < start_time + delay);
                    }
                }
                break;
            case 3:
                cout << "Exiting...";
                break;
            default:
                cout << "Invalid choice! Please try again." << endl;
        }
    } while (choice != 3);
}