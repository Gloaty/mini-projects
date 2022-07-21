#include <iostream>
#include <string> 
#include <fstream>

using std::string;
using std::endl;
using std::ofstream;

int gBudget, mBudget, gSpent, gDeposit, mDeposit, mSpent;
void budgetDeclare() {
    std::cout << "Enter your groceries budget: " << endl;
    std::cin >> gBudget;
    std::cout << "Enter your mortgage budget: " << endl;
    std::cin >> mBudget;
}

void grocerySpending() {
    std::cout << "Enter how much you spent on groceries: " << endl;
    std::cin >> gSpent;
    std::cout << "You spent $" << gSpent << " on groceries." << endl;
    gBudget = gBudget - gSpent;
    std::cout << "Groceries Budget: " << gBudget << endl;
}

void groceryDeposit() {
    std::cout << "Enter how much you wish to deposit on groceries: " << endl;
    std::cin >> gDeposit;
    std::cout << "You deposited $" << gDeposit << " on groceries." << endl;
    gBudget = gBudget + gDeposit;
    std::cout << "Groceries Budget: " << gBudget << endl;
}

void rentDeposit() {
    std::cout << "Enter how much you wish to deposit on mortgage: " << endl;
    std::cin >> mDeposit;
    std::cout << "You deposited $" << mDeposit << " on mortgage." << endl;
    mBudget = mBudget + mDeposit;
    std::cout << "Mortgage Budget: " << mBudget << endl;
}

void rentSpending() {
    std::cout << "Enter how much you spent on mortgage: " << endl;
    std::cin >> mSpent;
    std::cout << "You spent $" << mSpent << " on mortgage." << endl;
    mBudget = mBudget - mSpent;
    std::cout << "Mortgage: " << mBudget << endl;
}

void budgetSave() {
    ofstream budgetsavefile;
    budgetsavefile.open("budgetsave.dat");
    budgetsavefile << gBudget << endl;
    budgetsavefile << mBudget << endl;
    budgetsavefile.close();
}

void budgetTxt() {
    ofstream budgetfile;
    budgetfile.open("budgets.txt");
    budgetfile << "Groceries Budget: " << gBudget << endl;
    budgetfile << "Mortgage Budget: " << mBudget << endl;
    budgetfile.close();
}

int main()
{
    string menuChoice = "NULL";
    budgetDeclare();
    goto mainmenu;

    mainmenu:
        std::cout << "Welcome to the budget manager!" << endl;
        std::cout << "Would you like to view your current budgets, " << endl;
        std::cout << "or would you like to make a deposit or withdrawal from your budgets?" << endl;
        std::cout << "Enter 'view' to view your current budgets, or 'deposit' or 'withdrawal' to make a deposit or withdrawal." << endl;
        std::cin >> menuChoice;
        if (menuChoice == "view") {
            string txtchoice = "NULL";
            std::cout << "Groceries Budget: " << gBudget << endl;
            std::cout << "Mortgage Budget: " << mBudget << endl;
            std::cout << "Would you like a text file of your current budgets? (y/n)" << endl;
            std::cin >> txtchoice;
            if (txtchoice == "y") {
                budgetTxt();
            }
            else {
                std::cout << "Thank you for using our budget manager!" << endl;
            }
        }
        else if (menuChoice == "deposit") {
            groceryDeposit();
            rentDeposit();
            if (gBudget > 9999) {
                std::cout << "You have exceeded your budget for groceries." << endl;
                std::cout << "VALUE-ERR: BUFFER OVERFLOW; SETTING BACK TO MAXIMUM VALUE" << endl;
                gBudget = 9999;
            }
            else if (mBudget > 9999) {
                std::cout << "You have exceeded your budget for mortgage." << endl;
                std::cout << "VALUE-ERR: BUFFER OVERFLOW; SETTING BACK TO MAXIMUM VALUE" << endl;
                mBudget = 9999;
            }
            else if (gBudget > 9999 && mBudget > 9999) {
                std::cout << "You have exceeded your budget for groceries and mortgage." << endl;
                std::cout << "VALUE-ERR: BUFFER OVERFLOW; SETTING BACK TO MAXIMUM VALUE" << endl;
                gBudget = 9999;
                mBudget = 9999;
            }
            else {
                std::cout << "Groceries Budget: " << gBudget << endl;
                std::cout << "Mortgage Budget: " << mBudget << endl;
            }
        }
        else if (menuChoice == "withdrawal") {
            grocerySpending();
            rentSpending();
            if (gBudget < 0 || mBudget < 0) {
                std::cout << "You have gone over your budget!" << endl;
            }
        }
        else {
            std::cout << "Invalid input." << endl;
        }
        string resetchoice = "NULL";
        std::cout << "Would you like to return to main menu with your current budgets? (y/n)" << endl;
        std::cin >> resetchoice;
        if (resetchoice != "y") {
            std::cout << "Thank you for using our budget manager!" << endl;
        }
        else {
            goto mainmenu;
        }
    budgetSave();
    return 0;
}