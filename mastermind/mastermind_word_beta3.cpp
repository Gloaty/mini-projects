#include <iostream>
#ifdef _WIN32
#include <Windows.h>
#else
#include <unistd.h>
#endif

using namespace std;

int main() {
        
    //word picker
    string challenge_words [4] = { "BURIAL", "CREATION", "RESURGENCE", "AUTONOMY" };
    srand(time(NULL));
    int RanIndex = 0+ (rand() % 4);
    cout << "RanIndex Value: " << RanIndex << "\n";
    string chosen_word = challenge_words[RanIndex];
    cout << "\n" << "Chosen Word: " << chosen_word;
    cout << "\n" << "\n" << "--------------------------------------------------------------------------";
    
    //gameplay
    cout << "\n" << "\n" << "                           CREATED BY..";
    cout << "\n" << "                          GLOATY STUDIOS";
    sleep(2);
    cout << "\n" << "\n";
    cout << "                            MASTERMIND";
    cout << "\n" << "\n";
    cout << "The aim of this game is to guess the word that is randomly selected." << "\n";
    cout << "Should you get a letter right, the game will tell you that you got it" << "\n";
    cout << "right, but it will not tell you the position. Your job is to figure out" << "\n";
    cout << "the word with the information you are provided. If you think ";
    cout << "you " << "\n" << "have figured out the word, type '/WORD' to guess. Good Luck! " << "\n" << "\n";
    string begin = " ";
    cout << "                         Begin Game? (Y/N)";
    cin >> begin;
    if (begin == "Y") {
        cout << "\n";
        cout << "                   SYSTEM RANDOMLY PICKING WORD...";
        sleep(2);
        cout << "\n" << "                       WORD HAS BEEN PICKED";
        sleep(1);
        cout << "\n" << "                          BEGINNING GAME";
        string user_input = " ";
        string correct_letter_memory = " ";
        string incorrect_letter_memory = " ";
        string word_user_input = " ";
        for (int i = 1;i < 1000000000000000000; i++) {
            user_input = " ";
            cout << "\n";
            cout << "          Incorrect Letter: " << incorrect_letter_memory << " - ";
            cout << "          Correct Letter: " << correct_letter_memory << " - ";
            cout << "\n" << "\n" << "                               TURN " << i;
            cout << "\n" << "\n" << "                        WORD IS FULLY UPPERCASE! ";
            cout << "\n" << "\n";
            cout << "                           Guess Letter: ";
            cin >> user_input;
            if (user_input == "/WORD") {
                cout << "\n" << "\n" << "                     WORD GUESS MODE INITIALIZING";
                cout << "\n" << "                            Guess Word: ";
                cin >> word_user_input;
                if (word_user_input == chosen_word) {
                    cout << "                    Victory! You Won! The Word Was: " << chosen_word;
                    cout << "\n";
                    cout << "                             You Won in " << i << " Turn(s)! ";
                    break;
                }
            }
            else if (chosen_word.find(user_input) != string::npos ) {
                correct_letter_memory = user_input;
                cout << "                     Yes, " << user_input << " is in the word! ";
            }
            else if (chosen_word.find(user_input) == string::npos ) {
                incorrect_letter_memory = user_input;
                cout << "                     No, " << user_input << " is not in the word! ";
            }
        }
    return 0;
    }
}