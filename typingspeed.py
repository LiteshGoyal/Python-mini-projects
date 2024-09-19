from time import *
import random

samples = ['In the interview, the main question is- why do you need a gun? Self-defense is stated as one of','the customer obviously have to contact the dealer for the procurement of the gun','One cannot issue letters just on the basis of the authorities but, the delivery can be permitted to the retainer only on the behalf of the customer.']

typingtext = random.choice(samples)
splittedtext = typingtext.split(" ")
# print(splittedtext)

print(typingtext)

time_1 = time()
user_inp = input("Start typing:")
time_2 = time()
splittedinput = user_inp.split(" ")
print(splittedinput)
print(time_1)
print(time_2)
speed = len(user_inp)/(round(time_2,2) - round(time_1,2))
print(round(speed,2), "w/sec")
i = 0
err = 0
while i<len(splittedtext):
    if splittedinput[i] == splittedtext[i]:
        i += 1
    else:
        err += 1
        i += 1
    
print(err)
