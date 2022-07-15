#guess the number game ai vs user
import random
import time
previous_ai_limiter = 0
current_ai_limiter = 0
print("Welcome to Guess the Number! ")
print("The goal of this game is to guess the number with hints as to whether")
print("you are higher of lower than the number provided by the program. ")
print("Enjoy! ")
print(" ")
print("Guess the Number: Beta")
start  = input("    Start? (y/n)")
if start == ("y"):
    target = random.randrange(1000, 0, -1)
if start == ("n"):
    print("Too bad!")
    print("Goodbye!")
    exit()
while True:
        print("User turn: Take a guess!")
        print(target)
        userguess = int(input("Type number here: "))
        if userguess < target:
            print("Your guess is lower than the target number! ")
        elif userguess > target:
                print("Your guess is higher than the target number! ")
        elif userguess == target:
            print("You are spot on! Well done! ")
            print("User wins! Computer loses!")
            exit()
        aiguess = random.randrange(1000, 0, -1)
        print("The computer will now take a guess! ")
        time.sleep(2)
        print("AI Guess = " + str(aiguess))
        current_ai_limiter = int(aiguess)
        print(current_ai_limiter)
        print(previous_ai_limiter)
        if int(aiguess) < target:
            print("The computer's guess is lower than the target! ")
            aiguess = random.randrange(int(previous_ai_limiter), 1000, 1001)
            if previous_ai_limiter < current_ai_limiter:
                (previous_ai_limiter) = (current_ai_limiter)
        if int(aiguess) > target:
            print("The computer's guess is higher than the target! ")
            aiguess = random.randrange(int(previous_ai_limiter), 0, -1)
            if previous_ai_limiter < current_ai_limiter:
                (previous_ai_limiter) = (current_ai_limiter)
        if int(aiguess) == target:
            print("The computer's guess is spot on! Congrats, AI! ")
            print("Computer wins! User loses!")
            exit()
