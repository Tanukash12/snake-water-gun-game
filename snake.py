'''
1 for snake
-1 for water
0 for gun

Snake vs. Water: Snake wins because it drinks the water 
Water vs. Gun: Water wins because the gun drowns 
Gun vs. Snake: Gun wins because it kills the snake 
Draw: If both players choose the same object
'''
import random

youdict = { "s" : 1, "w" : -1, "g" : 0}
while True:
    youstr = input("Enter you choice (s for snake, w for water, g for gun): ")
    if youstr not in youdict:
            print("Please choose the appropriate player")
            continue
    else: 
        you = youdict[youstr]
        computer = random.choice([-1, 1, 0])

        # snake vs water
        if(computer == -1 and you == 1):
            print("you chose snake")
            print("computer chose water")
            print("you win!")
        elif(computer == 1 and you == -1):
            print("you chose water")
            print("computer chose snake")
            print("you loss!")
        # water vs gun
        elif(computer == -1 and you == 0):
            print("you chose gun")
            print("computer chose water")
            print("you loss!")
        elif(computer == 0 and you == -1):
            print("you chose water")
            print("computer chose gun")
            print("you win!")
        #gun vs snake 
        elif(computer == 0 and you == 1):
            print("you chose snake")
            print("computer chose gun")
            print("you loss!")
        elif(computer == 1 and you == 0):
            print("you chose gun")
            print("computer chose snake")
            print("you win!")
        elif(computer == you):
            if(you == -1):
                print("you chose water")
                print("computer chose water")
            elif(you == 1):
                print("you chose snake")
                print("computer chose snake")
            else:
                print("you chose gun")
                print("computer chose gun")
            print("match draw!")
        print(" ")
        choice = input("Press yes or no to continue (y/n): ")
        if(choice.lower() != 'y'):
            print("Exiting the game!")
            break
        else: 
            continue
  