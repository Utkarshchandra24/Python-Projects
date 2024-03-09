#Day04: Rock, Paper and Scissors Game

import random

print("Welcome to Rock, Paper and Scissors Game!")

rock,paper,scissors = 0,1,2
user = input("Select the option between Rock(R),Paper(P) and Scissors(S):").upper()

if user=="R":
    user = 0
elif user == "P":
    user = 1
elif user == "S":
    user = 2
else:
    print("Invalid Input, Please select between Rock(R),Paper(P) and Scissors(S)")
    print("User entered invalid input,Please Try again!,Please check the input you have given")
    exit()

comp = random.randint(0,2)
# print("Computer selected number =",comp)
if comp==0:
    compres = "Rock"
elif comp==1:
    compres = "Paper"
elif comp==2:
    compres = "Scissors"

print("Computer selected:",compres)

if (user<comp):
    print("You Lose!")
elif (user>comp):
    print("You Win!")
elif (user==comp):
    print("Its a tie")
else:
    print("User entered invalid input,Please Try again!,Please check the input you have given")



