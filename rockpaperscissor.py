import random
user_score = 0
com_score = 0
options = ["snake","water","gun"]

while True:
    user_input = input("Choose snake/water/gun or q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    # else:
    #     continue

    comp_choose = random.randint(0,2)
    comp_ansr = options[comp_choose]

    if user_input == "snake" and comp_ansr == "water":
        print("You scored!")
        user_score += 1
    elif user_input == "water" and comp_ansr == "gun":
        print("You scored!")
        user_score += 1
    elif user_input == "gun" and comp_ansr == "snake":
        print("You scored!")
        user_score += 1
    elif user_input == comp_ansr:
        print("Same choice. No scores...")
    else:
        print("Computer scored!")
        com_score += 1
print("Bye")

# works on replit