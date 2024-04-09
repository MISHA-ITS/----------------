#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>
using namespace std;

int generateRandomNumber() {
    srand(time(0));
    int num = rand() % 9000 + 1000;
    return num;
}

bool isValidGuess(int guess) {
    if (guess >= 1000 && guess <= 9999) {
        return true;
    }
    else {
        return false;
    }
}

void countBullsAndCows(string secretNum, string guess, int& bulls, int& cows, int index) {
    if (index >= 4) {
        return;
    }

    if (secretNum[index] == guess[index]) {
        bulls++;
    }
    else {
        for (int i = 0; i < 4; ++i) {
            if (secretNum[i] == guess[index]) {
                cows++;
                break;
            }
        }
    }

    countBullsAndCows(secretNum, guess, bulls, cows, index + 1);
}

int main() {
    int secretNumber = generateRandomNumber();
    string secretNumString = to_string(secretNumber);

    int attempts = 0;

    cout << "Bulls and cows game. Try to guess a four-digit number.\n";

    while (true) {
        int guess;
        cout << "Enter your number: ";
        cin >> guess;

        if (!isValidGuess(guess)) {
            cout << "Please enter a four - digit number.\n";
            continue;
        }

        string guessString = to_string(guess);

        int bulls = 0, cows = 0;
        countBullsAndCows(secretNumString, guessString, bulls, cows, 0);

        cout << "Bulls: " << bulls << ", Cows: " << cows << endl;

        attempts++;

        if (bulls == 4) {
            cout << "Congratulations! You guessed the number in " << attempts << " tries.\n";
            break;
        }
    }
}