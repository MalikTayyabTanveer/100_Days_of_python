# A simple game that you can play with the computer.

import random 

game  = ["Rock", "Paper", "scissor"]

user = int(input("enter your choice 0 for 'Rock' 1 for 'Paper' and 2 for 'Scissors' : "))

num = random.randint(0,2)
print("computer choice : ",game[num])
if user >= 0 and user <= 2:
    if user == 0 and num == 2:
        print("You win!")
    elif user == 1 and num == 0:
        print("You win!")
    elif user == 2 and num == 1:
        print("You win!")
    elif user == num:
        print("it's a draw!")
    else:
        print("you lose!")
else:
    print("Enter the proper number.")