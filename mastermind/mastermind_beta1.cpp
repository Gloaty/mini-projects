#include <iostream>
#ifdef _WIN32
#include <Windows.h>
#else
#include <unistd.h>
#endif

using namespace std;

int main()
{
    //word picker
    string challenge_words [4] = { "Burial", "Creation", "Resurgence", "Autonomy" };
    srand(time(NULL));
    int RanIndex = 0+ (rand() % 4);
    cout << "RanIndex Value: " << RanIndex << "\n";
    string chosen_word = challenge_words[RanIndex];
    cout << "\n" << "Chosen Word: " << chosen_word;
    cout << "\n" << "\n" << "------------------------------------------------";
    
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
    cout << "the word with the information you are provided. Good Luck! " << "\n" << "\n";
    string begin = " ";
    cout << "                         Begin Game? (Y/N)";
    cin >> begin;
    if (begin == "Y") {
        cout << "\n";
        cout << "                   SYSTEM RANDOMLY PICKING WORD...";
        sleep(2);
    }

    return 0;
}
