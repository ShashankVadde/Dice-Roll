import random

Dice_Rolls = [1, 2, 3, 4, 5, 6]
Dice_Rolls_2 = [1, 2, 3, 4, 5, 6, 7, 8]

print("The first dice has ", Dice_Rolls, "sides")
print("The second dice has ", Dice_Rolls_2, "sides")


def roll():
    side = input("Do you want to roll a(n) 6 sided or 8 sided die? (6/8) ")
    print(side) 
    if side == "6":
        roll = input("Type (six) to roll the dice: ")
    elif side == "8":
        roll = input("Type (eight) to roll the dice: ")
    else:
        print("Alright, come back next time! ")

    if roll == "six":
        roll_dice = random.choice(Dice_Rolls)
        print("Your number is: " + str(roll_dice))
        breakpoint
    elif roll == "eight":
        roll_dice = random.choice(Dice_Rolls_2)
        print("Your number is: " + str(roll_dice))
        breakpoint
    else:
        print("Alright, come back next time! ")
        breakpoint
        
roll()

def roll_again():
    while True:
        roll_again = input("Do you want to roll again ? (y/n)\n")
        if roll_again == "y":
            roll()
        else:
            print("Alright, come back next time! ")
            break
        
roll_again()