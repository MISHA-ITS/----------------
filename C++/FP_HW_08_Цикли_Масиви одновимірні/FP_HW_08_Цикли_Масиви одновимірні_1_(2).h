//Завдання 2. Написати гру «Кубики». Користувач і комп'ютер по черзі кидають 2 кубики. Переможець той, у кого за результатами 3х кидків сума більше. Передбачитикрасивий інтерфейс гри.

#include <iostream>
#include <ctime>

using namespace std;

int rollDice() {
    return rand() % 6 + 1;
}

int main() {
    srand(time(0));

    int userScore = 0;
    int computerScore = 0;

    cout << "\t\tC U B E S" << endl;

    for (int i = 0; i < 3; ++i) {
        int userRoll1 = rollDice();
        int userRoll2 = rollDice();
        int computerRoll1 = rollDice();
        int computerRoll2 = rollDice();
        
        cout << "\nYour throw: " << userRoll1 << " and " << userRoll2 << endl;
        cout << "Throwing the computer: " << computerRoll1 << " and " << computerRoll2 << endl;
        
        int userTotal = userRoll1 + userRoll2;
        int computerTotal = computerRoll1 + computerRoll2;

        userScore += userTotal;
        computerScore += computerTotal;

        cout << "Current account: you - " << userScore << ", computer - " << computerScore << endl;
    }

    if (userScore > computerScore) {
        cout << "\n\t\tYOU WON!" << endl;
    } else if (userScore < computerScore) {
        cout << "\n\t\tCOMPUTER WON!"<< endl;
    } else {
        cout << "\n\t\tD R A W !" << endl;
    }
}