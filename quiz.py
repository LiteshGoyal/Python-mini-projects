import time
print("zzz😴")
time.sleep(3)
name = input("Woah!😯 Who disturbed my sleep? Tell me your name: ")
time.sleep(2)
print(f"So it's {name}...Hmmm I see👀")
time.sleep(1)
print("So what are you here for?")
start = input("To play a game? ")
if start.lower() != "yes":
    quit()

print("Ok! Let's begin⌛.")
time.sleep(1)
print("Here comes the first question on your screen...")
time.sleep(1)
ques = input("What does CPU stand for? ")
print("Let me find the answer...")
time.sleep(2)
score = 0
if ques.lower() != "central processing unit":
    print("You got it wrong😂")

else:
    print("Good one! You got it right.")
    score += 1

ques = input("What does GPU stand for? ")
print("Let me find the answer...")
time.sleep(2)
if ques.lower() != "graphical processing unit":
    print("You got it wrong😂")

else:
    print("Good one! You got it right.")
    score += 1

ques = input("What does RAM stand for? ")
print("Let me find the answer...")
time.sleep(2)
if ques.lower() != "random access memory":
    print("You got it wrong😂")

else:
    print("Good one! You got it right.")
    score += 1

ques = input("What does PS stand for? ")
print("Let me find the answer...")
time.sleep(2)
if ques.lower() != "play station":
    print("You got it wrong😂")

else:
    print("Good one! You got it right.")
    score += 1

time.sleep(1)
print("Ok.. Time to wrap it up")
time.sleep(1)
print(f"You scored {score} marks")

