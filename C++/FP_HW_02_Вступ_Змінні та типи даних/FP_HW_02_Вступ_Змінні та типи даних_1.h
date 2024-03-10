#include <iostream>

using namespace std;

int main()
{
    /*Завдання 1. Задані три опори R1, R2, R3. Обчислити значення опору R0 за формулою: 1/R0 = 1/R1+1/R2+1/R3.*/
	
	float R0, R1, R2, R3;
	cout << "Enter the value of the resistances: " << endl;
    cout << " - first value: ";
    cin >> R1;
    cout << " - second value: ";
    cin >> R2;
    cout << " - third value: ";
    cin >> R3;
    R0 = 1 / (1 / R1 + 1 / R2 + 1 / R3);
    cout << "Сalculate value of resistance: R0 = 1 / (1 / " << R1 << " + 1 / " << R2 << " + 1 / " << R3 << ") = " << R0 << endl;
	
	/*Завдання 2. За заданою довжиною окружності знайти площу кола за формулою S = pi*R2, радіус обчислити з формули довжини кола: L = 2*pi*R.*/
	
	float L, S, R;
    float const PI = 3.14;
    cout << "\nEnter the length of the circumference L: ";
    cin >> L;
    R = L / (2 * PI);
    cout << "Calculate the radius of the circle from the formula: R = L / (2 * PI) = " << L << " / (2 * " << PI << ") = " << R << endl;
    S = PI * R * R;
    cout << "Find the area of a circle using the formula: S = PI * R ^ 2 = " << PI << " * " << R << " ^ 2 = " << S << endl;
	
	/*Завдання 3. Обчислити пройдену відстань при прямолінійному рівноприскореному русі за формулою S=v*t+(a*t2)/2, де v—швидкість, t—час, а—прискорення.*/
	
	float s, v, t, a;
    cout << "\nEnter speed: ";
    cin >> v;
    cout << "Enter time: ";
    cin >> t;
    cout << "Enter acceleration: ";
    cin >> a;
    s = v * t + (a * t * t) / 2;
    cout << "Find the distance: S = " << v << " * " << t << " + ( " << a << " * " << t << " ^ 2 ) / 2 = " << s;
}