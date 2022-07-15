import time

x = 0
while True:
    x = x + 1
    if x % 5 == 0 and x % 3 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
    time.sleep(0.5)
    print(" ")
    print("------------------")
    print(" ")