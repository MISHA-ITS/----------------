#include <iostream>
using namespace std;

bool isLeapYear(int year) {
    return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
}

int daysInMonth(int year, int month) {
    switch (month) {
    case 1: case 3: case 5: case 7: case 8: case 10: case 12:
        return 31;
    case 4: case 6: case 9: case 11:
        return 30;
    case 2:
        return isLeapYear(year) ? 29 : 28;
    default:
        return -1;
    }
}

int daysBetweenDates(int year1, int month1, int day1, int year2, int month2, int day2) {
    int days = 0;
    if (year1 > year2 || (year1 == year2 && month1 > month2) || (year1 == year2 && month1 == month2 && day1 > day2)) {
        swap(year1, year2);
        swap(month1, month2);
        swap(day1, day2);
    }
    while (year1 < year2 || month1 < month2 || day1 < day2) {
        days++;
        day1++;
        if (day1 > daysInMonth(year1, month1)) {
            day1 = 1;
            month1++;
            if (month1 > 12) {
                month1 = 1;
                year1++;
            }
        }
    }
    return days;
}

int main() {
    int year1, month1, day1;
    int year2, month2, day2;

    cout << "Enter the first date (year, month, day): ";
    cin >> year1 >> month1 >> day1;

    cout << "Enter the sуcond date (year, month, day): ";
    cin >> year2 >> month2 >> day2;

    int difference = daysBetweenDates(year1, month1, day1, year2, month2, day2);
    cout << "Difference in days between dates: " << difference << endl;
}
