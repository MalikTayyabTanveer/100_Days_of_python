print("welcome to the Treasure Island\nyour mission is to find the treasure")

step = input("do you wanna go left or right\ntype 'left' or 'right'\n").lower()

if step == "right":
    next_step = input("You arrived at the lake. do you want to 'swim' or 'wait' for the boat\n").lower()
    if next_step == "wait":

        door = input("you arrived at the Island. Which door you want to choose\n'Red' or 'white' ").lower()
        if door == "red":
            print("You win! Treasure is in front of you.")
        elif door == "white":
            print("Game over! white can not always a right color")
        else:
            print("choose 'red' or 'white'")
    
    elif next_step == "swim":
        print("Game over! Lake is full of sharks.")
    else:
        print("write 'swim' or 'wait'. ")

elif step =="left":
    print("game over!")
else:
    print("Choose left or right!")