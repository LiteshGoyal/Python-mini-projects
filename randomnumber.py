import random

limit = int(input("Upto which number you can guess? "))
number = random.randint(0,limit)
guess = 0
while True:
    user = int(input("Guess the number: "))
    if user > number:
        print("You were above the number")
        guess += 1
    elif user<number:
        print("You were under the number")
        guess += 1
    else:
        print(f"You got it right in {guess} tries")
        break
        
