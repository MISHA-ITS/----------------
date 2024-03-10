// #include <iostream>

using namespace std;

int main()
{
	/*Завдання 1. Користувач вводить з клавіатури час у секундах Необхідно написати програму, яка переведе введені користувачем секунди в години, хвилини, секунди і виводить їх на екран.*/
	
	int seconds, hours, minutes;
	cout << "Enter your time in seconds: ";
	cin >> seconds;
	hours = seconds / 3600;
	seconds %= 3600;
	minutes = seconds / 60;
	seconds %= 60;
	cout << "\t- hours: " << hours << "\n\t- minutes: " << minutes << "\n\t- seconds: " << seconds << endl;
	
	/*Завдання 2. Написати програму, яка перетворює введене з клавіатури дробове число на грошовий формат. Наприклад, число 12,5 має бути перетворено так: 12 грн 50 коп.*/
	
	double fract;
	int grn, kop;
	cout << "\nEnter a fractional number: ";
	cin >> fract;
	grn = int(fract);
	kop = int((fract - grn) * 100);
	cout << "Monetary format of your fractional number: " << grn << " grn " << kop << " kop." << endl;
	
	/*Завдання 3. Написати програму, яка обчислює, з якою швидкістю бігун пробіг дистанцію. Рекомендований вигляд екрану під час виконання програми наведено нижче:
    - Обчислення швидкості бігу;
    - Введіть довжину дистанції (метрів) = 1000;
    - Введіть час (мін. сек) = 3.25;
    - Дистанція: 1000 м;
    - Час: 3 хв 25 сек = 205 сек;
    - Ви бігли зі швидкістю 17.56 км/год.*/
    
    double fract_time, speed;
	int min, sec, int_time, distance;
	cout << "\nCalculation of running speed; " << endl;
	cout << "Enter the length of the distance (meters) = ";
	cin >> distance;
	cout << "Enter the time (min.sec) = ";
	cin >> fract_time;
	min = int(fract_time);
	sec = int((fract_time - min) * 100);
	int_time = min * 60 + sec;
	speed = (double) distance / int_time * 3.6;
	cout << "Distance = " << distance << " m." << endl;
	cout << "Time: " << min << " min " << sec << " sec = " << int_time << " sec." << endl;
	cout << "You run at a speed of " << speed << " km/h." << endl;
	
	/*Завдання 4. Написати програму, яка перетворює введену користувачем кількість днів на кількість повних тижнів і днів, що залишилися. Наприклад, користувач ввів 17 днів, програма має вивести на екран 2 тижні і 3 дні./год.*/
    
	int days, weeks, number;
	cout << "\nEnter the number of days: ";
	cin >> days;
	weeks = days / 7;
	days %= 7;
	cout << "\t- weeks: " << weeks << "\n\t- days: " << days;
}